import functools
import time

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


def hello_decorator(func): 
    def inner1(*args, **kwargs): 
          
        print("before Execution") 
          
        # getting the returned value 
        returned_value = func(*args, **kwargs) 
        print("after Execution") 
          
        # returning the value to the original frame 
        return returned_value 
          
    return inner1 

  
# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b): 
    print("Inside the function") 
    return a + b 
  
a, b = 1, 2

class A:
    def __init__(self,i):
        self.length = i
    def getLength(self):
        return self.length

a =  A(5)
print(a.getLength())
  
# getting the value through return of the function 
#print("Sum =", sum_two_numbers(a, b))

#waste_some_time(99)
