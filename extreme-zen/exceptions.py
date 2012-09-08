class PackageUpdaterException(Exception):
    def __init__(self, message, title=None):
        self.message=message
        self.title=title
        #log_message = "For {title}, {error_type}: {message}".format(
        #    title=
        #)
        #logging.error(log_message)
    


try:
    try:
        x = y
    except Exception as e:
        print(type(e))
        raise PackageUpdaterException(e)
except PackageUpdaterException as pue:
    pass


print pue
print pue.args
print pue.message
print type(pue.message)

