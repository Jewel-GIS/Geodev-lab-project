import geopandas as gpd

settlements = gpd.read_file("data/Settlements_Bashorun_ward.gpkg", layer="settlements_study_area").to_crs(epsg=32631)

layer = settlements.copy()
layer["geometry"] = layer.make_valid()

print("Count of valid polygons before:", settlements.is_valid.sum())
print("Count of valid polygons after:", layer.is_valid.sum())