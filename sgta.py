import threading
import time

# Shared resource
counter = 0

# Function that increments the counter
# Without a mutex, this causes a race condition
def increment_counter_without_mutex():
    global counter
    for _ in range(10):
        current_value = counter
        time.sleep(0.01)  # Simulate some processing time
        counter = current_value + 1
        print(f"Without Mutex: Counter = {counter}")

# Function that increments the counter with a mutex
def increment_counter_with_mutex(mutex):
    global counter
    for _ in range(10):
        with mutex:
            current_value = counter
            time.sleep(0.01)  # Simulate some processing time
            counter = current_value + 1
            print(f"With Mutex: Counter = {counter}")

# Main function to demonstrate the problem and solution
def main():
    global counter

    # Without Mutex
    print("Running without mutex:")
    counter = 0
    threads = [threading.Thread(target=increment_counter_without_mutex) for _ in range(2)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f"Final Counter without Mutex: {counter}\n")

    # With Mutex
    print("Running with mutex:")
    counter = 0
    mutex = threading.Lock()
    threads = [threading.Thread(target=increment_counter_with_mutex, args=(mutex,)) for _ in range(2)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f"Final Counter with Mutex: {counter}")

if __name__ == "__main__":
    main()
