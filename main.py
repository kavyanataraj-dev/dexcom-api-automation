import requests
from urllib.parse
import urlparse
import json

def test_post_headers_body_json():
    url = 'https://clarity.dexcom.com/'
    
    # Additional headers : username,password.
    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {'key1': 1, 'key2': 'value2'}
    
    # convert dict to json by json.dumps() for body data. 
    resp = requests.post(url, headers=headers, data=json.dumps(payload,indent=4))       
    
    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['url'] == url
    
    # print response full body as text
    print(resp.text)

def api_test():
  url = "https://api/subject/1594950620847472640/analysis_session"

  s = requests.Session()

  req = s.get(url)

  parsed = urlparse.urlparse(url)
  path = parsed[2]
 
 #elements that comes after "https://api", here 's the elements of the list [' subject ', '1594950620847472640 ',analysis_session '] '

  pathlist = path.split("/")
#Using Pytest to assert
  assert pathlist[3] != NULL


 
