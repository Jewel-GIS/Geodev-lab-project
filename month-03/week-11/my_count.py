import geopandas as gpd
import pandas as pd

pd.set_option("display.max_rows", None)

settlements = gpd.read_file("data/Settlements_Bashorun_ward.gpkg", layer="settlements_study_area").to_crs(epsg=32631)
facilities = gpd.read_file("data/health_fac_study_area.gpkg", layer="health_facilities").to_crs(epsg=32631)

settlements["geometry"] = settlements.geometry

# buffer
reach = facilities.copy()
reach["geometry"] = facilities.buffer(2000)
print("Buffered", len(reach), "facilities")

# count facilities per ward
joined = gpd.sjoin(
    facilities, settlements[["block_id", "geometry"]], how="inner", predicate="within"
)
counts = joined.groupby("block_id").size().rename("facility_count").reset_index()
settlements = settlements.merge(counts, on="block_id", how="left")
settlements["facility_count"] = settlements["facility_count"].fillna(0).astype(int)
print(settlements["block_id"], ["facility_count"])
print("Total counted:",settlements["facility_count"].sum(), "of", len(facilities))