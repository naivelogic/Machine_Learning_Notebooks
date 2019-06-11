"""
This is a set of helper scripts used to organize the EDA and modeling for the SBER Bank dataset
"""

"""
Some of the modeling is perfomred in SAS in which the naming convention proved to be either too long or had 
numerical charachters in which prompted exceptions when modeling in SAS. Therefore here are the new column names. 
"""
sas_col_rename = {
    'preschool_education_centers_raion':'prek_raison',
    'school_education_centers_top_20_raion': 'school_top20_raison',
    'raion_build_count_with_builddate_info': 'raison_build_count_info',
    'public_transport_station_min_walk':'public_transport_minwalk',
    '0_6_all':'under6_all',
    '0_6_male':'under6_m',
    '0_6_female':'under6_f',
    '7_14_all':'seven_14_all',
    '7_14_male':'seven_14_m',
    '7_14_female':'seven_14_f',
    '0_17_all':'under17_all',
    '0_17_male':"under17m",
    '0_17_female':'under17f',
    '16_29_all':'sixteen_29_all',
    '16_29_male':'sixteen_29m',
    '16_29_female':'six_29f',
    '0_13_all':'under13_all',
    '0_13_male':'under13_m',
    '0_13_female':"under13_f"
}

