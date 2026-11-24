import geopandas as gpd
import numpy as np
import rasterio
from rasterio.mask import mask

with rasterio.open("month-03/week-12/DEM.TIF") as src:
    wards = gpd.read_file("data/Bashorun_ward_boundary.gpkg", layer="study_area").to_crs(src.crs)
    means = []
    for geom in wards.geometry:
        cells, _= mask(src, [geom], crop=True, filled=False)
        means.append(float(cells.mean()))

wards["mean_elevation_m"] = np.round(means, 1)
print (wards[["ward", "mean_elevation_m"]])