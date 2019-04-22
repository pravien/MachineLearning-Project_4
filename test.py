import os
import urllib.request as req
from urllib.parse import urlparse

url = 'https://raw.githubusercontent.com/pravien/MachineLearning-Project_4/master/rotten_tomatoes_reviews.csv'
filename = os.path.basename(urlparse(url).path)
path = os.path.join(".", filename)
req.urlretrieve(url, path)