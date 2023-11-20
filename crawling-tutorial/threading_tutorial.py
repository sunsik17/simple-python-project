from threading import Thread
import time

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)

startTime = time.time()
start, end = 1, 50000000
result = list()
th1 = Thread(target=work, args=(1, start, end, result))

th1.start()
th1.join()

th1_elapsed = round(time.time() - startTime, 2)
print(f'{th1_elapsed} 초 경과')
print(f'합계 결과 : {sum(result)}')


result = list()
startTime = time.time()
th2 = Thread(target=work, args=(2, start, end, result))

th2.start()
th2.join()

th2_elapsed = round(time.time() - startTime, 2)
speedUp = round(th1_elapsed / th2_elapsed)
print(f'{th2_elapsed} 초 경과')
print(f'기능 {speedUp} 배 향상')
print(f'합계 결과 : {sum(result)}')