from concurrent.futures import ProcessPoolExecutor
import time


def io_task(name):
    print(f"Start {name}")
    time.sleep(2)
    print(f"End {name}")


if __name__ == "__main__":
    start_time = time.time()

    with ProcessPoolExecutor() as executor:
        for i in range(5):
            executor.submit(io_task, f"Task-{i}")

    end_time = time.time()

    print("All tasks completed")
    print("Total time:", round(end_time - start_time, 2), "seconds")
