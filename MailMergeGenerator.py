'''
   __  ___     _ ____  ___                 _____                     __          
  /  |/  ___ _(_/ /  |/  ___ _______ ____ / ______ ___ ___ _______ _/ /____  ____
 / /|_/ / _ `/ / / /|_/ / -_/ __/ _ `/ -_/ (_ / -_/ _ / -_/ __/ _ `/ __/ _ \/ __/
/_/  /_/\_,_/_/_/_/  /_/\__/_/  \_, /\__/\___/\__/_//_\__/_/  \_,_/\__/\___/_/   
                               /___/                                             
'''
#!/usr/bin/python3.4.3
# Imports
import csv
# ---------------------------------------------
# GLOBAL VARIABLES
# ---------------------------------------------
# Column[0] = City
# Column[1] = State
# Column[2] = Zip
# Column[3] = Crrt
# Column[4] = Route Count
# Column[5] = Bundle
# Column[6] = Bundle Per Route
# Column[7] = Last bundle
# Column[8] = SeqNum (Output Field, Set to 0)
# Column[9] = FinalBundles (Output Field, Set to 0)
# Column[10] = Count (Output Field, Set to 0)
# ---------------------------------------------
CSVFilesHaveHeaderRow = True # True or False if input files include a header row
InputFile = "/Users/rssenar/Desktop/" + input("Input File Name : ") + ".csv" 
OutputFile = "/Users/rssenar/Desktop/_MMOutput.csv" 
# ---------------------------------------------
RouteCount = 4 
Bundle = 5
BundlePerRoute = 6
LastBundle = 7 
SeqNum = 8 
UpdatedBundles = 9 
Count = 10 
HeaderRow = [\
	'City',\
	'State',\
	'Zip',\
	'Crrt',\
	'RouteCount',\
	'Bundle',\
	'BundlePerRoute',\
	'LastBundle',\
	'SeqNum',\
	'FinalBundles',\
	'Count',\
	]
# ---------------------------------------------
# OBJECTS
# ---------------------------------------------
Input = csv.reader(open(InputFile,'r'))
Output = csv.writer(open(OutputFile,'a'))
Output.writerow(HeaderRow)
# ---------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------
FirstLine = True
for line in Input:
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
			Output.writerow(line)
			counter+=1
