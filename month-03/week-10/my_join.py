import pandas as pd
import geopandas as gpd

pd.set_option("display.max_columns", 50)

health_settlements = gpd.read_file("data/nigeria_health_facilities.gpkg", layer="nga_health_facilities_v3_0")
health_fac = pd.read_csv("data/health_facilities_bashorun.csv")

first_try = health_fac.merge(health_settlements, left_on="Name of Facility", right_on="facility_n", how="left")

matched = first_try["Name of Facility"].notna().sum()
print("Matched on first try:", matched, "of", len(health_fac))
print(first_try[["Name of Facility", "ward_stand", "settlement"]])

def clean_name(name) :
    return name.strip().upper().replace("-", " ")

health_fac["join_key"] = health_fac["Name of Facility"].apply(clean_name)
health_settlements["join_key"] = health_settlements["facility_n"].apply(clean_name)


joined = health_fac.merge(health_settlements, on="join_key", how="left")
joined = joined[joined["ward_stand"] == "Bashorun"]
matched = joined["Name of Facility"].notna().sum()
print("Matched after cleaning:", matched, "of", len(health_fac))
print(joined[["Name of Facility", "settlement"]])