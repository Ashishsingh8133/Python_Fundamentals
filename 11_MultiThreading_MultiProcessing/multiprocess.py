import multiprocessing
import time

def square_number():
    for i in range(5):
        time.sleep(1) ##here the process p1 will sleep for 1 second and execute the square function for the next
        print(f"sqaure :{i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5) ##here process will sleep for 1.5 sec and after every 1.5 sec it will execute the next cube of the element
        print(f"cube :{i*i*i}")

if __name__=='__main__':
    

    ##create the multiple processes
    p1=multiprocessing.Process(target=square_number)
    p2=multiprocessing.Process(target=cube_number)

    ##start time
    t=time.time()

    ##start process
    p1.start()
    p2.start()

    ##after completing the process join it
    p1.join()
    p2.join()

    finish_time=time.time()-t
    print(finish_time)



