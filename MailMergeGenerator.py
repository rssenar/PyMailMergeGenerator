#!/usr/bin/python3.4.3
# ---------------------------------------------
# Imports
# ---------------------------------------------
import csv
# ---------------------------------------------
# Global Variables
# ---------------------------------------------
CSVFilesHaveHeaderRow = True # True or False if input files include a header row
InputFile = "Dec 2015 for Richard.csv"
OutputFile = "_MMOutput.csv" 
RouteCount = 4 
Bundle = 5
BundlePerRoute = 6 
LastBundle = 7 
SeqNum = 8 
UpdatedBundles = 9 
Count = 10 
# ----------------------------------------------
# Objects
# ----------------------------------------------
old = csv.reader(open(InputFile,'r'))
new = csv.writer(open(OutputFile,'a'))
new.writerow(['City','State','Zip','Crrt','RouteCount','Bundle','BundlePerRoute','LastBundle','SeqNum','FinalBundles','Count'])
# ----------------------------------------------
# Main Program
# ----------------------------------------------
FirstLine = True
for line in old:
	if CSVFilesHaveHeaderRow and FirstLine:
		FirstLine = False
	else:
		counter = 1
		LBundle = int(line[Bundle])
		LLastBundle = int(line[LastBundle])
		LBundlePerRoute = int(line[BundlePerRoute])
		
		while counter <= LBundlePerRoute:
			line[SeqNum] = counter
			if counter < LBundlePerRoute:
				line[UpdatedBundles] = LBundle
				RTBundles = line[UpdatedBundles]	
			else:
				line[UpdatedBundles] = LLastBundle
			line[Count] = str(line[SeqNum]) + " of " + str(line[BundlePerRoute])
			new.writerow(line)
			counter+=1
