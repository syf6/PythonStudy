def hi(name = "modalive"): 
    return "hi " + name

print(hi())

#We can even assign a function to a variable, like: 
greet = hi
#We are not using parentheses here because we are not calling the hi function
#Instead, put it in the greet variable. Let's try to run this

print(greet())

#Let's see what happens if we delete the old hi function
del hi
print(hi())

print(greet())