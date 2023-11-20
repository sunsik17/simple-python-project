import multiprocessing
import time


def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return


if __name__ == '__main__':

    startTime = time.time()
    start, end = 1, 50000000
    result = list()

    for i in range(2):
        work(1, start, end, result)
        print(f'{i + 1}번 째 실행')

    elapsed = round(time.time() - startTime, 2)
    print(elapsed, ' 초 경과')
    print(f'합계 결과 : {sum(result)}')

    startTime2 = time.time()
    result2 = list()
    start, end = 1, 50000000

    procs = []
    for i in range(2):
        p = multiprocessing.Process(target=work, args=(i, start, end, result2))
        p.start()
        procs.append(p)
        print(f'{i + 1}번 쨰 실행')

    for p in procs:
        p.join()

    t2_elapsed = round(time.time() - startTime2, 2)
    speed_up = round(elapsed / t2_elapsed, 1)
    print(t2_elapsed, ' 초 경과')
    print(speed_up, ' 배 향상')
    print(f'합계 결과 : {sum(result2)}')
