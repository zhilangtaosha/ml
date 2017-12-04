def test(func):
    def new_func(*args, **kwargs):
        print("start")
        print(func.__name__)
        print(args)
        print(kwargs)
        result = func(*args, **kwargs)
        print("end")
        return result
    return new_func

@test
def add_ints(a,b):
    print(a + b)

add_ints(1,2)
