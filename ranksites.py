from selenium import webdriver
from selenium.webdriver.common.keys import Keys

urls = ["http://www.python.org", "http://ajcpa.com/", "http://www.aemcpas.com/"]

def main():
    driver = webdriver.Chrome("/home/matt/Downloads/chromedriver")
    for url in urls:
        driver.get(url)
        rating = raw_input("Rate this site (1-3): ")
        print(rating)

if __name__ == '__main__':
    main()