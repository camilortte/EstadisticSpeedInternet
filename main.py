import sched, time
from testInternet import main

TIEMPO=60*20
s = sched.scheduler(time.time, time.sleep)
def print_time():
    s.enter(TIEMPO, 1, print_time, ())
    try:
        main()
    except Exception, e:
        raise e

s.enter(0, 1, print_time, ())
s.run()