import threading



counter = 0                     # Shared global variable
lock = threading.Lock()         # Lock object for this variable



def increment_counter():
    global counter
    for _ in range(100_000):
        with lock:              # The lock is automatically acquired and released
            counter += 1



# In CPython, the Global Interpreter Lock (GIL) ensures that only one thread
# executes Python bytecode at a time.

t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Final counter value: {counter}")
