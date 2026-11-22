import geopandas as gpd

ward = gpd.read_file("data/Bashorun_ward_boundary.gpkg", layer="study_area")
print("CRS:", ward.crs)

ward["area_wrong"] = ward.area
print(ward[["ward", "area_wrong"]].head(3))

print("Suggested UTM:", ward.estimate_utm_crs())
wards_utm = ward.to_crs(epsg=32631)
wards_utm["area_km2"] = wards_utm.area / 1_000_000
print(wards_utm[["ward", "area_km2"]].head(3))
print("Ibadan North total:", round(wards_utm["area_km2"].sum(), 1), "km2")