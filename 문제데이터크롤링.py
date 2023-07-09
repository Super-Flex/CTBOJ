from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

# Chrome 브라우저를 사용하여 Selenium WebDriver 생성
driver = webdriver.Chrome()

href_values = []
numbers = []
URL1 = "https://www.acmicpc.net/search#q=%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8&c=Workbooks"
URL2 = "https://www.acmicpc.net/search#q=%EC%BD%94%ED%85%8C&c=Workbooks"

for URL in [URL1, URL2]:
    # 첫 번째 페이지 접속
    driver.get(URL)
    time.sleep(2)

    # 각 페이지별 처리
    pagination = driver.find_element(By.CSS_SELECTOR, "#result-pagination")
    page_buttons = pagination.find_elements(
        By.CSS_SELECTOR, "li:not(:first-child):not(:last-child) a[data-page]"
    )
    total_pages = len(page_buttons)

    # 페이지 이동 및 데이터 수집
    for page in range(total_pages):
        # 다음 페이지로 이동
        driver.get(URL)
        page_buttons = driver.find_elements(
            By.CSS_SELECTOR, "li:not(:first-child):not(:last-child) a[data-page]"
        )
        page_buttons[page].click()
        time.sleep(2)

        # 현재 페이지의 HTML 가져오기
        html = driver.page_source

        # BeautifulSoup으로 HTML 파싱
        soup = BeautifulSoup(html, "html.parser")
        inner_results = soup.find_all(class_="inner-results")

        for inner_result in inner_results:
            href = inner_result.select_one("h3 a")["href"]
            href_values.append(href)

            # 세부 페이지에 접근
            driver.get(f"https://www.acmicpc.net{href}")
            time.sleep(2)

            # 세부 페이지의 HTML 가져오기
            detail_html = driver.page_source
            detail_soup = BeautifulSoup(detail_html, "html.parser")
            tr_elements = detail_soup.find_all("tr")

            for tr in tr_elements:
                first_td = tr.find("td")
                if first_td is not None:
                    number = first_td.get_text()
                    numbers.append(number)


# WebDriver 종료
driver.quit()

print(href_values)
print(numbers)

numbers_set = set(numbers)

# CSV 파일 경로
csv_file = "data/문제데이터크롤링.csv"

# CSV 파일에 데이터 저장
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["문제 번호"])
    writer.writerows([[number] for number in numbers_set])

print(f"{csv_file}에 데이터를 저장했습니다.")
