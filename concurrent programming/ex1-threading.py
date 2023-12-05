import time
import threading

start = time.perf_counter()

# A function that just does something.
# in this example we are simply sleeping to emulate an easy but long workload
def do_something():
    print("We are doing something")
    time.sleep(1)
    print("We have done something")

# Lets create some threads and add them to a list.
threads = []
for _ in range(100):
    thread = threading.Thread(target=do_something)	# Create (but not start) the thread. Save the handle to the variable thread
    thread.start()									# Start the thread
    threads.append(thread)							# Append the handle to threads list so we can check on them later.

for thread in threads:								# Lets wait for all the threads to join with out thread again.
    thread.join()									# if we dont to this, this thread/application can terminate before the threads are finished.
                                                    # somethimes this is ok, but not always.
finish = time.perf_counter()
print("Finished in " + str(finish-start) + " seconds")