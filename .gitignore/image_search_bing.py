# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 07:44:04 2018

@author: Ian
"""

from requests import exceptions
import argparse
import requests
import cv2
import os

#Key 1: 58a85a95853b41198628e634839b9e36
#Key 2: b56cb6b95d5b4e6f8a8026efae911636

ap = argparse.ArgumentParser()
ap.add_argument ("-q","--query", required=True,
                 help="search query to search Bing Image API for") 
ap.add_argument ("-o","--output", required=True,
                 help="path to output directory of images")
args= vars(ap.parse_args())

#set Microsoft Cognitive Services API key along with
#(1) the maximum number of results for a given search 
#(2) the group size for results (maximum of 50 per request)

API_KEY = "58a85a95853b41198628e634839b9e36"
MAX_RESULTS = 250
GROUP_SIZE = 50

# set the endpoint API URL
URL = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

EXCEPTIONS = set([IOError, FileNotFoundError,
                  exceptions.RequestException, exceptions.HTTPError,
                  exceptions.ConnectionError, exceptions.Timeout])

# store the search term in a convenience variable then set the
# headers and search parameters
term = args["query"]
headers = {"Ocp-Apim-Subscription-Key" : API_KEY}
params = {"q": term, "offset": 0, "count": GROUP_SIZE}

# make the search
print("searching Bing API for '{}'".format(term))
search = requests.get(URL, headers=headers, params=params)
search.raise_for_status()

# grab the results from the search, including the total number of
# estimated results returned by the Bing API
results = search.json()
estNumResults = min(results["totalEstimatedMatches"], MAX_RESULTS)
print("{} total results for '{}'".format(estNumResults,term))

# initialize the total number of images downloaded thus far
total = 0

# loop over the estimated number of results in `GROUP_SIZE` groups
for offset in range(0, estNumResults, GROUP_SIZE):
    # update the search parameters using the current offset, the
    # make the request to fetch the results
    print("making request for group {}-{} of {}...".format(
            offset, offset + GROUP_SIZE, estNumResults))
    params["offset"] = offset
    search = requests.get(URL, headers=headers, params=params)
    search.raise_for_status()
    results = search.json()
    print("saving images for group {}-{} of {}...".format(offset, offset + GROUP_SIZE, estNumResults))
    

# loop over the results
for v in results["value"]:
    # try to download the image
    try:
        # make a request to download the image
        print("fetching: {}".format(v["contentUrl"]))
        r= requests.get(v["contentUrl"], timeout=30)
         
        # build the path to the output image
        ext = v["contentUrl"][v["contentUrl"].rfind("."):]
        p = os.path.sep.join([args["output"], "{}{}".format(str(total).zfill(8), ext)])
         
        # write the image to disk
        f = open(p, "wb")
        f.write(r.content)
        f.close()
        
    # catch any errors that would not unable us to download the image
    except Exception as e:
        # check to see if our exception is in our list of
        # exceptions to check for
        if type(e) in EXCEPTIONS:
            print("skipping: {}".format(v["contentUrl"]))
            continue
    
    # try to load the image from disk
    image = cv2.imread(p)
    
    # if the image is `None` then we could not properly load the image from disk (so it should be ignored)
    if image is None:
        print("deleting: {}".format(p))
        os.remove(p)
        continue
    
    # update the counter
    total += 1
    