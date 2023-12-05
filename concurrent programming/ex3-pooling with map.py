import time
import concurrent.futures

start = time.perf_counter()

# A function that just does something.
# in this example we are simply sleeping to emulate an easy but long workload
# and this time we take arguments as well.
def do_something(thread_time):
    print(str(thread_time) + " are doing something")
    time.sleep(thread_time)
    return str(thread_time) + " has done something"

# This time we are using futures and threadpool for creting our threads.
# we are using map to map all the function calls.
secs = [5,4,3,2,1]
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(do_something, secs)

    for result in results:		# For each result do something.
        print(result)
    

finish = time.perf_counter()
print("Finished in " + str(finish-start) + " seconds")