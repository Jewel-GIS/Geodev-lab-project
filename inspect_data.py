import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    
    values = []
    for row in rows:
        value = row[column].strip()
        if value == "":
            continue
        values.append(float(value))
    return{
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }

area_result = inspect_column("bashorun_settlements.csv", "Shape__Area")
building_count_result = inspect_column("bashorun_settlements.csv", "building_count")

print("Area:", area_result)
print("Building Count:", building_count_result)