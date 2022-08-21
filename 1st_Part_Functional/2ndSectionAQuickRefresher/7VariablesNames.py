"""
                    Variables Names

                    Identifier names

    Rules and Conventions

    are case-sensitive
        ham and Ham are different identifiers



    must follow certain rules
        should follow certain conventions


    MUST
        Start with underscore (_) or letter (a-z A-Z)
            followed by any number of underscores(_) , letters (a-z A-Z) or digits (0-9)
                var my_var index1   index_1 _var __var __lt__ <-- are all legal names

        cannot be reserved words:
            None True False etc.

        Conventions

        _my_var (with single underscore)    This is a convention to indicate "internal use" or "private" objects

                                            Objects named this way will not get imported by a statement such as
                                            - from module import *
 
        __my_var (double underscore)        Used to "mangle" class attributes -useful in inheritance chains

        __my_var__ (double underscore start / end)
                                            Used for system-defined names that have a special meaning to the interpreter
                                            Do not invent them, stick to the ones pre-defined by python

                                            __init__  <-- initialize the class
                                            x < y     ----> x.__lt__(y)


                        from the PEP 8 Style Guide:
    Other Naming Conventions:                                                               example:

                Packages    short, all-lowercase names. Preferably no underscores.          utilities
                Modules     Short, all-lowercase names. Can have underscores                db_utilities dbutils
                Classes     CapWords (upper camel case) convention                          BankAccount
                Function    lowercase, words separated by underscores (snake_case)          open_account
                Variables   lowercase, words separated by underscores (snake_case)          account_id
                Constants   all-uppercase, words separated by underscores                   MIN_APR
                
    A foolish consistency is the hobgoblin of little minds (Emerson)

"""
