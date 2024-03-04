import time

def print_current_time():
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("현재 시간:", current_time)
        time.sleep(1)

if __name__ == "__main__":
    print_current_time()
