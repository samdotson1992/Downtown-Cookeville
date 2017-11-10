# I hope to keep adding to this, but the basic idea is that it sends a request to the Google Places API using a query search to get the Google Place IDs then it sends another request using the place ID to get all the data. 

import requests
#More info at http://docs.python-requests.org/en/master/
import json
# More info at https://docs.python.org/2/library/json.html

#Make changes to these varialbes 
API_KEY=  # You can get an API key from https://developers.google.com/places/web-service/

output_file_name= "test" # add string 
# change the items in the list to suit your needs. 
location ="Cookeville+TN"
# City in which you want to make the search
lst=["Crawdaddys West Side Grill"]

output=[]    
def request_places(location,query):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+ location+ "+" +query +'&key='+API_KEY
    print(url)
    r=requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query="+ location+ "+" +query +'&key='+API_KEY)
    data=r.json() 
    results=data["results"]
    #print(results)
    try:
        for i in range(len(results)):
            full = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid="+results[i]["place_id"] +'&key=' +API_KEY)
            return full.json()
    except:
        print("He's dead Jim.")
        # This is for error handling, if something goes wrong you may have either exceeded the APIs daily limit or the place name is bad. 
for x in range(len(lst)):
    request=request_places(location,lst[x])
    print(request)
    result=request["result"]
    try:
        website= result["website"]
    except:
        website = "unknown"    
    #alter the place varible to control what is added to the data.     
    place=({"type":"Feature", "geometry": {"type": "Point", "coordinates":  [result["geometry"]["location"]["lng"],result["geometry"]["location"]["lat"]]}, "properties":{"name": result["name"],"rating": result["rating"], "website": website}})
    output.append(place)
with open(output_file_name+'.json', 'w') as outfile:
    json.dump(output, outfile)
        
