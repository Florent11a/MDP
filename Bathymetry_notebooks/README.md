# Bathymetry port of Sisal (24 Sep and 16 Oct 2026)

`bathymetry_1.0.ipynb` processes the two bathymetry surveys of the port of Sisal, corrects them for the tide (depth below MSL 2026), and makes the maps and the difference between the two surveys.

Run the notebook from this folder. All paths are relative, so no settings need to be changed.

## Folder structure

```
Bathymetry_notebooks/
├── bathymetry_1.0.ipynb        processing notebook
├── data/                       input data (not changed by the notebook)
│   ├── survey_24sep2026/
│   │   ├── DSO/                Odom Echotrac MKIII recordings (.dso)
│   │   └── Bati240926.xlsx     GPS track of the survey
│   ├── survey_16oct2026/       Hypack edited soundings (.EDT) + log
│   ├── tide/
│   │   ├── 260626-260930.csv       Sisal tide gauge, 15 min, used for 24 Sep
│   │   ├── 20261016al18_sisal.txt  Sisal tide gauge, 1 min, used for 16 Oct
│   │   └── Marea260924Ok.xlsx      tide for 24 Sep (older version, not used)
│   └── drone/
│       └── drone_background_32615_0.1m.npz   drone photo of 7 Oct 2026, resampled to 0.1 m
└── output/                     made by the notebook
    ├── Bathymetry_Port_Sisal_24sep2026.csv
    ├── Bathymetry_Port_Sisal_16oct2026.csv
    ├── bathymetry_difference_16oct_minus_24sep.csv
    └── figures/                maps, comparison and difference plots
```

## Notes

- The original drone mosaic (`20261007_Canal_transparent_mosaic_group1.tif`, ~700 MB) is too big for GitHub. The notebook uses the resampled copy in `data/drone/`. To rebuild it, or to export the drone photo in full resolution, set `DRONE_TIF` in the settings cell to the path of the tif.
- The satellite background is downloaded with `contextily`, so it needs an internet connection. Without it the maps are made without the satellite image.
- Python packages: numpy, pandas, matplotlib, openpyxl, contextily, rasterio (only needed when `DRONE_TIF` is set).
