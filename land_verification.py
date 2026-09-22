# Aramco Land Affairs - Spatial Conflict Identification
# Author: Tpl Lubabatu Musa

import arcpy

def check_spatial_conflict(proposed_site, existing_landuse, oil_gas_facilities):
    buffer_distance = "500 Meters"
    conflict_zone = arcpy.Buffer_analysis(proposed_site, "in_memory/buffer", buffer_distance)
    conflict_result = arcpy.Intersect_analysis([conflict_zone, existing_landuse, oil_gas_facilities], "in_memory/conflict_check")
    count = int(arcpy.GetCount_management(conflict_result)[0])
    if count > 0:
        print(f"CONFLICT FOUND: {count} conflicts")
        return False
    else:
        print("CLEARED: No conflict - site suitable")
        return True
