import multiprocessing
import random, time


def funcToRunInProcess(x):
    print(f"(1) Hello from subprocess {x}!")
    sec = random.randint(1, 5)
    print(f"(2) Process {x} sleeping for {sec} seconds")
    time.sleep(sec)
    print(f"(3) Goodbye from subprocess {x}!")


if __name__ == "__main__":
    start_time = time.perf_counter()
    processes = []
    for i in range(5):
        my_process = multiprocessing.Process(target=funcToRunInProcess, args=(i+1,))
        my_process.start()
        processes.append(my_process)

    for process in processes:
        process.join()
    end_time = time.perf_counter()
    print(f"Finished in: {end_time - start_time} seconds")

