#!/usr/bin/env python3

import logging
import pandas
from pyproj import CRS, Transformer
import json
from os.path import exists
from osgeo import ogr, gdal
import sys
import click
from subprocess import Popen, PIPE

def gcp(map_x, map_y, source_x, source_y, inverse = False):
    if inverse:
        return gdal.GCP(source_x, source_y, 0, map_x, map_y)
    return gdal.GCP(map_x, map_y, 0, source_x, source_y)


def get_geotransform(gcp_file, old_format=False, inverse = False):
    # reading the CSV file
    csvFile = pandas.read_csv(gcp_file, comment='#')
    # displaying the contents of the CSV file
    if old_format:
        gcp_list = [gcp(row['mapX'], row['mapY'], row['pixelX'], -row['pixelY'], inverse) for _, row in csvFile.iterrows()]
    else:
        gcp_list = [gcp(row['mapX'], row['mapY'], row['sourceX'], -row['sourceY'], inverse) for _, row in csvFile.iterrows()]
    return gdal.GCPsToGeoTransform(gcp_list)

def get_inv_geotransform(gcp_file, old_format=False):
    # reading the CSV file
    csvFile = pandas.read_csv(gcp_file, comment='#')
    # displaying the contents of the CSV file
    if old_format:
        gcp_list = [gdal.GCP(row['mapX'], row['mapY'], 0, row['pixelX'], -row['pixelY']) for _, row in csvFile.iterrows()]
    else:
        gcp_list = [gdal.GCP(row['mapX'], row['mapY'], 0, row['sourceX'], -row['sourceY']) for _, row in csvFile.iterrows()]
    geo_trans = gdal.GCPsToGeoTransform(gcp_list)
    return gdal.InvGeoTransform(geo_trans)

def get_gcp_text(gcp_file, old_format=False):
    # reading the CSV file
    csvFile = pandas.read_csv(gcp_file, comment='#')
    gcps = []
    if old_format:
        for _, row in csvFile.iterrows():
            gcps.append(f"-gcp {str(row['pixelX'])} {str(row['pixelY'])} {str(row['mapX'])} {str(row['mapY'])}")
    else:
        for _, row in csvFile.iterrows():
            gcps.append(f"-gcp {str(row['sourceX'])} {str(row['sourceY'])} {str(row['mapX'])} {str(row['mapY'])}")
    return ' '.join(gcps)

def inv_transform(gcp_file, lon, lat, old_format=False):
    gcps = get_gcp_text(gcp_file=gcp_file, old_format=old_format)
    p = Popen(f'gdaltransform -i -tps {gcps} -output_xy', stdin=PIPE, stdout=PIPE, universal_newlines=True, shell=True) # run the program
    print(f'gdaltransform -i -tps {gcps} -output_xy')
    output = p.communicate("%s %s\n" % (lon, lat))[0] # pass coordinates
    return tuple(output.rstrip().split(' '))
    
