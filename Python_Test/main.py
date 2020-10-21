from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

options = Options()
# options.binary_location = "C:\\path\\to\\chrome.exe"
options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
d = DesiredCapabilities.CHROME

d['loggingPrefs'] = {'browser': 'ALL'}
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path="./chromedriver")


def youtube_check():
    driver.get("https://www.youtube.com/")
    time.sleep(5)
    browser = driver.find_element_by_xpath("//input[@id='search']").send_keys("Valorant")
    browser = driver.find_element_by_xpath("//button[@id='search-icon-legacy']/yt-icon[@class='style-scope ytd-searchbox']").click()
    time.sleep(10)
    # a = ["1", "3", "6"]
    # print(a[0])
    # print(a[0:-1])
    # print(a[-1])


if __name__ == '__main__':
    youtube_check()
