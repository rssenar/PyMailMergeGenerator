'''
888b     d888          d8b 888 888b     d888                                     .d8888b.                                              888                     
8888b   d8888          Y8P 888 8888b   d8888                                    d88P  Y88b                                             888                     
88888b.d88888              888 88888b.d88888                                    888    888                                             888                     
888Y88888P888  8888b.  888 888 888Y88888P888  .d88b.  888d888  .d88b.   .d88b.  888         .d88b.  88888b.   .d88b.  888d888  8888b.  888888  .d88b.  888d888 
888 Y888P 888     "88b 888 888 888 Y888P 888 d8P  Y8b 888P"   d88P"88b d8P  Y8b 888  88888 d8P  Y8b 888 "88b d8P  Y8b 888P"       "88b 888    d88""88b 888P"   
888  Y8P  888 .d888888 888 888 888  Y8P  888 88888888 888     888  888 88888888 888    888 88888888 888  888 88888888 888     .d888888 888    888  888 888     
888   "   888 888  888 888 888 888   "   888 Y8b.     888     Y88b 888 Y8b.     Y88b  d88P Y8b.     888  888 Y8b.     888     888  888 Y88b.  Y88..88P 888     
888       888 "Y888888 888 888 888       888  "Y8888  888      "Y88888  "Y8888   "Y8888P88  "Y8888  888  888  "Y8888  888     "Y888888  "Y888  "Y88P"  888     
                                                                   888                                                                                         
                                                              Y8b d88P                                                                                         
                                                               "Y88P"                                                                                          
'''
#!/usr/bin/python3.4.3
# ---------------------------------------------
# Imports
# ---------------------------------------------
import csv
# ---------------------------------------------
# Global Variables
# ---------------------------------------------
CSVFilesHaveHeaderRow = True # True or False if input files include a header row
InputFile = "Inout.csv"
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