def create_annotation(file_name, input_proj4_string, id, mask_file, mask_attribute, output_file_name, url, iiif_image_api_version, gcp_output, tps=False, inverse=False, old_format=False):
    source = f"{url}/full/max/0/default.jpg"
    crs = CRS.from_proj4(input_proj4_string)
    crs_4326 = CRS.from_epsg(4326)
    transformer = Transformer.from_crs(crs, crs_4326)
    # old QGIS gcp point format (no CRS and different pixel/source attribute)
    if old_format:
        imageX='pixelX'
        imageY='pixelY'
    else: 
        imageX='sourceX'
        imageY='sourceY'
    csvFile = pandas.read_csv(file_name,usecols=["mapX","mapY",imageX,imageY],comment='#',skip_blank_lines=True)
    features = []
    for _, row in csvFile.iterrows():
        (lat,lon) = transformer.transform(row['mapX'], row['mapY'])
        #node = BNode()
        
        features.append({
            "type": "Feature",
            "properties": {
                "pixelCoords": [round(float(row[imageX])), -round(float(row[imageY]))]
            },
            "geometry": {
                "type": "Point",
                "coordinates": [lon,lat]
            }
        })
    poly = None
    minX,maxX,minY,maxY=0,0,0,0
    if mask_file:
        if mask_attribute:
            conn = ogr.Open(mask_file.name)
            lyr = conn.GetLayer(0)
        else:
            conn = ogr.Open(mask_file.name)
            lyr = conn.GetLayerByName( id )
        if lyr is None:
            print('[ ERROR ]: layer name = "%s" could not be found in database "%s"' % ( id, mask_file ))
        else:
            if mask_attribute:
                lyr.SetAttributeFilter(f"{mask_attribute} = '{id}'")
                print(f"{mask_attribute} = '{id}'")
            feature = lyr.GetNextFeature()
            geometry = feature.GetGeometryRef()
            if inverse:
                #inverse the transform
                #inv_geotrans = get_geotransform(gcp_file=file_name, old_format=old_format, inverse=True)
                ring = geometry.GetGeometryRef(0)
                point_count = ring.GetPointCount()
                points = []
                xval = []
                yval = []
                for p in iter(range(point_count)):
                    lon, lat, _ = ring.GetPoint(p)
                    #x, y= gdal.ApplyGeoTransform(inv_geotrans, lon, lat)
                    x, y = inv_transform(gcp_file=file_name, lon = lon, lat=lat, old_format=old_format)
                    x = float(x)
                    y = -float(y)
                    xval.append(x)
                    yval.append(y)
                    points.append(list((str(int(round(x))),str(int(round(y))))))
                poly = ' '.join(list(map(','.join, points)))
                import numpy as np
                minX = int(np.array(xval).min())
                maxX = int(np.array(xval).max())
                minY = int(np.array(yval).min())
                maxY = int(np.array(yval).max())
            else:
                (minX,maxX,minY,maxY) = geometry.GetEnvelope()
                #invert Y values
                minY, maxY = -maxY, -minY
                #convert to int
                minX,maxX,minY,maxY=int(minX),int(maxX),int(minY),int(maxY)
                ring = geometry.GetGeometryRef(0)
                point_count = ring.GetPointCount()
                points = []
                for p in iter(range(point_count)):
                    lon, lat, _ = ring.GetPoint(p)
                    points.append(list((str(int(round(lon))),str(int(-round(lat))))))
                poly = ' '.join(list(map(','.join, points)))
    if not poly:
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

        poly = ' '.join(list(map(','.join, points_without_duplicates)))
        with open(f"tmp_shd/extents_{id}.json", "w") as output_file:
            min = transformer.transform(map_minX, map_minY)
            max = transformer.transform(map_maxX, map_maxY)
            json.dump({
                'westBoundLongitude': str(min[1]),
                'eastBoundLongitude': str(max[1]),
                'southBoundLatitude': str(min[0]),
                'northBoundLatitude': str(max[0])
            }, output_file, indent = 1) 
    image_service_type = "ImageService1"
    if (iiif_image_api_version == 2):
        image_service_type = "ImageService1"
    else: 
        if (iiif_image_api_version == 3):
            image_service_type = "ImageService3"
    if tps:
        transformation = {"type": "thinPlateSpline"}
    else:
        transformation = {
            "type": "polynomial",
            "options": {
                "order": 2
            }
        }
    dictionary = {
        "type": "AnnotationPage",
        "@context": [
            "http://www.w3.org/ns/anno.jsonld"
        ],
        "items": [{
            "type": "Annotation",
            "id": id,
            "@context": [
                "http://www.w3.org/ns/anno.jsonld",
                "http://geojson.org/geojson-ld/geojson-context.jsonld",
                "http://iiif.io/api/presentation/3/context.json"
            ],
            "motivation": "georeferencing",
            "target": {
                "type": "Image",
                "source": source,
                "service": [
                {
                    "@id": url,
                    "type": image_service_type,
                }
                ],
                "selector": {
                "type": "SvgSelector",
                "value": f"<svg width=\"{maxX-minX}\" height=\"{maxY-minY}\"><polygon points=\"{poly}\" /></svg>"
                }
            },
            "body": {
                "type": "FeatureCollection",
                "purpose": "gcp-georeferencing",
                "transformation": transformation,
                "features": features
            }
        }]
    }
    if output_file_name:
        import os
        os.makedirs(output_file_name.rsplit('/',1)[0],exist_ok=True)
        with open(output_file_name, 'w') as output_file:
            output_file.write(json.dumps(dictionary, indent=2))
    if gcp_output:
        print("gcp_output = {}".format(gcp_output))
        output_csv_file = open(gcp_output, 'w')
        output_csv_file.write('#CRS: PROJCRS["unknown",BASEGEOGCRS["unknown",DATUM["Unknown based on GRS80 ellipsoid",ELLIPSOID["GRS 1980",6378137,298.257222101,LENGTHUNIT["metre",1],ID["EPSG",7019]]],PRIMEM["Greenwich",0,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8901]]],CONVERSION["unknown",METHOD["Hotine Oblique Mercator (variant B)",ID["EPSG",9815]],PARAMETER["Latitude of projection centre",48.83635864,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8811]],PARAMETER["Longitude of projection centre",2.33652533,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8812]],PARAMETER["Azimuth of initial line",0,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8813]],PARAMETER["Angle from Rectified to Skew Grid",0.00047289,ANGLEUNIT["degree",0.0174532925199433],ID["EPSG",8814]],PARAMETER["Scale factor on initial line",1,SCALEUNIT["unity",1],ID["EPSG",8815]],PARAMETER["Easting at projection centre",0,LENGTHUNIT["unknown",1.9490363],ID["EPSG",8816]],PARAMETER["Northing at projection centre",0,LENGTHUNIT["unknown",1.9490363],ID["EPSG",8817]]],CS[Cartesian,2],AXIS["(E)",east,ORDER[1],LENGTHUNIT["unknown",1.9490363]],AXIS["(N)",north,ORDER[2],LENGTHUNIT["unknown",1.9490363]],REMARK["PROJ CRS string: +proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80 +to_meter=1.9490363"]]\n')
        csvFile.to_csv(output_csv_file,index=False)
        output_csv_file.close()
    return {
        "id": id, 
        "source": source, 
        "url": url, 
        "image_type":image_service_type, 
        "width": maxX-minX, 
        "height": maxY-minY, 
        "polygon": poly,
        "features": features
    }

