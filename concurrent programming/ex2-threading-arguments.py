import time
import threading

start = time.perf_counter()

# A function that just does something.
# in this example we are simply sleeping to emulate an easy but long workload
# and this time we take arguments as well.
def do_something(thread_name):
    for i in range(10):
        print(thread_name + " is running loop: " + str(i))

# Lets create some threads and add them to a list.
threads = []
for i in range(100):
    thread_name = "Thread " + str(i)
    thread = threading.Thread(target=do_something, args=[thread_name])	# Create (but not start) the thread. Save the handle to the variable thread. Sending argument as well through a list to args
    thread.start()														# Start the thread
    threads.append(thread)												# Append the handle to threads list so we can check on them later.

for thread in threads:								# Lets wait for all the threads to join with out thread again.
    thread.join()									# if we dont to this, this thread/application can terminate before the threads are finished.
                                                    # somethimes this is ok, but not always.

finish = time.perf_counter()
print("Finished in " + str(finish-start) + " seconds")
