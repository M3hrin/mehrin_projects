import time
import random
for i in range(3):
    input("Press Enter to start the reaction time test...")
    time.sleep(random.uniform(1, 5))
    print("GO")
    start_time = time.time()
    input()
    end_time = time.time()
    reaction_time = end_time - start_time
    print(reaction_time)