def service(url,image_type,iiif_version):
    if iiif_version==3:
        return {
            "@id": url,
            "type": image_type,
            "profile": "http://iiif.io/api/image/3/level2.json"
        }
    else:
        return {
            "@id": url,
            "type": image_type
        }
def annotation(entry,iiif_version, tps):
    if tps:
        transformation = {"type": "thinPlateSpline"}
    else:
        transformation = {
            "type": "polynomial",
            "options": {
                "order": 2
            }
        }
    return {
            "type": "Annotation",
            "id": entry['id'],
            "@context": [
                "http://www.w3.org/ns/anno.jsonld",
                "http://geojson.org/geojson-ld/geojson-context.jsonld",
                "http://iiif.io/api/presentation/3/context.json"
            ],
            "motivation": "georeferencing",
            "target": {
                "type": "Image",
                "source":  entry['source'],
                "service": [service(entry['url'],entry['image_type'],iiif_version)],
                "selector": {
                "type": "SvgSelector",
                "value": f"<svg width=\"{entry['width']}\" height=\"{entry['height']}\"><polygon points=\"{entry['polygon']}\" /></svg>"
                }
            },
            "body": {
                "type": "FeatureCollection",
                "purpose": "gcp-georeferencing",
                "transformation": transformation,
                "features": entry['features']
            }
        }
@click.command()
@click.option('--csv_file', help='csv file name', type=click.File('r'), required=True)
@click.option('--iiif_version', default = 3, help='iiif_version')
@click.option('--proj4_string', help='proj4_string', required=True)
@click.option('--output_annotation_file', help='output annotation file', type=click.File('w'), required=True)
@click.option('--input_mask', help='input_mask', type=click.File('r'), required=True)
@click.option("--mask_attribute", help="set the mask attribute")
@click.option("--tps", is_flag=True, show_default=True, default=False, help="use TPS")
@click.option("--inverse", is_flag=True, show_default=True, default=False, help="use inverse transform for the mask (reproject into image space)")
def createAnnotations(csv_file, iiif_version, proj4_string, output_annotation_file, input_mask = None, mask_attribute = None, tps = False, inverse = False):
    logging.basicConfig(level='INFO')
    entries = []
    csvFile = pandas.read_csv(csv_file,usecols=["gcp_file","id","url","annotation_output","gcp_output","ignore"],skip_blank_lines=True)
    for _, row in csvFile.iterrows():
        file_name = row['gcp_file']
        id = row['id']
        url = row['url']
        output_file_name = row['annotation_output']
        gcp_output = None
        if pandas.notna(row['gcp_output']):
            gcp_output = row['gcp_output']
        if not exists(file_name) or ("ignore" in row and row["ignore"] == 1):
            logging.warning(f"  Skipping file: {file_name}")
        else: 
            logging.debug(f"  Creating annotation for file: {file_name} with id {id} and url {url} ({output_file_name})")
            entry = create_annotation(file_name = file_name, input_proj4_string = proj4_string, id = id, mask_file = input_mask, mask_attribute = mask_attribute, output_file_name = output_file_name, url = url, iiif_image_api_version=iiif_version,gcp_output=gcp_output,inverse = inverse, tps=tps)
            entries.append(entry)
    items = []
    for entry in entries:
        item = annotation(entry,iiif_version,tps)
        items.append(item)
    dictionary = {
        "type": "AnnotationPage",
        "@context": [
            "http://www.w3.org/ns/anno.jsonld"
        ],
        "items": items
    }
    # from pathlib import Path
    # path = Path(output_annotation_file)
    # path.parent.mkdir(parents=True, exist_ok=True) 
    # with open(output_annotation_file, 'w') as output_file:
    #     output_file.write(json.dumps(dictionary, indent=2))
    output_annotation_file.write(json.dumps(dictionary, indent=2))

if __name__ == '__main__':
    # if len( sys.argv ) < 5:
    #     print('[ ERROR ]: you must pass at least four arguments -- the csv file argument, the iiif image api version, the proj4_string and the output file')
    #     sys.exit( 1 )

    # csv_file = sys.argv[1]
    # iiif_image_api_version = int(sys.argv[2])
    # proj4_string = sys.argv[3]
    # output_annotation_file = sys.argv[4]
    # input_mask = None
    # if len( sys.argv ) > 5:
    #     input_mask = sys.argv[5]
    # tps = False
    # if len( sys.argv ) > 6:
    #     if sys.argv[6] == "tps":
    #         tps = True
    # createAnnotations(csv_file_name=csv_file,iiif_version=iiif_image_api_version,proj4_string=proj4_string, output_annotation_file=output_annotation_file, input_mask=input_mask, tps=tps)
    createAnnotations()