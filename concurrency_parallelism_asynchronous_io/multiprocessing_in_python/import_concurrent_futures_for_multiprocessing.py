import concurrent.futures
import time


start_time = time.perf_counter()


def fun(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return f"Done sleeping for {seconds} seconds..."


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        f1 = executor.submit(fun, 1) # submit method submits a callable to be executed with the given arguments and returns a future
        print(f1.result()) # Returns the result of the call that the future represents
        print('------------------------------------------------------------')


    with concurrent.futures.ProcessPoolExecutor() as executor:
        # secs = [2, 3, 1, 5, 4]
        secs = [3, 2, 5]

        # 1 # Results are returned in the order they are completed
        future_objects = [executor.submit(fun, sec) for sec in secs]
        for future_obj in concurrent.futures.as_completed(future_objects):
            print(future_obj.result())
        print(f"Time passed: {round(time.perf_counter()-start_time, 2)}")
        print('------------------------------------------------------------')

        # 2 # Processs may be completed in any order but the results are returned in the same order as they are started
        future_objects = [executor.submit(fun, sec) for sec in secs]
        for future_obj in future_objects:
            print(future_obj.result())
        print(f"Time passed: {round(time.perf_counter()-start_time, 2)}")
        print('------------------------------------------------------------')

        # 3 # acts similar to #2 # Processs may be completed in any order but the results are returned in the same order as they are started
        results = executor.map(fun, secs)
        for result in results:
            print(result)
        print(f"Time passed: {round(time.perf_counter()-start_time, 2)}")
        print('------------------------------------------------------------')


    end_time = time.perf_counter()
    print(f"Finished: {round(end_time-start_time, 2)}")