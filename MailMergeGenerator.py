'''
ooo        ooooo            o8o  oooo  ooo        ooooo                                           .oooooo.                                                           .                      
`88.       .888'            `"'  `888  `88.       .888'                                          d8P'  `Y8b                                                        .o8                      
 888b     d'888   .oooo.   oooo   888   888b     d'888   .ooooo.  oooo d8b  .oooooooo  .ooooo.  888            .ooooo.  ooo. .oo.    .ooooo.  oooo d8b  .oooo.   .o888oo  .ooooo.  oooo d8b 
 8 Y88. .P  888  `P  )88b  `888   888   8 Y88. .P  888  d88' `88b `888""8P 888' `88b  d88' `88b 888           d88' `88b `888P"Y88b  d88' `88b `888""8P `P  )88b    888   d88' `88b `888""8P 
 8  `888'   888   .oP"888   888   888   8  `888'   888  888ooo888  888     888   888  888ooo888 888     ooooo 888ooo888  888   888  888ooo888  888      .oP"888    888   888   888  888     
 8    Y     888  d8(  888   888   888   8    Y     888  888    .o  888     `88bod8P'  888    .o `88.    .88'  888    .o  888   888  888    .o  888     d8(  888    888 . 888   888  888     
o8o        o888o `Y888""8o o888o o888o o8o        o888o `Y8bod8P' d888b    `8oooooo.  `Y8bod8P'  `Y8bood8P'   `Y8bod8P' o888o o888o `Y8bod8P' d888b    `Y888""8o   "888" `Y8bod8P' d888b    
                                                                           d"     YD                                                                                                        
                                                                           "Y88888P'                                                                                                        
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
