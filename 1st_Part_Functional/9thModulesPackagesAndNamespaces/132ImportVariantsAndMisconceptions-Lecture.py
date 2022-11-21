# Import Variants and Some Misconceptions

# import variants

import math

# is math in sys.modules?
# if not, load it and insert ref

# sys.modules
# math <module object>

# add symbol math to module1's global namespace referencing the same object

# module1.globals()
# math <module object>
# math symbol in namespace

# (If math symbol already exist in module1's namepsace, replace referece)


# ------------------

import math as r_math

# is math in sys.modules?
# if not, load it and insert ref

# sys.modules
# math <module object>

# add symbol r_math to module1's global namespace referencing the same object

# module1.globals()
# r_math <module object>
# math symbol not in namespace

# (If r_math  symbol already exist in module1's namepsace, replace referece)


# ------------------

from math import sqrt

# is math in sys.modules?
# if not, load it and insert ref

# sys.modules
# math <module object>

# add symbol sqrt to module1's global namespace referencing math.sqrt

# module1.globals()
# sqrt <math.sqrt object>
# math symbol not in namespace

# (If sqrt symbol already exist in module1's namepsace, replace referece)


# ------------------

from math import sqrt as r_sqrt

# is math in sys.modules?
# if not, load it and insert ref

# sys.modules
# math <module object>

# add symbol r_sqrt to module1's global namespace referencing math.sqrt

# module1.globals()
# sqrt <math.sqrt object>
# math symbol not in namespace

# (If r_sqrt symbol already exist in module1's namepsace, replace referece)


# ------------------

from math import *

# is math in sys.modules?
# if not, load it and insert ref

# sys.modules
# math <module object>


# add "all" symbols defined n math to module1's global namespace

# what all means can be defined by the module being imported

# pi <math.pi object >
# sin <math.sin object>                 (math symbol not in namespace)
# and many many more

# (if any symbols already exists in module1's namespace, replace their reference)
"""

Commonality 


    in every case the math module was loaded into memory and referenced in sys.modules

    Running         from math import sqrt

        did not "partially" load math

        if only affected what symbols were placed in module1's namespace!

    Things may be different with packages, but for simples modules this is the behavior


-----------

    Why from <module> import * can lead to bugs


    # module1.py

    from cmath import *

                            module.globals()
                                sqrt <cmath.sqrt>

    from math import *

                            module1.globals()
                                sqrt <math.sqrt>
    

-------

    Efficiency

        What is more efficient?

                import math

                    or

                from math import sqrt

        importing ->> same amount of work

        calling math.sqrt(2)    <-- this first needs to find the sqrt symbol in math's namespace
                                   
                sqrt(2)         <-- there is one less lookup in dictionaries
                                        dict lookup -> super fast!

                                In this case readability is going to give you more than this one less lookup in dictionary



"""
