import rasterio

with rasterio.open("month-03/week-12/LC08_L2SP_191055_20250202_20250208_02_T1_SR_B3.TIF") as src:
    print("Width x height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src. bounds)
    print("Nodata:", src. nodata)
    print("Transform:")
    print(src.transform)