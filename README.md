# Create AllMaps Annotations

## Atlas de Verniquet from BnF

```shell
python3 create_annotations.py --csv_file bnf_verniquet.csv --iiif_version 1 --proj4_string "+proj=aeqd +lat_0=48.83635863 +lon_0=2.33652533 +x_0=0 +y_0=0 +ellps=GRS80 +to_meter=1.94903631 +no_defs" output/bnf_verniquet/annotation_bnf_verniquet.json
```

## Atlas de Verniquet from David Rumsey

```shell
python3 create_annotations.py --csv_file rumsey_verniquet.csv --iiif_version 2 --proj4_string "+proj=aeqd +lat_0=48.83635863 +lon_0=2.33652533 +x_0=0 +y_0=0 +ellps=GRS80 +to_meter=1.94903631 +no_defs" output/rumsey_verniquet/annotation_rumsey_verniquet.json
```

## Atlas de Jacoubet from 

```shell
python3 create_annotations.py --csv_file jacoubet.csv --iiif_version 2 --proj4_string "+proj=aeqd +lat_0=48.83635863 +lon_0=2.33652533 +x_0=0 +y_0=0 +ellps=GRS80 +no_defs" --output_annotation_file output/bhvp_jacoubet/annotation_bhvp_jacoubet.json
```


## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1878
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935100
```shell
python3 create_annotations.py --csv_file bhdv_atlas_municipal_1878.csv --iiif_version 3 --proj4_string "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" --output_annotation_file output/bhdv_atlas_municipal_1878/annotation_bhdv_atlas_municipal_1878.json --input_mask ./bhdv_atlas_municipal_1878/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1886
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935114
```shell
python3 create_annotations.py --csv_file bhdv_atlas_municipal_1886.csv --iiif_version 3 --proj4_string "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" --output_annotation_file output/bhdv_atlas_municipal_1886/annotation_bhdv_atlas_municipal_1886.json --input_mask ./bhdv_atlas_municipal_1886/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1887 
from http://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935115
```shell
python3 create_annotations.py --csv_file bhdv_atlas_municipal_1887.csv --iiif_version 3 --proj4_string "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" --output_annotation_file output/bhdv_atlas_municipal_1887/annotation_bhdv_atlas_municipal_1887.json --input_mask ./bhdv_atlas_municipal_1887/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1888
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935116
```shell
python3 create_annotations.py --csv_file bhdv_atlas_municipal_1888.csv --iiif_version 3 --proj4_string "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" --output_annotation_file output/bhdv_atlas_municipal_1888/annotation_bhdv_atlas_municipal_1888.json --input_mask ./bhdv_atlas_municipal_1888/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1900 (1895 tirage 1900)
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935510
```shell
python3 create_annotations.py --csv_file bhdv_atlas_municipal_1900.csv --iiif_version 3 --proj4_string "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" --output_annotation_file output/bhdv_atlas_municipal_1900/annotation_bhdv_atlas_municipal_1900.json --input_mask ./bhdv_atlas_municipal_1900/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1925
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935524
```shell
python3 create_annotations.py --csv_file bhdv_atlas_municipal_1925.csv --iiif_version 3 --proj4_string "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" --output_annotation_file output/bhdv_atlas_municipal_1925/annotation_bhdv_atlas_municipal_1925.json --input_mask ./bhdv_atlas_municipal_1925/masks.gpkg
```

## Atlas municipal des vingt arrondissements de la ville de Paris dressé sous l'administration de M. E. Poubelle, préfet, sous la direction de M. Alphand,... par les soins de M. L. Fauve, géomètre en chef, avec le concours des géomètres du Plan de Paris... 1937
from https://bibliotheques-specialisees.paris.fr/ark:/73873/pf0000935528
```shell
python3 create_annotations.py --csv_file bhdv_atlas_municipal_1937.csv --iiif_version 3 --proj4_string "+proj=omerc +gamma=0.00047289 +lonc=2.33652533 +lon_0=2.33652533 +lat_0=48.83635864 +lat_ts=48.83635864 +x_0=0 +y_0=0 +no_defs +ellps=GRS80" --output_annotation_file output/bhdv_atlas_municipal_1937/annotation_bhdv_atlas_municipal_1937.json --input_mask ./bhdv_atlas_municipal_1937/masks.gpkg
```

## Parcellaire de Paris des ingénieurs géographes, environ 1820-1833, Service Historique de la Défense, SHDGR/GR/6/M/J10/C/1188 
First, we create the masks for manual edit:
```shell
python create_masks.py SHDGR__GR_6_M_J10_C_1188.csv SHDGR__GR_6_M_J10_C_1188.masks.gpkg```

```shell
python create_annotations.py --csv_file SHDGR__GR_6_M_J10_C_1188.csv --iiif_version 3 --proj4_string "+proj=aeqd +lat_0=48.83635863 +lon_0=2.33652533 +x_0=0 +y_0=0 +ellps=GRS80 +to_meter=1.94903631 +no_defs" --output_annotation_file output/SHDGR__GR_6_M_J10_C_1188/SHDGR__GR_6_M_J10_C_1188.json --input_mask SHDGR__GR_6_M_J10_C_1188.masks.gpkg
```

## Atlas général de Paris (CP/F/31/1 et 2)
from https://www.siv.archives-nationales.culture.gouv.fr/siv/IR/FRAN_IR_057290
```shell
python create_annotations.py --csv_file ~/data/3_V_GEOREFERENCEE_ADRESSES_PARIS_PLAN_CADASTRAL_AN_F31_1_ET_2/cadastre_general_paris.csv --proj4_string "+proj=aeqd +lat_0=48.83635863 +lon_0=2.33652533 +x_0=0 +y_0=0 +ellps=GRS80 +to_meter=1.94903631 +no_defs" --output_annotation_file output/Atlas_general_de_Paris/Atlas_general_de_Paris.json --input_mask ~/data/3_V_GEOREFERENCEE_ADRESSES_PARIS_PLAN_CADASTRAL_AN_F31_1_ET_2/masks.gpkg --mask_attribute MASK --tps --inverse
```