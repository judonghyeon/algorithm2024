import datetime

def printmyinfo():
    # 개인 정보
    name = "주동현"
    student_id = "202311442"
    subject = "알고리즘"
    
    # 현재 시간
    now = datetime.datetime.now()
    date_str = now.strftime("%Y년 %m월 %d일 %H시 %M분")
    
    # 정보 출력
    print("이름:", name)
    print("학번:", student_id)
    print("과목:", subject)
    print("오늘의 날짜는", date_str)

# 모듈 import 시 자동으로 함수 실행되지 않도록 보호
if __name__ == "__main__":
    printmyinfo()
