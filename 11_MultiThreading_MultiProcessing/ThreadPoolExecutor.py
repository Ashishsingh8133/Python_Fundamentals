from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers=[1,2,3,4,5,45,33,4,3,2,1,4,5,7,8]

with ThreadPoolExecutor (max_workers=3) as executor: ##here we create 3 threads by using threadpool executor
    ## and these 3 threads parallely execute the same function print_number and will apply the map funcition
    ##over the given list numbers
    results=executor.map(print_number,numbers)

for result in results:
    print(result)