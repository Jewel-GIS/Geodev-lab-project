import rasterio

with rasterio.open(r"C:\Users\Jewel.Oluwole\dev\Geodev-lab-project\data\raw\dem.tif") as src:
    print("Width x height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src. bounds)
    print("Nodata:", src. nodata)
    print("Transform:")
    print(src.transform)