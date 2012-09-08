def fib_spartan(n):
    if n < 2:
        return n
    return fib_spartan(n-1) + fib_spartan(n-2)
    
for i in xrange(10): fib_spartan(i)