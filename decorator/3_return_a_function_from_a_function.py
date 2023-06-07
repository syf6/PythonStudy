#In fact, there is no need to execute another function in one function, we can also return it as output:
def hi(name="modalive"): 
    def greet():
        return "now you are in the greet() function"
    
    def welcome():
        return "now you are in the welcome() function"
    
    if name == "modalive":
        return greet
    else:
        return welcome

a = hi()
print(a)
#<function hi.<locals>.greet at 0x000001D9945B9360>
#The above clearly shows that `a` now points to the greet() function in the hi() function
#now, try this instead: 
print(a())
#print(hi()())
'''
Look at this code again. 
In the if/else statement we return greet and welcome instead of greet() and welcome(). 
why? 
This is because when you put a pair of parentheses after it, the function will be executed; 
however if you don't put the parentheses after it, then it can be passed around and assigned to other variables without executing it. 
Do you understand it? Let me explain a little more detail.

When we write a = hi(), hi() will be executed, and since the name parameter defaults to modalive, the function greet is returned. 
If we change the statement to a = hi(name = "abc"), then the welcome function will be returned. 
We can also print hi()(), which prints now you are in the greet() function.
'''