# main.py

import sys
import module1
print('================================')
print('Running main.py - module name: {0}'.format(__name__))


print(module1)

module1.pprint_dict('main.globals', globals())

print(sys.path)

print('================================')
