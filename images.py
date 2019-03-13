from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def StartSearch():
    search = input("Search for:")
    params = {"q": search}

    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)

    soup = BeautifulSoup(r.text, "html.parser")
    #links = soup.findAll("img")
    links = soup.findAll("a", {"class": "thumb"}) #This class call out works but doesn't get you the 'right' images

    for item in links:

        img_obj = requests.get(item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
        print("Getting", title, "\nFrom:", item.attrs["href"])
        '''
        img_obj = requests.get(item.attrs["src"])
        title = item.attrs["src"].split("/")[-1]
        print("Getting", title, "\nFrom:", item.attrs["src"])
        '''
        try:
            img = Image.open(BytesIO(img_obj.content))
            img.save("./" + dir_name + "/" + title, img.format)
        except:
            print("Could not save image!")

        print("\n")

    StartSearch()

StartSearch()