from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_extension("mfcaadoifdifdnigjmfbekjbhehibfel.crx")  # 익스텐션의 경로를 지정합니다.
driver = webdriver.Chrome(options=options)


login_url = "https://www.acmicpc.net/login?next=%2F"  # 로그인 페이지 URL
driver.get(login_url)
time.sleep(2)
username_input = driver.find_element(
    By.NAME, "login_user_id"
)  # 아이디 입력란의 name 속성을 사용하여 요소 찾기
password_input = driver.find_element(
    By.NAME, "login_password"
)  # 비밀번호 입력란의 name 속성을 사용하여 요소 찾기
username_input.send_keys("acepark")  # 여기에 로그인에 사용할 아이디 입력
time.sleep(5)
password_input.send_keys("qew213")  # 여기에 로그인에 사용할 비밀번호 입력
time.sleep(5)
login_button = driver.find_element(By.ID, "submit_button")  # 로그인 버튼 요소를 id 속성을 사용하여 찾기
login_button.click()
# 로그인이 완료될 때까지 잠시 대기
time.sleep(5)


href_values = []
numbers = []
problem_id = 1005
# page = 1
URL = f"https://www.acmicpc.net/problem/status/{problem_id}/1"

print(URL)
driver.get(URL)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
inner_results = soup.find(class_="pagination")
last_li = inner_results.find_all("li")
last_a_href = last_li[-1].find("a")["href"]
pages = int(last_a_href.split("/")[-1])
print(pages)

tiers = [0] * 31
try_cnts = [0] * 31
for page in range(1, 1 + 1):
    URL = f"https://www.acmicpc.net/problem/status/{problem_id}/{page}"
    driver.get(URL)
    html = driver.page_source
    # with open("1005번 맞힌 사람 - 1 페이지.html", "r", encoding="utf-8") as file:
    #     html = file.read()

    soup = BeautifulSoup(html, "html.parser")
    tbody = soup.find_all("tbody")
    all_row = tbody[1].find_all("tr")
    for row in all_row[1:]:
        try:
            try_cnt = int(row.find_all("td")[2].text)
            tier = int(row.find_all("td")[3].img["src"].split("/")[-1][:-4])
            tiers[tier] += 1
            try_cnts[tier] += try_cnt
        except:
            continue
driver.quit()
print(tiers, try_cnts)

# CSV 파일 경로
csv_file = f"data/{problem_id}.csv"

# CSV 파일에 데이터 저장
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["티어", "사람수", "시도 횟수"])
    idx = 0
    for i in range(31):
        writer.writerow([idx, tiers[i], try_cnts[i]])
        idx += 1

print(f"{csv_file}에 데이터를 저장했습니다.")
