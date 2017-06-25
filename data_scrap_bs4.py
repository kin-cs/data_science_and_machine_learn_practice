'''
Using Beautiful Soup and urllib to do information retrieval


tutorial by Data Science Dojo from https://www.youtube.com/watch?v=XQgXKtPSzUI

modified by Kin

'''


from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://shop.fender.com/en/intl/artist-gear/'

# opening up connection, grab the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grap each the guitar item
containers = page_soup.findAll('div', {'class': 'product-item'})


models = []
for container in containers:
	model = container.div.a['title']
	colors = container.findAll('div', {'class': 'product-item__swatches'})
	colors_out = ' '.join(colors[0].text.split())
	models.append((model, colors_out))

print(models)
