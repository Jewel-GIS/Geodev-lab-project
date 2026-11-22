import geopandas as gpd

ward = gpd.read_file("data/Bashorun_ward_boundary.gpkg", layer="study_area").to_crs(epsg=32631)
facilities = gpd.read_file(
    "data/health_fac_study_area.gpkg", layer="health_facilities"
).to_crs(epsg=32631)

ward["area_km2"] = ward.area / 1_000_000

reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)
reach = reach.dissolve()

uncovered = gpd.overlay(ward, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area / 1_000_000

gaps = uncovered[["ward", "uncovered_km2"]]
result = ward.merge(gaps, on="ward", how="left")
result["uncovered_km2"] = result["uncovered_km2"]. fillna(0)
share = result["uncovered_km2"] / result["area_km2"] * 100
result["uncovered_pct"] = share.round(1)
print(result[["ward", "area_km2","uncovered_km2", "uncovered_pct"]].round(2))