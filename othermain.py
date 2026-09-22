import time
import random
from _pyrepl.commands import end

best_time = None
for _ in range(5):
    time.sleep(random.randrange(2, 5))
    start_time = time.monotonic()
    input("GO!")
    end_time = time.monotonic()
    speed = end_time - start_time
    print(speed)
    if best_time is None:
        best_time = speed
    if speed < best_time:
        best_time = speed
print(f"Your fastest time was {best_time}")
