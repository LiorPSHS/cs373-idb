# coding=utf-8

from bs4 import BeautifulSoup
import requests
import re
import os
import http.cookiejar
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

try:
	import urllib.request as urllib2
except ImportError:
	import urllib2

def get_soup(url,header):
	return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def get_top_image(query):
	query = query.encode('UTF-8')
	query = urllib2.quote(query)
	url="https://www.google.com/search?q="+query+"&source=lnms&tbm=isch"

	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
	}
	soup = get_soup(url,header)

	top_image = []
	for a in soup.find_all("div",{"class":"rg_meta"}):
	    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
	    top_image.append(link)
	    break

	return top_image[0]
