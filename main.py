# This is a sample Python script.
from elapsed import aop


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


@aop
def fun1(a, b, c):
    return a + b + c


@aop
def fun2(a, b, c):
    return a * b * c


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(fun1(1, 2, 3))
    print(fun2(1, 2, 3))
