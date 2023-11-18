import time


def aop(fun):
    def mapping(a, b, c):
        print('실행')
        start = time.time()
        result = fun(a, b, c)
        print('종료')
        end = time.time()
        print('메서드 실행 시간 : %f 초' % (end - start))
        return result
    return mapping
