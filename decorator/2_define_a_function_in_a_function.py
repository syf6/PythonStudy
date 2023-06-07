#in python we can define a function in another function
def hi(name="modalive"):
    print("now you are inside the hi funciton")

    def greet():
        return "now you are in the greet function"
    
    def welcome():
        return "now you are in the welcome() function"
    
    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
#The above shows that whenever you call hi(), greet() and welcome() will be called at the same time.
#Then the greet() and welcome() functions cannot be accessed outside the hi() function, for example:
greet()
#NameError: name 'greet' is not defined

#So now we know that we can define other functions inside functions. That is: we can create nested functions. Now you need to learn a little more, that functions can also return functions.