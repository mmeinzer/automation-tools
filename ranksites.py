from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    with open("site_urls.txt") as f:
        urls = [line.strip() for line in f]
    with open("site_ratings.txt", 'w') as w:
        driver = webdriver.Chrome("/home/matt/Downloads/chromedriver")
        for url in urls:
            driver.get(url)
            value = raw_input("Rate this site (1-3): ")
            if value in ["1", "2", "3"]:
                w.write(value + "\n")
            else:
                break

if __name__ == '__main__':
    main()