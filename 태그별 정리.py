import csv

# CSV 파일 경로
csv_file = "문제데이터크롤링.csv"

problem = []
# CSV 파일 읽기
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        # 각 행의 데이터 처리
        for data in row:
            # 데이터 활용
            print(data)
                

# 출력:
# 데이터1
# 데이터2
# 데이터3
# ...
