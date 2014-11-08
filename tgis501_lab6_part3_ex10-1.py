'''
Project: T GIS 501 a: Part 3, Challenge Exercise 10-1
Purpose: Add layer to map document data frame
Author:  Kris Symer
Date:    2014-11-07
Notes:   
'''

try:
        import arcpy
        from arcpy import env
        env.workspace = "X:/msgt/tgis501/lab_6/Exercise10"
        env.overwriteOutput = True
        mxd = arcpy.mapping.MapDocument("C:/EsriPress/Python/Data/Exercise10/Austin_TX.mxd")
        df = arcpy.mapping.ListDataFrames(mxd, "Parks")[0]
        lyr = arcpy.mapping.ListLayers(mxd, "parks", df)[0]
        dflist = arcpy.mapping.ListDataFrames(mxd)
        for dframe in dflist:
                if dframe.name <> "Parks":
                        arcpy.mapping.AddLayer(dframe, lyr)
        mxd.save()
        del mxd

except arcpy.ExecuteError:
        print arcpy.GetMessages()
except:
        print "Something else failed"
        print arcpy.GetMessages()
finally:
        print "clean up"
