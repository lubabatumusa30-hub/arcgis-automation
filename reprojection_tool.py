# Aramco G&SSD - Coordinate Reference System Reprojection Tool
# Author: Tpl Lubabatu Musa
# Purpose: Expert knowledge of CRS, accuracy & performance

import arcpy

def reproject_parcels(input_fc, target_crs="WGS 1984 UTM Zone 38N"):
    transformation = "Minna_To_WGS_1984_4"
    output_fc = "reprojected_parcels"
    arcpy.Project_management(input_fc, output_fc, target_crs, transformation)
    print(f"Reprojection complete: {output_fc}")
    return output_fc

if __name__ == "__main__":
    reproject_parcels("agis_parcels_raw")
