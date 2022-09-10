# This code is obsolete, our nemisis the LCBO has updated their website
# Needs a rewrite with Selenium (i think) because the website now infinate scrolls

import requests
from bs4 import BeautifulSoup
import time
import csv

# Also requires 'pip install lxml' installed

from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.progress import track
from rich.console import Console

console = Console()

department = "coolers-18-1"  # coolers-18-1 , wine-14
pageView = "grid"  # Default = grid
orderBy = "orderBy=5"  # 5 = Availability
pageNum = 1
pageMax = 18  # Manually grab this from the website
beginIndex = "beginIndex=" + str((pageNum * 12) - 12)  # pg# = (n*12)-12
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"  # Need to fake that we are a user and not a scraper

csvFile = "cooler.csv"

# Prepare the file to be written
print("Prepairing:", csvFile, end="")
with open(csvFile, "w", newline="") as file:
    # Save headers in our csv file
    writer = csv.writer(file)
    writer.writerow(
        [
            "Name",
            "Price",
            "Volume",
            "Alcohol %",
            "Location",
            "Made by",
            "Sugar content",
            "Sweetness discriptor",
            "Style",
            "Variety",
        ]
    )
    print("[green] ...Done![/green]")

# Main loop, itterate thru pages until page max
while pageNum <= pageMax:
    beginIndex = "beginIndex=" + str((pageNum * 12) - 12)  # pg# = (n*12)-12
    url = (
        "https://www.lcbo.com/webapp/wcs/stores/servlet/en/lcbo/"
        + department
        + "?"
        + pageView
        + "&"
        + orderBy
        + "&"
        + beginIndex
    )
    # Open page
    print("Opening:", url, "- pg:", pageNum, end="")
    page = requests.get(url, headers={"User-Agent": userAgent})
    print("[green] ...Done![/green]")

    soup = BeautifulSoup(page.content, "lxml")
    siteTitle = soup.find("title")
    print("Reading:", siteTitle.string, "- pg:", pageNum, end="")
    # tempString = "page " + str(pageNum) + " : " + siteTitle.string
    # titlePanel = Panel(url, title= Text(tempString, justify="center")) #
    # print(url)
    # This is where i would print my title if i could print my title
    for item in soup.select("ul.list_mode li"):
        print("[green] ...Found link![/green]")
        # Now we further dissect the <li> blocks that BS has found.
        #
        # there should only be one here but ".select" returns a list:
        infoList = []
        for li in item.select("div.productChart div a"):
            name = li.get_text()  # Get name
            infoList.append(name)
            for price in item.select("div.product_price"):
                price = price.get_text().strip()
                # print(price)
                fPrice = float(price[1:])  # Get price
                infoList.append(fPrice)
            newUrl = li.attrs["href"]  # Get new URL

            print("Opening:", newUrl, "- pg:", pageNum, end="")
            newPage = requests.get(newUrl, headers={"User-Agent": userAgent})
            newSoup = BeautifulSoup(newPage.content, "lxml")
            print("[green] ...Done![/green]\n", "Reading:", name, end="")
            for dl_tag in newSoup.select("dl"):
                # print(dl_tag.text)
                for info in dl_tag.select("dd"):
                    info = info.get_text()
                    info = info.strip()
                    # print(info)
                    infoList.append(info)
                break
            print(" - Length:", len(infoList), end="")
            if len(infoList) >= 3:
                tempString = infoList[2]
                print(" - Type:", type(tempString), end="")
                if type(tempString) is str:
                    tempString = tempString.replace("\xa0", " ")
                    tempString = tempString.replace("mL can", "")
                    tempString = tempString.replace("mL", "")
                    tempString = tempString.replace("x", "*")
                    tempString = tempString.replace("bottle", "")
                    tempString = tempString.replace(" ", "")
                    if "*" in tempString:
                        tempString = "= " + tempString

                # print("\n", tempString)
                infoList[2] = tempString

            print("[green] ...Found: [/green]", infoList, end="")

            # print(infoList) #Debug line
            print("Writing to:", csvFile, end="")
            with open(csvFile, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(infoList)
                # print("Data wrote!")
                print("[green] ...Done![/green]")
                file.close()
            # tempString = str(url) + str("   [green]Written ✓[/green]")
            # infoPanel = Panel(tempString, title= name)
            # print(infoPanel)
        print("Waiting", end="")
        time.sleep(1)
    pageNum = pageNum + 1

input("Press enter to quit")
