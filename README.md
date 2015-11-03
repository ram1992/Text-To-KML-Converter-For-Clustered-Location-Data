# Text-To-KML-Converter-For-Clustered-Location-Data
This script converts clustered location data containing latitudes and longitudes into Key Hole Markup language placemarks.Each location point is considered as a placemark and each cluster is given an unique color.

Programming Language Used: Python
Input:
The code assumes the input to be in the following manner:  

"Name of the clustering algorithm input is formed from"  
Cluster Number 1  
latitude 1, longitude 1,...  
latitude 2, longitude 2,...  
'  
'  
'  
'  
'  
Cluster Number 2  
latitude 1, longitude 1,...  
latitude 2, longitude 2,...  

Example:  
DB-Scan  
Cluster 1  
-30.3464513,-70.43454  
-30.4543543,-70.43535  
-30.3435343,-70.343513  
Cluster 2  
-30.4543,-70.43533  
-30.4543543,-70.43535  
-30.3435343,-70.343513  
Cluster 3  
-30.64354,-70.354  
-30.4543543,-70.43535  
-30.3435343,-70.343513  

Output:  
Output is a kml file obtained with the same name as input txt file. 
Replace txt with your file extension in "main.py" if you have a different extension.
Increase color codes in list color in "main.py" if you have more than 10 clusters.
KML takes hex color code format (OpacityRedGreenBlue).  
