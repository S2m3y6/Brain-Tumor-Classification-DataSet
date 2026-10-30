# Brain Tumor Classification Dataset

Dit project bevat een MRI/scan-dataset voor beeldclassificatie van hersentumoren. De dataset is georganiseerd in mappen per klasse en per aanzicht, zodat een model verschillende soorten tumoren en niet-tumorbeelden kan herkennen.

## 1. Overzicht van het project

De repository bestaat uit:

- beeldbestanden per tumortype en aanzicht
- gesorteerde trainings- en testsets
- een opgesplitste 80/20 dataset
- CSV-bestanden met labels en voorspellingen
- notebooks voor data-preparatie en modeltraining
- een script om de dataset opnieuw te verdelen

## 2. Klassen in de dataset

De afbeeldingen zijn verdeeld in vier klassen:

1. `glioma_tumor` – beeld van een glioma-tumor
2. `meningioma_tumor` – beeld van een meningioma-tumor
3. `no_tumor` – geen tumor aanwezig
4. `pituitary_tumor` – beeld van een pituitary-tumor

Deze klassen komen voor in meerdere aanzichten van de hersenen.

## 3. Beeldweergaven (views)

Elke klasse is ook onderverdeeld in drie beeldoriëntaties:

- `Axiaal` / `axiaal`
- `Coronaal` / `coronaal`
- `Sagittaal` / `sagittaal`

Dit is belangrijk, omdat de modeltraining niet alleen onderscheid maakt tussen tumorsoorten, maar ook rekening houdt met hoe de scan is genomen.

## 4. Structuur van de mappen

### 4.1 Hoofdmap: `Training` en `Testing`

Deze mappen bevatten de basisverdeling voor trainings- en testbeelden.

```text
Training/
  glioma_tumor/
  meningioma_tumor/
  no_tumor/
  pituitary_tumor/

Testing/
  glioma_tumor/
  meningioma_tumor/
  no_tumor/
  pituitary_tumor/
```

Deze folders zijn relatief eenvoudig: de beelden zijn per klasse gegroepeerd zonder extra niveau voor kijkrichting.

### 4.2 Map: `Sorted`

In `Sorted` is de data verder gestructureerd per beeldzicht en klasse:

```text
Sorted/
  Training/
    axiaal/
      glioma_tumor/
      meningioma_tumor/
      no_tumor/
      pituitary_tumor/
    coronaal/
      ...
    sagittaal/
      ...
  Testing/
    axiaal/
      ...
    coronaal/
      ...
    sagittaal/
      ...
```

Belangrijk:

- `Training` en `Testing` bestaan hier opnieuw
- de namen van de weergaven zijn lowercase: `axiaal`, `coronaal`, `sagittaal`
- binnen elke weergave staan weer de vier klassen

### 4.3 Map: `Resplit_80_20`

Deze map is gemaakt met het script `resplit_dataset.py` en bevat een nieuwe verdeling van 80% training en 20% test, per klasse en per beeldzicht.

```text
Resplit_80_20/
  Training/
    Axiaal/
      glioma_tumor/
      meningioma_tumor/
      no_tumor/
      pituitary_tumor/
    Coronaal/
      ...
    Sagittaal/
      ...
  Testing/
    Axiaal/
      ...
    Coronaal/
      ...
    Sagittaal/
      ...
```

Deze set is nuttig om te zorgen dat elk beeldzicht en elke klasse gelijkwaardig vertegenwoordigd zijn in de train/test-splits.

## 5. Datasetgroottes

De repository bevat de volgende aantallen beelden in de belangrijkste datasets:

- `Training`: 2871 afbeeldingen
- `Testing`: 394 afbeeldingen
- `Sorted/Training`: 2878 afbeeldingen
- `Sorted/Testing`: 408 afbeeldingen
- `Resplit_80_20/Training`: 3032 afbeeldingen
- `Resplit_80_20/Testing`: 1084 afbeeldingen

