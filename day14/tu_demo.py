#!/usr/local/bin/python3
import requests
import re
from time import sleep

url = 'https://source.unsplash.com/random'


def pp():
    resp = requests.get(url)
    hz = re.split(r'=', re.split(r'\&', re.split(r'\?', resp.url)[1])[2])[1]
    filename = re.split(r'photo-', re.split(r'\?', resp.url)[0])[1]
    path = '/Users/aolei/Pictures/myimages/'+filename+'.'+hz
    with open(path, mode='wb') as f:
        f.write(resp.content)
    print(path)


if __name__ == "__main__":
    num = 10
    while num >= 0:
        pp()
        sleep(1)
        num -= 1
