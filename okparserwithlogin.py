from selenium import webdriver
from bs4 import BeautifulSoup
import pickle
from selenium.webdriver.common.by import By
import urllib.request
from progress.bar import Bar
import time

browser = webdriver.Firefox()

def login():
    browser.get("http://ok.ru")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get('Тут введи ссылку на альбом')

def ScrollToDown():
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
                lastCount = lenOfPage
                time.sleep(1)
                lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                    match=True

def main():
    login()
    ScrollToDown()
    bar = Bar('Сбор фотографий', fill='#', suffix='%(percent)d%%')
    counter = 0
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    links = soup.find_all(class_='photo-card_cnt')
    for link in links:
        browser.get('https://ok.ru' + link['href'])
        counter = counter + 1
        urllib.request.urlretrieve(browser.find_element(by=By.TAG_NAME, value='img').get_attribute('src'), f"{counter}.png")
        bar.next(100/len(links))
        
if __name__ == '__main__':
    main()
