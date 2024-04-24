import threading
import time

# Hàm chạy trên thread
def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(1)  # Giả lập việc thực hiện công việc mất thời gian

# Hàm chạy trên thread
def print_letters():
    for letter in 'ABCDE':
        print(f"Letter: {letter}")
        time.sleep(1)  # Giả lập việc thực hiện công việc mất thời gian

# Tạo các thread
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Khởi động các thread
thread1.start()
thread2.start()

# Chờ các thread kết thúc
thread1.join()
thread2.join()

print("All threads have finished execution")
