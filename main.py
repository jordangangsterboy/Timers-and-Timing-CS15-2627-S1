import time
import random

attempts = 5
best = None   # no reaction times recorded yet

for attempt in range(attempts):
    print(f"\nAttempt {attempt + 1}")
    print("Get ready...")

    # 1. Pick a random wait length between 2 and 5 seconds
    wait_length = random.uniform(2, 5)

    # 2. Non-blocking wait: loop until elapsed >= wait_length
    start_time = time.monotonic()
    while elapsed_time < wait_length:
        current_time = time.monotonic()
        elapsed_time = current_time - start_time

    # 3. Show the prompt and mark the moment it appeared
    print("GO!")
    go_time = time.monotonic()

    # 4. Wait for Enter, then mark the moment it was pressed
    input()
    press_time = time.monotonic()

    # 5. Calculate and display the reaction time
    reaction = press_time - go_time
    print(f"Reaction time: {reaction:.3f} seconds")

    # 6. Update `best` if this is the fastest so far
    #    (careful with the first attempt — best is None)

print(f"\nFastest reaction time: {best:.3f} seconds")

if best is None or reaction < best:
    best = reaction