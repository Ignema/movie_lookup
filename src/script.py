# importing the requests library 
import sys
import requests 
from json import loads, dumps

# Get keyword from the shell 
keyword = sys.argv[1]

# api-endpoint 
URL = "https://sg.media-imdb.com/suggests/" + keyword[0] + "/"+ keyword + ".json"

# sending get request and saving the response as response object
try:
    r = requests.get(url = URL)    
except:
    print("Error fetching data...")
    exit(404) 

# extracting data in json format
try:
    content = r.content.decode().strip("imdb$"+ keyword +"(")
    content = content[:len(content)-1]
    json = loads(content)  
except:
    print("Couldn't parse JSON payload...")
    exit(0) 

# extracting movies 
movies = json['d']

# printing the output 
for movie in movies:
    print(movie["l"])