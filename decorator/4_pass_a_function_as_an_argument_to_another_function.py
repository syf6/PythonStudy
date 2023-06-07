def hi():
    return "hi modalive! "

#the arguments we pass here is the function
def doSomethingBeforeHi(func): 
    print("I am doing some boring work before executing hi()")
    print(func())

doSomethingBeforeHi(hi)

'''
Now that you have all the necessary knowledge, let's move on to what a decorator really is. 
Decorators let you execute code before and after a function.
'''