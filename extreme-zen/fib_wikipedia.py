def fib_wikipedia(n):
    if n < 2:
        return n
    else:
        return fib_wikipedia(n-1) + fib_wikipedia(n-2)
        
for i in xrange(10): fib_wikipedia(i)