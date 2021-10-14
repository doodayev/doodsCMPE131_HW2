import time

def calculate_time(func):
    def wrapper():
        before=time.time()
        func()
        print("Total time", time.time()-before)

    return wrapper

#@calculate_time
#def run():
#    time.sleep(2)

#run()
