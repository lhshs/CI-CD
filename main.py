import subprocess

if __name__ == "__main__":
    # 실행할 다른 Python 파일의 경로 설정
    other_python_file_path = "timer.py"
    
    # subprocess를 사용하여 다른 Python 파일 실행
    subprocess.run(["python", other_python_file_path])
