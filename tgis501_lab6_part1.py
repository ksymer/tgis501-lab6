'''
Project: T GIS 501 a: Lab 6, Part I 
Purpose: Chapter 8 skills
Author:  Kris Symer
Date:    2014-11-04
Notes:   Uses turtles script from Lab 3, Problem 4
'''

#============================================
# Step 1: Draw polygon and record points
#============================================

#default variables
sides = -1 #default is a pentagon
min_sides = 3
max_sides = 100
degrees = 360.0 #CONSTANT: sum of all angles in a polygon


#helper functions 
#check for valid integer in range; does not yet handle non-integer values such as strings or decimals
def validNum(num, min_num, max_num):
	if num < min_num:
		print str(num) + ' is invalid.  A polygon must have at least ' + str(min_num) + ' sides. Try again.'
		return 0
	elif num > max_num:
		print str(num) + ' is greater than the maximum of ' + str(max_num) + '. Try again.'
		return 0
	else:
		return 1

#request user input
def getInput(minint,maxint):
	while 1:
		num = raw_input('Let\'s draw a polygon. How many sides?\nEnter an integer between 3 and 100: ')
		if validNum(int(num), minint, maxint):
			break
	print 'Nice choice. The turtle will now draw a ' + str(num) + '-sided polygon in a new window.'
	#print str(minint) + ', ' + str(maxint)
	return num

num = getInput(min_sides, max_sides);

#cast input return value as integer and continue with drawing
sides = int(num)

#calculate polygon geometry based on sides
length = 600.0 / sides #estimate optimal side length in pixels
angle = degrees / sides #construct equalateral polygon

#import library
import turtle

#create graphics window and override default attributes
wn = turtle.Screen()
wn.title('Fun with Turtle Graphics | Kris Symer')
wn.bgcolor('#ffefd5')

#create instance of turtle and override default attributes
shell = turtle.Turtle()
shell.hideturtle() #hide turtle until we draw the polygon
shell.pensize(3)
shell.color('#382465')
shell.shape('turtle')

#lift pen and move upward to write intro message
shell.penup()
shell.goto(0,220)
shell.setheading(0)
shell.pendown()
shell.write('This equilateral polygon has ' + str(sides) + ' sides:', False, align='left', font=('sans-serif', 16, 'bold'))

#move back to original point and 100px to right.
shell.color('blue')
shell.penup()
shell.goto(100,0)
shell.setheading(0)
shell.pendown()
shell.showturtle()

#create numbered list of turtle x,y coordinate pairs
#add origin point to list
print "origin = " + str(shell.position())
poly_coords = [[0, round(shell.xcor(), 4), round(shell.ycor(), 4)]]
#draw polygon sides counterclockwise (left turns) based on geometry
i = 1
while i <= sides:
	shell.forward(length)
	print shell.position() #print current position
	#append current position to list
	poly_coords.append([i, round(shell.xcor(), 4), round(shell.ycor(), 4)])
	shell.left(angle)
	i = i + 1

print poly_coords

#write message user about closing window
shell.penup()
shell.hideturtle()
shell.color('#666')
shell.goto(0,-40)
shell.setheading(0)
shell.pendown()
shell.write('Click anywhere in this window to exit.', False, align='left', font=('sans-serif', 16, 'bold'))
wn.exitonclick()



#============================================
# Part II: Create shapefile from points
#============================================

import arcpy
from arcpy import env

env.workspace = "X:/msgt/tgis501/lab_6/"
env.overwriteOutput = True
outpath = "X:/msgt/tgis501/lab_6/" #env.workspace
newfc = "turtle.shp"
prjfile = "4326.prj" #WGS 84 source: http://spatialreference.org/ref/epsg/4326/
spatialref = arcpy.SpatialReference(prjfile)

arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon", "", "DISABLED", "DISABLED", spatialref)
cursor = arcpy.da.InsertCursor(newfc,["SHAPE@"])
array = arcpy.Array()
point = arcpy.Point()
for i, x, y in poly_coords:
        point.ID, point.X, point.Y = i, x, y
        array.add(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
del cursor
