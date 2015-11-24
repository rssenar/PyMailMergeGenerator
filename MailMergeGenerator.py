'''
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 |M|a|i|l|M|e|r|g|e|G|e|n|e|r|a|t|o|r|
 +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
#!/usr/bin/python3.4.3
# Imports
import csv
# ---------------------------------------------
'''
 +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
 |G|l|o|b|a|l| |V|a|r|i|a|b|l|e|s|
 +-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+-+
'''
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
InputFile = "Input.csv"
OutputFile = "_MMOutput.csv" 
RouteCount = 4 
Bundle = 5
BundlePerRoute = 6
LastBundle = 7 
SeqNum = 8 
UpdatedBundles = 9 
Count = 10 
# ----------------------------------------------
''' 
 +-+-+-+-+-+-+-+
 |O|b|j|e|c|t|s|
 +-+-+-+-+-+-+-+ 
'''
old = csv.reader(open(InputFile,'r'))
new = csv.writer(open(OutputFile,'a'))
new.writerow(['City','State','Zip','Crrt','RouteCount','Bundle','BundlePerRoute',\
	'LastBundle','SeqNum','FinalBundles','Count'])
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

