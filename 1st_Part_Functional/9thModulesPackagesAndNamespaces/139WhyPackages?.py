# Why Packages?

"""
    Suppose you have 50 different functions and classes in your program

api.py                                              
    connect                                             
    execute_no_result                                               
    execute_single_row                                              
    execute_multi_row                                               
    normalize_string                                                
    convert_str_to_bool                                             
    format_iso_date                                             
    current_time_utc                                                
    authenticate                                                
    validate_token                                              
    get_permissions                                             
    authorize_endpoint                                              

    User
    UserProfile
    Users
    BlogPost
    BlogPosts
    RouteTable
    Configuration
    JSONEncoder
    UnitTests


api/
    api.py
    dbutilities.py
    typeconversions.py
    authentication.py
    authorization.py
    users.py
    blogposts.py
    jsonutilities.py
    validations.py
    logging.py
    unittests.py



better 
    but still unwieldy - everything is at the top level

    to many imports

    certain modules could be broken down further:

        dbutilities -> connections, queries

        users -> User, Users, UserProfile

    Certain modules belong together
        authentication ,authorization -> security


===========================

api/
    utilities/
        __init__.py
        database/
            __init__.py
            connections.py
            queries.py
        json/
            __init__.py
            encoders.py
            decoders.py
    security/
        __init__.py
        authentication.py
        authorization.py
    models/
        __init__.py
        users/
            __init__.py
            user.py
            userprofile.py
--------------------------------


    Another use case

        You have a module that implements 2 functions/ classes for users of the module

        Those two objects require 20 different helper function and 2 additional helper classes

            from module developer's perspective

                much easier to break the code down into multiple modules

            from module user's perspective:
                
                they just want a single import for the function and the class

                    i.e. it should look like a single module

-----------------------

    Module Developer's Perspective

        mylib/
            __init__.py
            submod1.py
            submod2.py
            subpack1
                __init__.py
                pack1mod1.py
                pack1mod2.py

    Smaller code modules, with a specific purpose are easier to write, debug, test and understand



        Module User's Perspective

        mylib/
            __init__.py
            submod1.py
            submod2.py
            subpack1
                __init__.py
                pack1mod1.py
                pack1mod2.py


    user should not have to write:
        from mylib.submod1 import my_func                   <--- internal implementation of package
        from mylib.subpack1.pack1mod2 import MyClass


    much easier for user if they could write:   from mylib import my_func, MyClass

                    or simply                   import mylib

                                                mylib.my_func() mylib.MyClass()

----------------------------------------------

        Using __init__.py

        We can use packages' __init__.py code to export (expose) just what's needed by ou users


        mylib/
            __init__.py                             <---- mylib.__init__.py
            submod1.py                                      from mylib.submod1 import my_func
            submod2.py                                      from mylib.subpack1.pack1mod2 import MyClass
            subpack1        
                __init__.py                                 User uses it this way:
                pack1mod1.py                                    import mylib
                pack1mod2.py                                    mylib.my_func()     mylib.MyClass()
                                                            our internal implementation is hidden.

--------------------------------

    So why packages?

        ability to break code up into smaller chunks, makes our code:

            easier to write
            easier to test and debug
            easier to read and understand
            easier to document

            just like books are broken down into chapters, sections, paragraphs

        but they can still be stitched together
            hides inner implementation from users

            makes their code
                easier to write
                easier to test and debug
                easier to read and understand

                




"""
