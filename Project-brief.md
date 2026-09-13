# Project brief

## Research Question

Which populated areas of Bashorun Ward, Ibadan North LGA, Oyo State, are poorly served by both transportation infrastructure and health facilities?

## Study Area

Bashorun Ward, Ibadan North Local Government Area (LGA), Oyo State, Nigeria.

## Aim

To assess and map the spatial accessibility of transportation infrastructure and health facilities in Bashorun Ward by integrating settlement locations, population estimates, road proximity, and proximity to health facilities using GIS.

## Objectives

1. Map populated settlements within Bashorun Ward.
2. Estimate the population associated with each populated settlement using gridded population data.
3. Calculate the proximity of populated settlements to transportation infrastructure (roads).
4. Calculate the proximity of populated settlements to health facilities.
5. Combine transportation and health-facility accessibility measures to identify underserved populated areas.
6. Identify and map areas with the greatest combined service-access gaps and population exposure.

## Problem Statement

Access to transportation infrastructure and health facilities is an important factor in the ability of communities to reach essential services. Within urban areas, some populated settlements may be located farther from major roads and health facilities than others. Identifying these areas can help reveal spatial inequalities in access and support the prioritisation of locations for further planning and service provision.

This project analyses Bashorun Ward in Ibadan North LGA, Oyo State, to identify populated areas that are poorly served by both transportation infrastructure and health facilities. The analysis focuses on physical proximity rather than travel time because a travel-time friction dataset is not being used.

## Method

The analysis will use GIS to:

1. Identify populated settlements within Bashorun Ward.
2. Overlay the settlements with a 100 m gridded population raster and calculate the estimated population for each settlement.
3. Calculate the distance from each populated settlement to the nearest road/transportation infrastructure.
4. Calculate the distance from each populated settlement to the nearest health facility.
5. Standardise the transport and health accessibility measures so that areas with poorer access receive higher gap scores.
6. Combine the two accessibility measures to produce a combined service-access gap.
7. Use population exposure alongside the service-access gap to identify populated areas that should receive the highest priority for further investigation.

## Datasets

| Dataset | Variable / Use | Source |
|---|---|---|
| GRID3 Settlements | Populated settlement areas | [GRID3 Nigeria](https://data.grid3.org) |
| WorldPop / GRID3 Population | Estimated population per 100 m grid cell | WorldPop Data Catalogue — [WorldPOP](https://hub.worldpop.org/geodata) |
| Roads / Highways | Transportation infrastructure and distance to nearest road | OpenStreetMap |
| Health Facilities | Location of health facilities and distance to nearest facility | [GRID3 Nigeria](https://data.grid3.org) |
| Ward Boundary | Administrative reference | [GRID3](https://data.grid3.org) |
| LGA Boundary | Administrative reference | [GRID3](https://data.grid3.org) |
| State Boundary | Administrative reference | [GRID3](https://data.grid3.org) |

## What I would build

A GIS map that identifies populated areas in Bashorun Ward that are poorly served by both transportation infrastructure and health facilities. The map will highlight priority areas based on population and proximity to roads and health facilities, helping users quickly identify communities with the greatest service-access gaps.

## Important Methodological Note

This project measures **physical proximity/accessibility based on distance**. It does not estimate actual travel time, road congestion, road quality, or network travel conditions because a travel-time friction surface is not included in the analysis.
