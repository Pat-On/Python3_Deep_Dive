"""
------------------ Multi-line Statements and Strings ------------------


        Python Program
            -> physical lines of code (text files)                          end with a physical newline character
                -> Logical lines of code (compiled to, by python compiler)  end with a logical NEWLINE token
                    -> tokenized                                            


        physical newline vs logical newline
            - sometimes, physical newlines are ignored
                in order to combine multiple physical lines
                into a single logical line of code
                terminated by a logical NEWLINE token

                            (because of this implementation we can write multiple physical line that normally
                                should be written in one logical line)

        Conversation can be implicit or explicit

        Implicit example
            Expression in:
                list literals: []
                tuple literals: ()
                dictionary literals: {}
                set literals: {}
                function arguments / parameters

                    supports inline comments

                        Example:                    
                           [1,  # item 1
                            2,  # item 2
                            3]  # item 3

        Explicit example:
            - You can break up statements over multiple lines explicitly, by using the \ (backslash) character
            - multi-line statements are not implicitly converted to a single logical line

                example
                    Wrong example:
                    if a
                        and b
                        and c:

                    Correct example:
                        if a \
                            and b \
                            and c:

            Comments cannot be part of a statement, not even a multi-line statement.

                Wrong example
                        if a \ 
                            and b \ # some comment
                            and c:


------------------ Multi-Line String Literals ------------------

            Multi-line string literals can be created using triple delimiters (' single or " double)


            Be aware that non-visible characters such as newlines tabs, etc. are actually part of the string - basically anything you type

            You can use escaped characters (e.g. \n \t) use string formatting etc

            A multi-line string is just a regular string.

            multi-line string are not comments, although they can be used as such especially with special comments called docstring. 
"""

# list
a = [1, 2, 3]
b = [1,
     2,  # comment
     3, ]

# tuple
c = (1,
     2,
     3)

if a > 5 \
    and b > 4 \
        and c > 20:
    print('yes')
