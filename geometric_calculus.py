# -*- coding: utf-8 -*-

"""
Second Individual Assignment RIccardo Serafini Data Structure Course """

Pi = 3.14

def calculate_volume_cylinder(radius_cylinder, height_cylinder):
    
    return float(radius_cylinder) * float(height_cylinder) * 2 * Pi 


def calculate_sphere_volume(radius_sphere):
    
    return (float(radius_sphere) * 4 * Pi) / 3


radius_cylinder = input("Insert the radius: ")
height_cylinder = input("Insert the height: ")
print(calculate_volume_cylinder(radius_cylinder, height_cylinder))

radius_sphere = input("Insert the radius: ")
print(calculate_sphere_volume(radius_sphere)) 



#%% Nmber 6

def multiplies():
    
    my_multiplies = []

    for i in range(0, 1001):
        if i % 3 == 0 and i % 5 == 0:
          my_multiplies.append(i)
            
    return my_multiplies
        
print(multiplies())  