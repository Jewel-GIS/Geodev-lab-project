## OSM roads, Bashorun Ward, Ibadan North
- Extracted [09/10/2026] via QuickOSM, highway =*
- 1,144 features
- COMPLETENESS: good in built-up area. Compared my own
street: 9 of 11 roads present. Sparse at the northern edge.
- CURRENCY: 
- POSITIONAL: roads align well with satellite imagery, no
systematic offset visible.
- ATTRIBUTE: only 18% carry a surface tag, so paved and
unpaved cannot be separated reliably.
- FITNESS: adequate for access analysis in the built-up
area. Not adequate for a paved-road question.

## NGA Health Facilities
- Extracted [09/10/2026] via GRID3
- 41,778 features [clipped 20 features to Bashorun ward]
- COMPLETENESS: good in study area. Compared my own
- CURRENCY: last edited August 14, 2026. 
- POSITIONAL: Health Facilities align well with known facilities, no
systematic offset visible.
- ATTRIBUTE: Fifteen functional, three unfunctional and two unknown health facilities
- FITNESS: adequate for analysis in the study area

## Nigeria Operational Wards
- Extracted [09/10/2026] via GRID3
- 351 features (filtered for Oyo State only)
- COMPLETENESS: good in study area. Compared my own
- CURRENCY: last edited July 15, 2026. 
- POSITIONAL: Wards align well with known wards, no
systematic offset visible.
- ATTRIBUTE: contains all wards in Oyo State
- FITNESS: adequate for analysis in the study area

## NGA POP 2026 100m
- Extracted [09/10/2026] via WorldPOP
- Raster Image, Band 1 [clipped to study area, Min: 43.7452, Max: 162.7849]
- COMPLETENESS: good in study area.
- CURRENCY: 2026. 
- POSITIONAL: Raster layer of population in Nigeria.
- ATTRIBUTE: Fully covers Nigerian population
- FITNESS: adequate for analysis in the study area

## CRS and preparation
All source layers arrived in EPSG:4326
- Study area: Bashorun ward, Ibadan North, extracted from GRID3 wards
- All layers clipped to study area, then reprojected to EPSG:32631 (UTM 31N)
- Area check: Bashorun ward, Ibadan North 7 km2, matches published figure
- Working files in data/processed/, raw files untouched

