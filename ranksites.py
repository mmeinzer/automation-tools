from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    with open("site_urls.txt") as f:
        urls = [line.strip() for line in f]
        print(urls)
    driver = webdriver.Chrome("/home/matt/Downloads/chromedriver")
    for url in urls:
        driver.get(url)
        rating = raw_input("Rate this site (1-3): ")
        print(rating)

if __name__ == '__main__':
    main()