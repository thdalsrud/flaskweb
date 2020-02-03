import datetime

def datetime_decorate(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated

@datetime_decorate
def main_function_1():
    print('MAIN FUNCTION ** SATRT')

main_function_1()
