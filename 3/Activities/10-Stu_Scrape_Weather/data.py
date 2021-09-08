  # Set up Splinter
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com
url = "https://visitcostarica.herokuapp.com/"
browser.visit(url)

time.sleep(1)

    # Scrape page into Soup
html = browser.html
soup = bs(html, "html.parser")

    # Get the average temps
    # @TODO: YOUR CODE HERE!
temps=soup.find_all('strong')


    # Get the min avg temp
    # @TODO: YOUR CODE HERE!
min_temp=temps[1].text
    # Get the max avg temp
    # @TODO: YOUR CODE HERE!
max_temp=temps[2].text
    # BONUS: Find the src for the sloth image
    # @TODO: YOUR CODE HERE!
sloth_img=soup.find_all("img", class_="animals")[1]
    # Store data in a dictionary
costa_data = {
        "sloth_img": sloth_img,
        "min_temp": min_temp,
        "max_temp": max_temp
}

    # Quite the browser after scraping
browser.quit()