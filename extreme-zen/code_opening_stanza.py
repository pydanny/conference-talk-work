"""
    1. Contention: When working on sophisticated issues we want to remove mental overhead 
    2. We want to know the components at work

"""

import functools
import timeit

def show_functool_partial():
    def myfunc(a, b):
        print(locals())
        return a, b

    # create a partial
    p1 = functools.partial(myfunc, b=4)

    print p1(1)

    print(p1.func)
    print(p1.args)
    print(p1.keywords)
    print(myfunc(a=1,b=1))
    
def spartan_programming():
    
    def test_wikipedia():
        s = """\
        def fib_wikipedia(n):
            if n < 2:
                return n
            else:
                return fib_wikipedia(n-1) + fib_wikipedia(n-2)
        for i in range(10): fib_wikipedia(i)
        """
        t = timeit.Timer(stmt=s)
        print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000)

    def test_spartan():
        s = """\
        def fib_spartan(n):
            if n < 2:
                return n
            return fib_spartan(n-1) + fib_spartan(n-2)
        for i in range(10): fib_spartan(i)
        """
        t = timeit.Timer(stmt=s)
        print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000)

    test_wikipedia()
    test_spartan()

    def test_deep_nesting(name):
        for letter in name:
            try:
                int()
        
        

if __name__ == "__main__":
    show_functool_partial()
    spartan_programming()