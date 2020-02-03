import datetime

class DatetimeDecorator:
    def __init__(self, f):
        self.func=f
    
    def __call__(self, *args, **kwargs):
        print(datetime.datetime.now())
        self.func(*args, **kwargs)
        print(datetime.datetime.now())

class MainClass:
    @DatetimeDecorator
    def main_function_1():
        print('MAIN FUNCTION 1 SATRT')

    @DatetimeDecorator
    def main_function_2():
        print('MAIN FUNCTION 2 SATRT')

    @DatetimeDecorator
    def main_function_3():
        print('MAIN FUNCTION 3 SATRT')

my = MainClass()
my.main_function_1()
my.main_function_2()
my.main_function_3()