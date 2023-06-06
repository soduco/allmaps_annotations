# Create AllMaps Annotations

## Atlas de Verniquet from BnF

```shell
python3 create_annotations.py bnf_verniquet.csv 1 "+proj=omerc +gamma=0.00047289 +lonc=2.33652588 +lon_0=2.33652588 +lat_0=48.83635612 +lat_ts=48.83635612 +x_0=0 +y_0=0 +to_meter=1.9490363 +no_defs +ellps=GRS80" output/bnf_verniquet/annotation_bnf_verniquet.json
```

## Atlas de Verniquet from David Rumsey

```shell
python3 create_annotations.py rumsey_verniquet.csv 2 "+proj=omerc +gamma=0.00047289 +lonc=2.33652588 +lon_0=2.33652588 +lat_0=48.83635612 +lat_ts=48.83635612 +x_0=0 +y_0=0 +to_meter=1.9490363 +no_defs +ellps=GRS80" output/rumsey_verniquet/annotation_rumsey_verniquet.json
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1887 
from http://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935115

```shell
python3 create_annotations.py bhdv_atlas_municipal_1887.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1887/annotation_bhdv_atlas_municipal_1887.json ./bhdv_atlas_municipal_1887/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1888
```shell
python3 create_annotations.py bhdv_atlas_municipal_1888.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1888/annotation_bhdv_atlas_municipal_1888.json ./bhdv_atlas_municipal_1888/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1900 (1895 tirage 1900)
```shell
python3 create_annotations.py bhdv_atlas_municipal_1900.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1900/annotation_bhdv_atlas_municipal_1900.json ./bhdv_atlas_municipal_1900/masks.gpkg
```