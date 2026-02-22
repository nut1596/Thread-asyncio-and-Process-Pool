import asyncio
import time


async def io_task(name):
    print(f"Start {name}")
    await asyncio.sleep(2)
    print(f"End {name}")


async def main():
    tasks = []
    for i in range(5):
        tasks.append(io_task(f"Task-{i}"))
    await asyncio.gather(*tasks)


start_time = time.time()

asyncio.run(main())

end_time = time.time()

print("All tasks completed")
print("Total time:", round(end_time - start_time, 2), "seconds")
