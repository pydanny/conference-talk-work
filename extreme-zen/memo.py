def memoize(func):
    cache = {}
    #print(cache)

    def memoized(*args):
        print(cache)
        try:
            # Get the cached result
            return cache[args]
        except KeyError:
            # nothing in the cache, so we set it now
            result = cache[args] = func(*args)
            return result

    return memoized
    
@memoize
def allcaps(string):
    return string.upper()

allcaps = memoize(allcaps)
    
#print allcaps('PyCon')
#print allcaps('PyCon')


def memoize2(func):
    cache = {}

    def memoized(*args):
        if args in cache:
            return cache[args]
        result = cache[args] = func(*args)
        return result

    return memoized

allcaps = memoize2(allcaps)

#print allcaps('PyCon')
#print allcaps('PyCon')


def multiplier(multiple):
    def decorator(function):
        def wrapper(*args, **kwargs):           
            return function(*args, **kwargs) * multiple
        return wrapper
    return decorator


@multiplier(5)
def echo(foo):
    return foo

# usage
print echo('Hello, World')
'12345'


def authorization(roles):
    def decorator(function):
        def wrapper(*args, **kwargs):
            rights = args[0].get('rights', ())
            for right in rights:
                if right in roles:
                    return function(*args, **kwargs)
            raise Exception("You don't have the right!")
        return wrapper
    return decorator
    
@authorization('admin')
def do_admin_thing(user):
    # do something administrative
    return user

admin_user = {'name':'Admin', 'rights':['admin',]}    
print(do_admin_thing(admin_user))
user = {'name':'User'}
print(do_admin_thing(user))