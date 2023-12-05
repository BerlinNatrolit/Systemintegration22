import time
import concurrent.futures

start = time.perf_counter()

# A function that just does something.
# in this example we are simply sleeping to emulate an easy but long workload
# and this time we take arguments as well.
def do_something(thread_name, thread_time):
    print(str(thread_name) + " are doing something")
    time.sleep(thread_time)
    return str(thread_name) + " has done something"		# we are now returning results.

# This time we are using futures and threadpool for creting our threads.
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(do_something, "Thread " + str(i), i) for i in range(10)]		# and we create a range of threads uising list comprehension.
    
    for future in concurrent.futures.as_completed(futures):		# we are handling the result from each thread as they are completed.
       print(future.result())									# print the result from the future.

finish = time.perf_counter()
print("Finished in " + str(finish-start) + " seconds")