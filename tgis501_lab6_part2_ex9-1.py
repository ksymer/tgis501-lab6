'''
Project: T GIS 501 a: Part 2, Challenge Exercise 9-1
Purpose: Map algebra suitability
Author:  Kris Symer
Date:    2014-11-06
Notes:   Moderate slope: between 5 and 20 degrees
         Southerly aspect: between 150 and 270 degrees
         Forested: land-cover types of 41, 42, or 43
         Map algebra syntax follows complex statement rules at
         http://resources.arcgis.com/en/help/main/10.2/index.html#//00p60000000p000000
'''

import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "X:/msgt/tgis501/lab_6/Exercise09"
env.overwriteOutput = True
if arcpy.CheckExtension("spatial") == "Available":
        arcpy.CheckOutExtension("spatial")
        elevraster = arcpy.Raster("elevation")

        #criteria 1: Moderate slope: between 5 and 20 degrees
        slope = arcpy.Slope("elevraster")
        modslope = (slope > 5) & (slope < 20)

        #criteria 2: Southerly aspect: between 150 and 270 degrees
        aspect = arcpy.Aspect("elevraster")
        southaspect = (aspect > 150) & (aspect < 270)

        #criteria 3: Forested: land-cover types of 41, 42, or 43
        cover = "landover.tif"
        forestcover = (cover == 41) | (cover == 42) | (cover == 43)

        #combine criteria
        bestland = (modslope & southaspect & forestcover)
        bestland.save("final")

        arcpy.CheckInExtension("spatial")
else:
        print "Spatial Analyst license is not available."
