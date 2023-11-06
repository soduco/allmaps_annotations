# Create AllMaps Annotations

## Atlas de Verniquet from BnF

```shell
python3 create_annotations.py bnf_verniquet.csv 1 "+proj=aeqd +lat_0=48.83635863 +lon_0=2.33652533 +x_0=0 +y_0=0 +ellps=GRS80 +to_meter=1.94903631 +no_defs" output/bnf_verniquet/annotation_bnf_verniquet.json
```

## Atlas de Verniquet from David Rumsey

```shell
python3 create_annotations.py rumsey_verniquet.csv 2 "+proj=aeqd +lat_0=48.83635863 +lon_0=2.33652533 +x_0=0 +y_0=0 +ellps=GRS80 +to_meter=1.94903631 +no_defs" output/rumsey_verniquet/annotation_rumsey_verniquet.json
```

## Atlas de Jacoubet from 

```shell
python3 create_annotations.py jacoubet.csv 2 "+proj=aeqd +lat_0=48.83635863 +lon_0=2.33652533 +x_0=0 +y_0=0 +ellps=GRS80 +no_defs" output/bhvp_jacoubet/annotation_bhvp_jacoubet.json
```


## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1878
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935100
```shell
python3 create_annotations.py bhdv_atlas_municipal_1878.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1878/annotation_bhdv_atlas_municipal_1878.json ./bhdv_atlas_municipal_1878/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1886
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935114
```shell
python3 create_annotations.py bhdv_atlas_municipal_1886.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1886/annotation_bhdv_atlas_municipal_1886.json ./bhdv_atlas_municipal_1886/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1887 
from http://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935115
```shell
python3 create_annotations.py bhdv_atlas_municipal_1887.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1887/annotation_bhdv_atlas_municipal_1887.json ./bhdv_atlas_municipal_1887/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1888
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935116
```shell
python3 create_annotations.py bhdv_atlas_municipal_1888.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1888/annotation_bhdv_atlas_municipal_1888.json ./bhdv_atlas_municipal_1888/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1900 (1895 tirage 1900)
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935510
```shell
python3 create_annotations.py bhdv_atlas_municipal_1900.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1900/annotation_bhdv_atlas_municipal_1900.json ./bhdv_atlas_municipal_1900/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1925
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935524
```shell
python3 create_annotations.py bhdv_atlas_municipal_1925.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1925/annotation_bhdv_atlas_municipal_1925.json ./bhdv_atlas_municipal_1925/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1937
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935528
```shell
python3 create_annotations.py bhdv_atlas_municipal_1937.csv 3 "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" output/bhdv_atlas_municipal_1937/annotation_bhdv_atlas_municipal_1937.json ./bhdv_atlas_municipal_1937/masks.gpkg
```