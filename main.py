from __future__ import with_statement
import sched, time
from testInternet import main
import signal, time
from contextlib import contextmanager

class TimeoutException(Exception): pass
 
@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException, "Timed out!"
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
 
 
TIEMPO=60*10  #El test se realiza cada 10 minutos
TIME_OUT=60*5 #DEspues de 5 se termina.
s = sched.scheduler(time.time, time.sleep)
def print_time():
	try:
	    with time_limit(TIME_OUT):
		    s.enter(TIEMPO, 1, print_time, ())
		    try:
		        main()
		    except Exception, e:
		        raise e
	except TimeoutException, msg:
	    print msg
	

s.enter(0, 1, print_time, ())
s.run()


