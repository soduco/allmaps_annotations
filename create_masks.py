#!/usr/bin/env python3

import logging
import pandas
from pyproj import CRS, Transformer
import json
from os.path import exists
from osgeo import ogr
import sys

def create_mask(file_name, id, old_format=False):
    # old QGIS gcp point format (no CRS and different pixel/source attribute)
    if old_format:
        imageX='pixelX'
        imageY='pixelY'
    else: 
        imageX='sourceX'
        imageY='sourceY'
    csvFile = pandas.read_csv(file_name,usecols=["mapX","mapY",imageX,imageY],comment='#',skip_blank_lines=True)
    minX = round(csvFile[imageX].min())
    maxX = round(csvFile[imageX].max())
    minY = -round(csvFile[imageY].max())
    maxY = -round(csvFile[imageY].min())

    map_minX = csvFile["mapX"].min()
    map_maxX = csvFile["mapX"].max()
    map_minY = csvFile["mapY"].min()
    map_maxY = csvFile["mapY"].max()

    def to_point(df):
        round_df = df.filter(items=['sourceX', 'sourceY']).apply(round)
        round_df['sourceY'] = round_df['sourceY'].apply(lambda x: -x)
        return round_df.values.astype('int').astype(str).tolist()
    
    line = csvFile[csvFile["mapY"] == map_maxY].sort_values(by=["mapX"],ascending=False)
    points = to_point(line)
    line = csvFile[csvFile["mapX"] == map_minX].sort_values(by=["mapY"],ascending=False)
    points.extend(to_point(line))
    line = csvFile[csvFile["mapY"] == map_minY].sort_values(by=["mapX"],ascending=True)
    points.extend(to_point(line))
    line = csvFile[csvFile["mapX"] == map_maxX].sort_values(by=["mapY"],ascending=True)
    points.extend(to_point(line))
    #from collections import OrderedDict
    #points_without_duplicates = list(OrderedDict.fromkeys(points))
    points_without_duplicates = [i for n, i in enumerate(points) if i not in points[:n]]
    ring = ogr.Geometry(ogr.wkbLinearRing)
    first = None
    for p in points_without_duplicates:
        if not first:
            first = p
        ring.AddPoint(int(p[0]),-int(p[1]))
    if first:
        ring.AddPoint(int(first[0]),-int(first[1]))
    # Create polygon
    poly = ogr.Geometry(ogr.wkbPolygon)
    poly.AddGeometry(ring)
    return id, poly
    

def createMasks(csv_file_name, output_mask):
    logging.basicConfig(level='INFO')
    entries = {}
    csvFile = pandas.read_csv(csv_file_name,usecols=["gcp_file","id","ignore"],skip_blank_lines=True)
    # Create a Graph
    #from rdflib.namespace import _FOAF , _XSD
    #from rdflib import Namespace
    #JSONLD = Namespace("http://www.w3.org/ns/anno.jsonld")
    #g = Graph()
    #bn = BNode()
    #g.add((bn, URIRef('type'), Literal("AnnotationPage")))
    
    for _, row in csvFile.iterrows():
        file_name = row['gcp_file']
        id = row['id']
        if not exists(file_name) or ("ignore" in row and row["ignore"] == 1):
            logging.warning(f"  Skipping file: {file_name}")
        else: 
            logging.debug(f"  Creating mask for file: {file_name} with id {id}")
            entry_id, entry_poly = create_mask(file_name, id)
            entries[entry_id] = entry_poly
    
    from pathlib import Path
    path = Path(output_mask)
    path.parent.mkdir(parents=True, exist_ok=True)
    outputFile = output_mask
    outDriver = ogr.GetDriverByName("GPKG")
    import os
    # Remove output shapefile if it already exists
    if os.path.exists(outputFile):
        outDriver.DeleteDataSource(outputFile)

    # Create the output shapefile
    outDataSource = outDriver.CreateDataSource(outputFile)
    for key, value in entries.items():
        outLayer = outDataSource.CreateLayer(key, geom_type=ogr.wkbPolygon)
        # Add an ID field
        idField = ogr.FieldDefn("id", ogr.OFTInteger)
        outLayer.CreateField(idField)
        # Create the feature and set values
        featureDefn = outLayer.GetLayerDefn()
        feature = ogr.Feature(featureDefn)
        feature.SetGeometry(value)
        feature.SetField("id", 1)
        outLayer.CreateFeature(feature)
        feature = None
    # Save and close DataSource
    outDataSource = None

if __name__ == '__main__':
    if len( sys.argv ) < 3:
        print('[ ERROR ]: you must pass at least two arguments -- the csv file argument, the output mask file')
        sys.exit( 1 )

    csv_file = sys.argv[1]
    output_mask = sys.argv[2]
    createMasks(csv_file_name=csv_file,output_mask=output_mask)
