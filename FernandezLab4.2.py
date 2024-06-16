##Robert Fernandez
##Complete
##This program will show the ocean level rising by 1.8 millimeters per year for 25 years.


##Variable list
sea_level_rise_per_year = 1.8 #millimeters

for year in range(1, 26):
    total_rise = sea_level_rise_per_year * year
    print(f"{year}: {total_rise:.2f}")
