import urlparse

import requests
from requests_oauthlib import OAuth1

from secret import CLIENT_KEY, CLIENT_SECRET
from urls import *

import json

def search(query, result_type, count):
	"""Performs a twitter search for a user"""
