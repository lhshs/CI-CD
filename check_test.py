import psutil
import time
import subprocess
# import threading
# from timer import print_current_time

def check_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return True
    return False

def start_timer():
    timer_file_path = "timer.py"
    return subprocess.Popen(["python", timer_file_path])

def stop_process(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            proc.kill()

'''
def get_running_processes():
    running_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        running_processes.append(proc.info['name'])
    return running_processes
'''

if __name__ == "__main__":
    process_name_to_check = "CalculatorApp.exe"  # 확인하고 싶은 프로그램의 이름을 여기에 입력하세요
    interval = 1  # 확인 간격 (초)

    timer_process = None

    while True:
        '''
        running_processes = get_running_processes()
        print("실행 중인 프로세스들:")
        print(running_processes)
        print()
        '''

        if check_process(process_name_to_check):
            print(f"{process_name_to_check}이 실행 중입니다.")
            if timer_process is not None:
                timer_process.terminate()  # 현재 타이머 프로세스를 종료
            timer_process = start_timer()  # 새로운 타이머 프로세스를 시작
            stop_process(process_name_to_check)  # process_name_to_check 종료
            timer_process.terminate()  # 현재 타이머 프로세스 종료
            timer_process = start_timer()  # 새로운 타이머 프로세스 시작
        else:
            print(f"{process_name_to_check}이 실행되지 않았습니다.")
            if timer_process is None:
                timer_process = start_timer()  # 프로세스가 종료되었으므로 새로운 타이머 프로세스를 시작

        if check_process(process_name_to_check):
            print(f"{process_name_to_check}이 실행 중입니다.")
            stop_process(process_name_to_check)  # process_name_to_check 종료
            print('🍁 외부 프로그램 종료')
            timer_process.terminate()  # 현재 타이머 프로세스 종료
            print('▶️ 프로세스 종료')
            timer_process = start_timer()  # 새로운 타이머 프로세스 시작
            print('▶️ 프로세스 시작')
        else:
            print(f"{process_name_to_check}이 실행되지 않았습니다.")

        time.sleep(interval)
    
