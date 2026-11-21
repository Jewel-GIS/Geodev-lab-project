import geopandas as gpd
import matplotlib.pyplot as plt

facilities = gpd.read_file("data/health_fac_study_area.gpkg", layer="health_facilities")
bashorun_ward = gpd.read_file("data/Bashorun_ward_boundary.gpkg", layer="study_area")

fig, ax = plt.subplots(figsize=(7, 8))
bashorun_ward.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Health facilities in Bashorun")
ax.set_axis_off()

fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches="tight")
print("Map saved")