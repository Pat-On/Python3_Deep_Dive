"""

            What are implicit Namespace PAckages?

            Namespace packages are package-like

                directories
                    may contain modules
                    may contain nested regular packages
                    may contain nested namespace packages
                    but cannot contain __init__.py

            These directories are implicitly made into these special types of packages. 

                        PEP 420

-----------------

        Mechanics

            utils/                                      utils/ does not contains __init__.py            -> namespace packages
                validators/                             validators/ does not contains __init__.py       -> namespace packages
                    boolean.py                          boolean.py is a file with a .py extension       -> module
                    date.py
                    json/                               json/ contains __init__.py                      -> regular package
                        __init__.py
                        serializers.py                  serializers.py  is a file with a .py extension  -> module
                        validators.py

-----------------

    Regular vs Namespace Packages

        Regular Package                                                     Namespace Package

        type    ->  module                                                  type -> module

        __init__.py -> yes                                                  __init__.py -> no

        __file__    -> package __init__                                     __file__  -> not set
        
        paths   -> breaks if parent                                         paths -> dynamic path computation so
                    directories change                                                  ok if parent directories change
                    and absolute imports 
                    are used                                                        (your import statements will still need to be modified)

        single package lives in single directory                            single package can live in multiple (non-nested) directories
                                                                            in fact, parts of the namespace may even be in a zip file

"""
