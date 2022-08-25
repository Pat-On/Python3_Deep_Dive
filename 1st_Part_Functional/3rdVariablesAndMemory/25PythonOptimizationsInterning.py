"""

                Python Optimizations

                    Interning


Important Note: 
    - a lot of what we discuss with memory management,
    garbage collection and optimizations, is usually specific to the Python implementation you use

    - in this course we are using CPython, the standard (or reference) Python implementation (written in C)

    - But there are other Python implementations out there: These include:
        + Jython - written in Java and can import and use any Java class - in fact it even
        compiles to Java bytecode which can then run in a JVM
        + IronPython - this one is written in C# and targets .Net (and mono) CLR
        + PyPy - this one is written in RPython (which is itself a statically-typed subset of Python written
        in C that is specifically designed to write interpreters)

                more about it: https://wiki.python.org/moin/PythonImplementations
        
        a = 10
        b = 10              ---> is sharing the same reference in memory


        a = 500
        b = 500             ---> in this case, although it would be safe
                                for Python to create a shared reference, it does not!

        What is going on?

            Interning: reusing objects on-demand

            At startup, PYthon (Cpython), pre-loads (caches) a global list of integers in the range [-5, 256]
                Singletons [in ran ge -5, 256]
                        (Optimization strategy - small integers show up often)


        When we write
            a = 10
        Python just has to point to the existing reference fo 10

        But if we write
            a = 257
        Python does not use that global list and a new object is created every time





"""
