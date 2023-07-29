from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import csv

# Chrome 브라우저를 사용하여 Selenium WebDriver 생성
# driver = webdriver.Chrome()

href_values = []
numbers = []
URL = "https://www.acmicpc.net/ranklist/"

# 첫 번째 페이지 접속
driver = webdriver.Chrome()
user_handle = []
for i in range(1, 1 + 1000):
    url = URL + str(i)
    driver.get(url)
    print(URL + str(i))
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    tbody = soup.find("tbody")
    tr_tags = tbody.find_all("tr")
    second_td_tags = [tr.find_all("td")[1] for tr in tr_tags]

    # Extract the href attribute of the <a> tag within each second <td> tag
    user_hrefs = [
        "".join(td.find("a")["href"][6:]) for td in second_td_tags if td.find("a")
    ]
    user_handle += user_hrefs
# CSV 파일 경로
csv_file = "유저핸들.csv"

# CSV 파일에 데이터 저장
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["유저 핸들"])
    for handle in user_handle:
        file.write(handle + "\n")

print(f"{csv_file}에 데이터를 저장했습니다.")
