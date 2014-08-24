import authorization
import json
import requests
import search

from urls import *

def main():
	auth = authorization.authorize()
	response = requests.get(TIMELINE_URL, auth=auth)
	search_result = search.search('James', '*recent', 100, auth)
	print json.dumps(search_result.json(), indent=4)

if __name__ == "__main__":
	main()