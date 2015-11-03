'''
Created on November 3 , 2015

@author: Sai Ram Nellutla
'''

class TxtToKml:

	#Constructor
	def __init__(self,f_,h_,color_,algoName_):
		self.f = f_
		self.h = h_
		self.color = color_
		self.algoName = algoName_

	# writes KML head
	def writeHead(self):
		self.h.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"+"\n"+"<kml xmlns=\"http://www.opengis.net/kml/2.2\">"+"\n"+"<Document>"+"\n     "+"	<name>"+self.algoName+"</name>"+"\n") 

	# writes placemark features for each cluster
	def writeClusterHead(self,clustCount):
    		self.h.write("	<Style id=\"icon_id"+str(clustCount)+"\">"+"\n"+"		<IconStyle>"+"\n"+"			<color>"+self.color[clustCount-1]+"</color>"+"\n"+"			<Icon>"+"\n"+"				<href>http://maps.google.com/mapfiles/kml/paddle/blu-blank.png</href>"+"\n"+"				<scale>1.0</scale>"+"\n"+"			</Icon>"+"\n"+"		</IconStyle>"+"\n"+"	</Style>"+"\n")

	# writes KML tail
	def writeTail(self):
		self.h.write("</Document>\n</kml>")	#kml tail


	# writes KML body
	def writeBody(self,lat,lon,clustCount):
        	self.h.write("	<Placemark>\n		<name>"+ str(lat)+","+str(lon)+" </name>\n		<description>"+ self.algoName +"</description>\n		<styleUrl>#icon_id"+str(clustCount)+"</styleUrl>\n		<Point>\n			<coordinates>"+str(lon)+","+str(lat)+",0"+"</coordinates>\n		</Point>\n	</Placemark>\n")
