from bs4 import BeautifulSoup
import requests
import re





try:
	def compare(search_term, price):
			
		url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131"
		page = requests.get(url).text
		doc = BeautifulSoup(page, "html.parser")

		page_text = doc.find(class_="list-tool-pagination-text").strong
		pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

		items_found = {}

		for page in range(1, pages + 1):
			url = f"https://www.newegg.ca/p/pl?d={search_term}&N=4131&page={page}"
			page = requests.get(url).text
			doc = BeautifulSoup(page, "html.parser")

			div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")
			items = div.find_all(text=re.compile(search_term))

			for item in items:
				parent = item.parent
				if parent.name != "a":
					continue

				link = parent['href']
				next_parent = item.find_parent(class_="item-container")
				try:
					price = next_parent.find(class_="price-current").find("strong").string
					q = price.strip("$")
					d = q.replace(",", "")
					if d.replace("$", "") <= price:
							items_found[item] = {"price": int(d.replace("$", "")), "link": link}
					else:
						pass
						
					
					
				except:
					pass

		sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])

		for items in sorted_items:
			print(items[0])
			print(f"${items[1]['price']}")
			print(items[1]['link'])
			print("-------------------------------")
except requests.exceptions:
	pass



