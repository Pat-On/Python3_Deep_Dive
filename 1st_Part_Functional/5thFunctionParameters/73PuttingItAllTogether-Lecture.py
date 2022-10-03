"""
        Putting all together



    Recap

        positional arguments

    specific    may have default values

    *args       collects, and exhausts remaining positional arguments

    *           indicates the and of positional arguments (effectively exhausts)

                        a, b, c=10
                        *args / *



        Keyword-only arguments

    after positional arguments have been exhausted

    specific    may have default values

    **kwargs    collects any remaining keyword arguments - to the dictionary

                        kw1, kw2=100
                        **kwargs
------------------------------------------------------------------------------------------
Example:

    Typical use case: Python's print() function

        from doc:
            print(*objects. sep='', end='\n', file=sys.std.out, flush=False)


    Typical use cases:

        - Often, keyword-only arguments are used to modify the default behavior of a function
        such as the print() function we just saw

    def calc_hi_to_avg(*args, log_to_console=False):
        hi = int(bool(args)) and max(args)
        lo = int(bool(args)) and min(args)
        avg = (hi + to) / 2
        if log_to_console:
            print(hi, lo, avg)
        return avg


"""


def calc_hi_to_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo) / 2
    if log_to_console:
        print(hi, lo, avg)
    return avg
