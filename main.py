import time
start_time = time.time()
def countdown(i):
    while i:
        mins, secs = divmod(i, 60)
        timer = '{:02d}:{:02d}'.format( mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        print(timer)
        i -= 1
    print('Finish')
timing = input("Start Time : ")
countdown(int(timing))