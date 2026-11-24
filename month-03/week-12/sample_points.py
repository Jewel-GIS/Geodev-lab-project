import geopandas as gpd
import rasterio

with rasterio.open(r"C:\Users\Jewel.Oluwole\dev\Geodev-lab-project\data\raw\dem.tif") as src:
    facilities = gpd. read_file(
    r"C:\Users\Jewel.Oluwole\dev\Geodev-lab-project\data\processed\facilities.gpkg", layer="facilities"
    ).to_crs(src.crs)
    coords = [(p.x, p.y) for p in facilities.geometry]
    facilities["elevation_m"] = [values[0] for values in src.sample(coords)]

print(facilities[["name", "elevation_m"]].head())