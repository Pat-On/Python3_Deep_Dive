"""
    Some languages (Java, C++, Swift) are statically typed
                    We are associating data type to variable :>
    JAVA:
    String myVar = "hello";
    Java is creating object string in memory 


    String       ref        String  0x1000
    myVar       ----->       hello


    myVar = 10      Does not work!  myVar has been declared as a string
                    and cannot be assigned the integer value 10 later

    myVar = "abc"   <--- ok, because it is string



    Python, in contrast is dynamically typed:
        my_var = "hello"
            The variable my_var is purely a reference to a string object with value hello.
            no type is attached to my_var

        my_var = 10
            the variable my_var is now point to an integer object with value 10

        - my_var is just a reference and its type was never defined.

    
    We can use the built-in type() function to determine
    the type of the object currently referenced by a variable.

    Remember: variables in Python do not have an inherent static type

    Instead, when we call type(my_var)
        Python look up the object my_var is referencing (pointing to),
        and return the type of the object at that memory location.


"""

a = "hello"
print(type(a))
