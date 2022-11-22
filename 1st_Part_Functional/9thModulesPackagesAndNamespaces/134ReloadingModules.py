# Reloading Modules


import importlib
import sys
import os


def create_module_file(module_name, **kwargs):
    '''Create a module file named <module_name>.py
    Module has a single function (print_values) that will print
    out the supplied (stringified) kwargs
    '''

    module_file_name = f'{module_name}.py'
    module_rel_file_path = module_file_name
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'w') as f:
        f.write(f'# {module_name}.py\n\n')
        f.write(f"print('running {module_file_name}...')\n\n")
        f.write(f'def print_values():\n')
        for key, value in kwargs.items():
            f.write(f"\tprint('{str(key)}', '{str(value)}')\n")


create_module_file("test", k1=10, k2='Python')

try:
    import test
except:
    print("Exception")

test.print_values()

create_module_file("test", k1=10, k2="Python", k3="cheese")


try:
    import test
except:
    print("Exception")

test.print_values()


print("id: ", id(test))

# the way to force reloading - remove reference sys module
print('test' in sys.modules)

del sys.modules['test']
print('test' in sys.modules)

try:
    import test
except:
    print("Exception")

print("id: ", id(test))
test.print_values()

create_module_file("test", k1=10, k2="Python", k3="cheese", k4="parrots")

# reload of object - mutating - it is safe way of doing it, but you should not do it :>
importlib.reload(test)

test.print_values()


create_module_file('test2', k1="python")


try:
    from test2 import print_values
except:
    print("Exception")

print('test2' in globals())
print('test2' in sys.modules)

print_values()

create_module_file('test2', k1="python", k2="cheese")

importlib.reload(sys.modules['test'])

# not updated! all because of the references to old module
print_values()
