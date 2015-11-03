# Text-To-KML-Converter-For-Clustered-Location-Data
This file converts clustered location data containing latitudes and longitudes into Key Hole Markup language placemarks.Each location point is considered as a placemark and each cluster is given an unique color.

Programming Language Used: Python
Input:
The code assumes the input to be in the following manner:

"Name of the clustering algorithm input is formed from"_
Cluster Number 1_
latitude 1, longitude 1,..._
latitude 2, longitude 2,..._
'_
'_
'_
'_
'_
Cluster Number 2_
latitude 1, longitude 1,..._
latitude 2, longitude 2,..._

Output:

Output is a kml file obtained with the same name as input txt file. 
Replace txt with your file extension in "main.py" if you have a different extension.
Increase color codes in list color in "main.py" if you have more than 10 clusters.
KML takes hex color code format (OpacityRedGreenBlue).  
