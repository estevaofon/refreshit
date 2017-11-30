from refreshit import uprint
from time import sleep

def example1():
    conversa = ["Beautiful is better than ugly.", "Explicit is better than implicit.",
                "Simple is better than complex."]
    for i in range(1):
        for fala in conversa:
            uprint(fala)
            sleep(0.5)
    print()

def example2():
    for i in range(101):
        uprint(str(i)+"%")
        sleep(0.05)
    print()

def example3():
    load = ["Loading...", "Loading..", "Loading.", "Loading"]
    load = load[::-1]
    for i in range(3):
        for item in load:
            uprint(item)
            sleep(0.2)
    uprint("Complete\n")

def example4():
    load = ["\\","|", "/", "-"]
    for i in range(3):
        for item in load:
            uprint(item)
            sleep(0.2)
    print()

def example5():
    n = 20
    squares = [u"\u25A0"*x+" "+"{:.0f}".format((x/(n-1))*100)+"%" for x in range(n)]
    for i in range(2):
        for item in squares:
            uprint(item)
            sleep(0.1)
    print()

example1()
example2()
example3()
example4()
example5()
