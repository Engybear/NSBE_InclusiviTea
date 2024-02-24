import requests
from bs4 import BeautifulSoup as bs
import wget

query = "University of Toronto Bookstore College Street Location"
params = {
    "q": query,
    "tbm": "isch",
}

html = requests.get("https://www.google.com/search",params)
soup = bs(html.content,features="html.parser")

images = soup.select('div img')
images_url = images[0]['src']
# print(images_url)

outFileName = "outputImage.png"

# wget.download(images_url,outFileName)
check = wget.download(images_url,outFileName)
