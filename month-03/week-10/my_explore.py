import geopandas as gpd

print(gpd.list_layers("data/Clipped roads in bashorun ward Ibadan North LGA.gpkg"))

roads = gpd.read_file("data/Clipped roads in bashorun ward Ibadan North LGA.gpkg", layer="Bashorun ward roads")

print(roads.head())
print("Rows and columns:", roads.shape)
print(roads.geom_type.value_counts())
print("CRS:", roads.crs)
print("Bounds:", roads.total_bounds)