import requests
from bs4 import BeautifulSoup


url  = "https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/wine-14"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36" # Need to fake that we are a user and not a scraper
page = requests.get(url, headers={'User-Agent':userAgent})
soup = BeautifulSoup(page.content, 'lxml')

for item in soup.select("ul.list_mode li"):
    # Now we further dissect the <li> blocks that BS has found.
    #
    # there should only be one here but ".select" returns a list:
    for li in item.select("div.productChart div a"):
        print(li.get_text())
    
    print(li.attrs['href'])

    

        
    for price in item.select("div.product_price"):
        price = price.get_text().strip()
        print(price)
        fPrice = float(price[1:])

    for volume in item.select("div.other_details"):
        string = volume.get_text()
        string = " ".join(string.split())
        numbers = ([int(s) for s in string.split() if s.isdigit()])
        volume = numbers[0]
        print(fPrice / volume * 1000 , "$ / L")
        print(string)

    print("-----")