'''
Created on November 3 , 2015

@author: Sai Ram Nellutla
'''
import random as rand
import os 
import csv
from txttokml import TxtToKml

#read the location from the csv input file, convert to KML and write to kml file

for filename in os.listdir('/Input'):
	f = open('/Input/'+str(filename),'r') 
	reader = csv.reader(f, delimiter=",") # read wile
	h = open('Output/'+str(filename).replace("txt","kml"),'w') 
	color = ["ffffff00","ff00ff00","ffffdddd","ff000033","ff0033ff","ffff00ff","ff6666ff","ff669966","ff00ffff","ff669999","ff003300","ff6699cc"] #Color codes for Placemarks
	flag = 0
	algoName = ""
	clustCount = 0
	for line in reader:
		if flag is 1:
			if len(line) is 2: 
				ttk.writeBody(line[0],line[1],clustCount)								
			else:
				clustCount += 1
				print "Processing Cluster:" + str(clustCount)
				ttk.writeClusterHead(clustCount)
		else:
			algoName=line[0]
			print algoName
			ttk = TxtToKml(f,h,color,algoName)
			ttk.writeHead()
			flag = 1
	print str(clustCount) + " Clusters found"
	ttk.writeTail()

