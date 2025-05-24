#block of code
#Data can be called its called parameter
#function can return data as a result
def my_function():
    print("Hello")
my_function()
#Arguments information can be passed
#we can pass any number of arg
def full_name(fname,lname):
    print(fname," ",lname)
full_name("priya","babu")
#* can take multiple arg
def some_names(*names):
    print(names)
some_names("priya","vaish")
#kwyword arguments
#arbitary **
#default parameter-check this
def myfunction(x):
    return 5*x
print(myfunction(4))
#pass function 
#Recursion - functions that calls itself

