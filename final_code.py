from datetime import datetime

def write_to_file(filename, content):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + '\n')

def read_to_file(filename, name):## 이름이 있는지
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        if name in content:
            return True
        else:
            return False
        
## 회원 이름
## 김진 김성진 김수민 김경민 김남욱
def make_attend_file(name):
    with open(f"{name}_attendance.txt", 'a', encoding='utf-8') as file:
        file.write(f"{name}_attendance.txt"+ "\n")

def attendance_manager():
    make_attend_file("김진")
    make_attend_file("김성진")
    make_attend_file("김수민")
    make_attend_file("김경민")
    make_attend_file("김남욱")
        
# attendance_manager()

def calculate_work_hours(start_time, end_time):
    fmt = "%Y-%m-%d %H:%M:%S"
    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)
    work_hours = (end - start).total_seconds() / 3600
    work_minute = (end - start).total_seconds() / 60
    return work_hours

def calculate_work_minute(start_time, end_time):
    fmt = "%Y-%m-%d %H:%M:%S"
    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)
    work_minute = (end - start).total_seconds() / 60
    return work_minute

def main():
    start_time = None
 

    while True:

        print("기록을 시작하시겠습니까?(기록/종료)")## 
        des = input()
    
        # start_time = None ## 이 부분 고치기(이놈이 시작할때마다 None 값으로 바껴 문제 발생)
        if "기록" in des:
            print("근무자의 이름을 입력하세요 (종료하려면 '종료' 입력):")
            name = input()
            filename = f"{name}_attendance.txt"
            attend_date = datetime.now().strftime(" %Y-%m-%d") ## attend_date 초기화
    

        print("출/퇴근 여부를 말씀해주세요 (종료하려면 '종료' 입력):")
        task = input()

        if "종료" in task:
            print("작업을 종료합니다.") 
            break

        if "출근" in task:
            start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   ##Starttime
            # attend_date = datetime.now().strftime(" %Y-%m-%d")
            write_to_file(filename, f"{name}님 출근: {start_time}")
            
            
        elif "퇴근" in task:
            if read_to_file(filename, name):
                end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                write_to_file(filename, f"{name}님 퇴근: {end_time}")
                work_hours = calculate_work_hours(start_time, end_time)
                work_minute = calculate_work_minute(start_time, end_time)
                work_hours = round(work_hours, 1)
                work_minute = round(work_minute, 1)
                write_to_file(filename, attend_date)
                write_to_file(filename, f"{name}님의 근무 시간: {work_hours:.2f} 시간,{work_minute: 2f} 분")
                start_time = None
                break
            else:
                print("출근 기록이 없습니다.")  
                # break     
        else:
            print("프로그램을 종료합니다.")
            break


## 음성인식으로 실행을 시키면 main함수 실행되어지게
if __name__ == "__main__":
    main()
