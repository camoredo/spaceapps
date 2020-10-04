# Data Gathering
All data is taken from the [Copernicus Open Access Hub](https://scihub.copernicus.eu/), and processed using [Acolite](https://github.com/acolite/acolite) and [SNAP Sentinel Toolkits](http://step.esa.int/main/download/snap-download/). 

## 1. Downloading Data
To download satellite images, visit the [Copernicus Open Access Hub](https://scihub.copernicus.eu/) and register for an account. Selected areas of interest are based on [(Biermann, et. al., 2020)](https://www.nature.com/articles/s41598-020-62298-z), as well as some other areas discussed by the group.

The satellite product used is **Sentinel-2 MSI L-1C.** Made sure that the images selected have _minimal cloud coverage_.

## 2. Preprocessing
Once the data has been downloaded, the following preprocessing steps need to be executed:
1. **Atmospheric Correction** (using [Acolite])
2. **Land/Sea Masking** (using the [SNAP Sentinel Toolkits](http://step.esa.int/main/download/snap-download/))

## 3. NDVI/FDI Calculation
The equations for NDVI and FDI were derived form [(Biermann et. al., 2020)](https://www.nature.com/articles/s41598-020-62298-z) and [(Topouzelis et. al., 2020)](https://www.mdpi.com/2072-4292/12/12/2013/htm). Use the **Band Math** tool to plug in the following expressions.
#### NDVI
```
(rhos_833 - rhos_665) / (rhos_833 + rhos_665)
```
#### FDI
```
rhos_833 - (rhos_739 + ((rhos_1610 - rhos_739) * ((833-665)/(1610-665))*10))
```
After getting both indices, use a **mask** to get pixels of suspected plastics. The threshold values were derived from [(Biermann et. al., 2020)](https://www.nature.com/articles/s41598-020-62298-z):

```
ndvi > 0.02 and ndvi < 0.24 and fdi > 0.018 and fdi < 0.067
```
## 4. Exporting Pixel Data
Once the mask has been applied, export the pixel data into a `.txt` file (_Raster > Export > Mask Pixels_). This will be used by the Python script in the root directory.

## 5. Convert to two JSON files
After retrieving the `.txt` file from the SNAP Toolkit GUI, import the contents into a `pandas` dataframe and re-export it as JSON files: one to represent the scatter plot and another to represent a heatmap. The scatter plot representation is the latitude and longitude pixel values from the mask. The heatmap representation, on the other hand, is the same representation, but neighboring pixel values are aggregated to create the heatmap values.
