'''
In the last example, we actually created a decorator! 
Now let's modify the previous decorator and write a slightly more useful program
'''

def a_new_decorator(a_func):

    def wrapTheFunction(): 
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction

def a_function_requiring_decoration(): 
    print("I am the function which needs some decoration to remove my foul smell")

# a_function_requiring_decoration()
# #outputs: "I am the function which needs some decoration to remove my foul smell"

# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# #attention, we do not use () here to execute the function, just pass it
# #now a_function_requiring_decoration is wrapped by wrapTheFunction()

# a_function_requiring_decoration()

'''
Do you understand? 
We have just applied the principles we learned earlier. 
This is exactly what decorators do in python! 
They wrap a function and modify its behavior in one way or another. 
Now you might be wondering, we didn't use the @ symbol in the code? 
That's just a short way to generate a decorated function. 
Here's how we used @ to run the previous code:
'''

@a_new_decorator
def a_function_requiring_decoration():
    """Hey you ! Decorate me !"""
    print("I am the function whhich needs some decoration to remove my foul smell")
    
a_function_requiring_decoration()
