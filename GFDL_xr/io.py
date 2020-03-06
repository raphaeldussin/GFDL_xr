import xarray as _xr
import subprocess as _sp

def dmget_this(files):
    check = _sp.check_call(f'dmget {files}', shell=True)
    if check != 0:
        print(return_code)
    return None


def open_dataset(filename_or_obj, **kwargs):
    dmget_this(filename_or_obj)
    return _xr.open_dataset(filename_or_obj, **kwargs)


def open_mfdataset(paths, **kwargs):
    dmget_this(paths)
    return _xr.open_mfdataset(paths, **kwargs)


def load_dataset(filename_or_obj, **kwargs):
    dmget_this(filename_or_obj)
    return _xr.load_dataset(filename_or_obj, **kwargs)


def open_rasterio(filename, **kwargs):
    dmget_this(filename)
    return _xr.open_rasterio(filename, **kwargs)


def open_zarr(store, **kwargs):
    dmget_this(store)
    return _xr.open_zarr(filename, **kwargs)


open_dataset.__doc__ = _xr.open_dataset.__doc__
open_mfdataset.__doc__ = _xr.open_mfdataset.__doc__
load_dataset.__doc__ = _xr.load_dataset.__doc__
open_rasterio.__doc__ = _xr.open_rasterio.__doc__
open_zarr.__doc__ = _xr.open_zarr.__doc__
