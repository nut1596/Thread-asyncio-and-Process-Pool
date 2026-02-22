import threading
import time


def io_task(name):
    print(f"Start {name}")
    time.sleep(2)  # จำลองงาน I/O
    print(f"End {name}")


start_time = time.time()

threads = []

for i in range(5):
    t = threading.Thread(target=io_task, args=(f"Task-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = time.time()

print("All tasks completed")
print("Total time:", round(end_time - start_time, 2), "seconds")
