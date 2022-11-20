# How does Python Import Modules

"""
When we run a statement such as 

`import fractions`

what is Python actually doing?

The first thing to note is that Python is doing the import 
at **run time**, i.e. while your code is actually running.

This is different from traditional compiled languages such 
as C where modules are compiled and linked at compile time.

In both cases though, the system needs to know **where** 
those code files exist.

Python uses a relatively complex system of how to find 
and load modules. I'm not going to even attempt to describe 
this in detail, but we'll take a brief look at the main points.

"""
import pprint
import sys

pp = pprint.PrettyPrinter(indent=4)


print(sys.prefix)

# location of compiled c binaries
print(sys.exec_prefix)


"""
Basically when we import a module, Python will search 
for the module in the paths contained in `sys.path`. 

If it does not find the module in one of those paths, 
the import will fail.

So if you ever run into a problem where Python is not able
 to import a module or package, you should check this first 
 to make sure the path to your module/package is in that list.
"""
pp.pprint(sys.path)


"""
At a high level, this is how Python imports a module from file:


* checks the `sys.modules` cache to see if the module has already been imported 
    - if so it simply uses the reference in there, otherwise:
* creates a new module object (`types.ModuleType`)
* loads the source code from file
* adds an entry to `sys.modules` with name as key and the newly created
* compiles and executes the source code


One thing that's really to important to note is that when a module is imported,
 the module code is **executed**.
"""
