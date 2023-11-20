import sched
import time

start = time.time()

def funA(a):
    print(round(time.time() - start), '초 경과')
    print(a)
def funB(b):
    print(round(time.time() - start), '초 경과')
    print(b)
def funC(c):
    print(round(time.time() - start), '초 경과')
    print(c)

schedule1 = sched.scheduler()
schedule1.enter(5, 1, funA, ('funA 실행',))
schedule1.enter(3, 1, funA, ('funB 실행',))
schedule1.enter(7, 1, funA, ('funC 실행',))
schedule1.run()