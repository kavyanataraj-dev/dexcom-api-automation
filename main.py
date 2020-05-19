import requests
from urllib.parse
import urlparse

def api_test()
 url = "https://api/subject/1594950620847472640/analysis_session"

 s = requests.Session()

 req = s.get(url)

 parsed = urlparse.urlparse(url)
 path = parsed[2]

 pathlist = path.split("/") #elements that comes after "https://api", here 's the elements of the list [' subject ', '1594950620847472640 ',
analysis_session '] '


assert pathlist[3] != NULL

