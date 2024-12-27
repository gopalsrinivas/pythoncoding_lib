import os
import urllib.request as urllib2
import json

while True:
    ip = input("What is your target IP: ")
    url = "http://ip-api.com/json/" + ip

    try:
        # Open the URL and fetch the response
        response = urllib2.urlopen(url)

        # Read the response data
        data = response.read()

        # Parse the JSON data
        values = json.loads(data)

        # Print IP information
        print("IP: " + values["query"])
        print("City: " + values["city"])
        print("ISP: " + values["isp"])
        print("Country: " + values["country"])
        print("Region: " + values["region"])
        print("Timezone: " + values["timezone"])

    except Exception as e:
        print("Error fetching IP information: ", e)

    break
