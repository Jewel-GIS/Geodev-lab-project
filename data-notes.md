# Data notes

## GRID3 Nigeria Operational Wards v3.0
- Source: https://data.grid3.org
- Downloaded: [09/10/2026]
- 351 features (filtered for Oyo state only), polygons
- Columns: ward_name (text), lga_name (text), state (text), country (text)
- No nulls in ward_name
- Fully covers Ibadan North LGA

## NGA LGA Boundaries
- Source: https://data.grid3.org
- Downloaded: [09/10/2026]
- 33 features (filtered for Oyo state only), polygons
- Columns: lga_name (text), lga_code (int), state (text)
- No nulls in lga_name
- Fully covers Oyo state

## NGA State Boundaries
- Source: https://data.grid3.org
- Downloaded: [09/10/2026]
- 1 feature (filtered for Oyo state only), polygons
- Columns: state (text), state_code (text)
- No nulls in state
- Fully covers Oyo state

## NGA Health Facilities
- Source: https://data.grid3.org
- Downloaded: [09/10/2026]
- 41,778 features, points
- Columns: facility_name (text), settlement (text),  ward_name (text), lga_name (text), state (text), country (text)
- No nulls in facility_name
- Fully covers Nigeria Health Facilities

## NGA POP 2026 100m
- Source: https://hub.worldpop.org/geodata
- Downloaded: [09/10/2026]
- Data Type: GeoTIFF (Raster)
- Bands: Band 1
- Fully covers Nigeria Population

## OSM roads, extracted via QuickOSM in QGIS
- Query: highway =* within Bashorun ward extent
- Extracted: [09/10/2026]
- 1,144 features, lines
- Many have no surface tag, so paved and unpaved cannot be separated everywhere
- Coverage looks good in the built-up area, sparse at the edges