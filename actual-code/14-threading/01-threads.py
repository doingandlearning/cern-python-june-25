from threading import Thread
import random
import time

list_readings = []

def worker(sensor_name):
    for _ in range(0,10):
        then = time.time_ns()
        time.sleep(1)
        reading = random.random() * 100
        print(f"Sensor reading[{sensor_name}: {reading} ({time.time_ns() - then}")
        list_readings.append((sensor_name, reading))


threads = [Thread(target=worker, args=(sensor,)) for sensor in range(0,10)]

for thread in threads:
    thread.start()

print([t.name for t in threads])

for thread in threads:
    thread.join()

print(list_readings)