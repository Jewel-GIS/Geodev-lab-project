import pandas as pd
import geopandas as gpd

table = pd.read_csv("data/health_fac_study_area.csv")
print(table.head(3))

health = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
)
print(health.head(3))
print(health.crs)

health.to_file("data/processed/health_fac_study_area.gpkg", layer="health_facilities")
print("Saved", len(health), "health_facilities")