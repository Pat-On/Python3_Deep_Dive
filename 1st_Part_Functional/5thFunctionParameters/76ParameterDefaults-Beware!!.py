"""
                    Default Values


        What happens at run-time...

        When a module is loaded:
            all code is executed immediately
                Module Code
                a = 10          the integer object 10 is created and a references it


                def func(a):    the function object is created and func references it (def)
                    print(a)

                func(a)         the function is executed


        
        What about default values?

                Module Code

                def func(a = 10):   the function object is created and func references it (def)
                    print(a)        the integer object 10 is evaluated/created
                                    and is assigned as the default for a

                func()              the function is executed

                                    by the time this happens, the default value for a has already been
                                    evaluated and assigned - it is not re-evaluated when the function is called

                
        So what?
            Consider this:

                We want to create a function that will write a log entry to the console with a user-specified event
                date/time. If the user does not supply a date/time, we want to set it to the current date/time.


                we may try something like it:

                    from datetime import datetime

                    def log(msg, *, dt=datetime.utcnow()):
                        print("{0}: {1}.format(dt, msg))

                    
                    log("message 1")  -> 2020-08-21 20:52:32.32534 : message 1


                    a few minutes later:

                    log("message 2")  -> 2020-08-21 20:52:32.32534 : message 2

            Solution Pattern

                We set a default for dt to None

                Inside the function we test to see if dt is still None

                If dt is None, set it to the current date/time

                otherwise, use what the caller specified for dt

                example:

                    from datetime import datetime

                    def log(msg, *, dt=None):
                        dt = dt or datetime.utcnow()
                        print("{0}: {1}.format(dt, msg))



                In general, always beware of using a mutable object 
                (or a callable) for an argument default



"""

from datetime import datetime

print(datetime.utcnow())


def log(msg, *, dt=datetime.utcnow()):
    print("{0}: {1}".format(dt, msg))


log("message 1", dt="2001-01-01 00:00:00.000")
log("message 2")

for i in range(100000000):
    var = i + i


log("message 3")

# Interesting outcome:
# 2022-10-04 13:48:29.524746
# 2001-01-01 00:00:00.000: message 1
# 2022-10-04 13:48:29.526624: message 2
# 2022-10-04 13:48:29.526624: message 3


def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print("{0}: {1}".format(dt, msg))


log("message 1", dt="2001-01-01 00:00:00.000")
log("message 2")

for i in range(100000000):
    var = i + i


log("message 3")
# 2001-01-01 00:00:00.000: message 1
# 2022-10-04 13:49:48.809750: message 2
# 2022-10-04 13:49:54.092165: message 3
