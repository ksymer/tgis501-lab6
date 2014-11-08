'''
Project: T GIS 501 a: Part 2, Challenge Exercise 9-2
Purpose: Copy workspace rasters to geodatabase
Author:  Kris Symer
Date:    2014-11-06
Notes:   
'''

try:
        import arcpy
        from arcpy import env
        outpath = "X:/msgt/tgis501/lab_6/Exercise09"
        env.workspace = outpath
        env.overwriteOutput = True
        geodb = "myGeodb.gdb"
        mydb = arcpy.CreatePersonalGDB_management(outpath, geodb)
        rasterlist = arcpy.ListRasters()
        print rasterlist
        
        for raster in rasterlist:
                desc = arcpy.Describe(raster)
                rastername = desc.baseName
                outraster = outpath + "/" + geodb + "/" + outraster
                arcpy.CopyRaster_management(raster, outraster)
                print str(raster)
except arcpy.ExecuteError:
        print arcpy.GetMessages()
except:
        print "Something else failed"
        print arcpy.GetMessages()
finally:
        print "clean up"
