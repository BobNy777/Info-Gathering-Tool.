 import sys
 import requests
 import socket 
 import json

 if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + <"url>")
    sys.exit(1)

req = requests.get("https://sys.argv[1]")
print("\n"+str(req.headers))


gethostby_ =socket.gethostbyname(sys.argv[1])
print("\nThe IP Address of " +sys.argv[1]+" is: "+gethostby_ + "\n")

#ipinfo.io

req_two = requests.get("https://ipinfo.io/" +gethostby_+"/json")

resp_ =json.loads(req_two.text)

print("location: " +resp_["loc"])
print("region: "+resp_["region"])
print("city: "+resp_["city"])
print("country: "+resp_["country"])