De verschillen in aantallen komen doordat de data opnieuw is gesorteerd en opnieuw is opgesplitst per klasse en per kijkrichting.

## 6. CSV-bestanden

### 6.1 `labeled_scans.csv`

Dit bestand bevat handmatig gelabelde afbeeldingen. De kolommen bevatten onder andere:

- `annotation_id` – unieke identificatie van de annotatie
- `annotator` – wie de annotatie heeft gemaakt
- `choice` – gekozen label, bijvoorbeeld `Axiaal`, `Coronaal`, `Sagittaal`
- `created_at` – tijd van annotatie
- `id` – unieke rij-ID
- `image` – bestandsnaam van de afbeelding
- `lead_time` – tijd die nodig was voor de annotatie
- `updated_at` – laatste wijzigingstijd

Dit bestand is relevant voor de labelworkflow van de dataset.

### 6.2 `predicted_viewtraining.csv`

Dit bestand bevat de voorspelde beeldweergave voor de trainingsset. De structuur is vergelijkbaar met:

```text
klasse\beeldnaam,view
```

Bijvoorbeeld:

```text
glioma_tumor\image(1).jpg,Axiaal
```

Dit betekent dat het model voor die afbeelding een bepaalde weergave heeft voorspeld.

### 6.3 `predicted_viewtesting.csv`

Hetzelfde principe als bij de trainingsset, maar dan voor de testset. Dit is handig om de voorspelde weergave van testafbeeldingen te vergelijken met de echte classificaties van labels.

## 7. Notebooks

### `Data_Preparation.ipynb`

Dit notebook wordt gebruikt voor het voorbereiden van de data:

- inlezen van afbeeldingen
- sorteren en structureren van de dataset
- verdelen in trainings- en testsets
- controleren van mappen en labels
- voorbereiden van input voor het model

### `Model.ipynb`

Dit notebook bevat het trainings- en evaluatieproces van het classificatiemodel. Typisch wordt hierin gewerkt met:

- beeldinvoer
- labels per klasse
- CNN/Deep Learning-modeltraining
- evaluatie op de testset
- analyse van prestaties per klasse of per beeldzicht

## 8. Script: `resplit_dataset.py`

Dit script herverdeelt de beelden in de `Sorted`-dataset naar een 80/20-verdeling per klasse en per beeldzicht.

Het script:

- leest de mappen in `Sorted`
- verwerkt de weergaven `Sagittaal`, `Axiaal` en `Coronaal`
- verzamelt alle bestanden per klasse
- husselt de afbeeldingen
- splitst ze in 80% training en 20% test
- kopieert ze naar `Resplit_80_20`

Het programma bewaart afbeeldingen met unieke namen wanneer er naamconflicten ontstaan.

## 9. Hoe de data bedoeld is om gebruikt te worden

De dataset is ontworpen voor beeldclassificatie van hersentumoren. Een typische workflow is:

1. structuur maken met `Sorted`
2. dataset opsplitsen via `resplit_dataset.py`
3. model trainen in `Model.ipynb`
4. labels en voorspellingen analyseren met de CSV-bestanden
5. evalueren op basis van verschillende weergaven en klassen

## 10. Belangrijkste conclusie

Deze repository bevat geen willekeurige afbeeldingen, maar een gestructureerde verzameling van hersenscans met:

- 4 ziekte-/klassecategorieën
- 3 beeldweergaven
- verschillende trainings-/testverdelingen
- CSV-annotaties en voorspellingen voor analyse

Door deze opbouw kunnen modellen niet alleen het type tumor herkennen, maar ook verschil maken tussen verschillende aanzichten van dezelfde aandoening.

---

## 11. Snelle samenvatting

```text
Brain-Tumor-Classification-DataSet/
├── Data_Preparation.ipynb
├── Model.ipynb
├── labeled_scans.csv
├── predicted_viewtraining.csv
├── predicted_viewtesting.csv
├── resplit_dataset.py
├── Training/
├── Testing/
├── Sorted/
└── Resplit_80_20/
```
