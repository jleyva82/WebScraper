from bs4 import BeautifulSoup
import requests

search = input("Enter search term:")                            #input
params = {"q": search}                                          #create parameters for search
r = requests.get("https://www.bing.com/search", params=params)   #pull request from bing search queary with concatenated search term

soup = BeautifulSoup(r.text, "html.parser")                      #parse through text with beatuiful soup library
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

        children = item.find("h2")                               #technique to parse sideways through text
        print("Next Sibiling of the h2:", children.next_sibiling)

        for child in children:                                  #technique to parse downwards through text
           print("Child:", child)

        print("Summary:", item.find("a").parent.parent.find("p").text) #technique to display summary
        print("\n")