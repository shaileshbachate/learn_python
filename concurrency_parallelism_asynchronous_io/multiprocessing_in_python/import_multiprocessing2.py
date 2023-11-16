import multiprocessing
import time


def fun1():
    print(f"hi from fun1")
    time.sleep(2)
    print("bye from fun1")


def fun2():
    print(f"hi from fun2")
    time.sleep(5)
    print("bye from fun2")


if __name__ == '__main__':
    start_time = time.perf_counter()
    fun1()
    fun2()
    end_time = time.perf_counter()
    print(f"Time required for running the functions synchronously: {(end_time - start_time):.2f} seconds")
    print('------------------------------------------------------------')

    start_time = time.perf_counter()
    p1 = multiprocessing.Process(target=fun1)
    p2 = multiprocessing.Process(target=fun2)
    p1.start()
    p2.start()
    end_time = time.perf_counter()
    print(f"This calculation will run before the subprocesses finish, so it will give wrong value for time \
    taken to run the functions: {(end_time - start_time):.2f} seconds")
    print('------------------------------------------------------------')

    p1.join() # Wait until child process terminates
    print(f"Process 1 has completed. Time passed: {round(time.perf_counter()-start_time, 2)}")
    p2.join()
    print(f"Process 2 has completed. Time passed: {round(time.perf_counter()-start_time, 2)}")
    end_time = time.perf_counter()
    print(f"Time required for running the functions using multiprocessing: {(end_time - start_time):.2f} seconds")
    print('------------------------------------------------------------')
