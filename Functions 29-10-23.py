# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:31:58 2023

@author: MadCorpSlave
"""
"""
FUNNCTIONS
"""

argPrintTest="Checking if this prints"

def printThis(argPrintTest):
    print(argPrintTest)
    return "Succesful"

printThis(argPrintTest)

sCheck=printThis("Checking if this prints")  ## Creates a check variable tha the function is finished edecuting successfully

printThis()  ## GGives error
printThis(sCheck)  

##  Mumtiple Argument to a functions  
def fnMultiArgument (sName, iAge):
    print("The name :", sName)
    print("The age :", iAge)
    return sName, iAge

print(21,"Percy")   ## Gives error as sequence is wrong

print(fnMultiArgument(iAge=21,sName="Percy"))  ## diffrent sequence but values are assigned. returns 

## function taking one argument default 

def fnAgeDefault(sName, iAge=50):
    print("The name :", sName)
    print("The age :", iAge)
    return    ## retunrs nothing for user 

fnAgeDefault(age=22)  ## Gives error as name is not given 0 expected 
fnAgeDefault(sName="Someone", iAge=22)  ## Works well 
fnAgeDefault(sName="Someone") ## takes default age - no error 

## flexibe argument in function definition 
def fnPrintJunk(arg1, *argAnyThing):
   print("output of this function is :")
   print(arg1)
   
   for variables in argAnyThing:
       print(variables) 
       return
       
fnPrintJunk(10, 2000)    ## prints 2 of the args 
nlCatch=fnPrintJunk(10,20)  ## returns a variable with null
fnPrintJunk(10, 3848,3844,334,3434,"Thus is text",332,"Some Junk")  ## Prints it all in sequence 
##above is not working as intended - need to check

## Mutiple argument to function
def fnSumTotal(a,b,c,d=5,e=20):
     iAdded=a+b+c+d+e
      return iAdded
  
iTotal=fnSumTotal(5,10,15,20)
print(iTotal)

""" Defining function that will add 3 numbers and rtun two values 
"""

def fnSumInfo(a,b,c):
    d=a+b+c
    return d,a

""" See in Variable window - 2 vaiablles will be created  
iAValue and iSum with value of A parameter that is 5 and total that is 30 """

iSum,iAValue=fnSumInfo(5,10,15)  

"""     ************  LAMBDA *****************     """


""" LAMBDA are Short one line function 
"""

fnSumThese = lambda arg1, arg2, arg3 : arg1+arg2 +arg3

iTotal = fnSumThese(10,20,30)  ## Calling labda function 
print(iTotal)  ## shows total of 3 arguments


""" ******** GLOBAL AND LOCAL VAIRABLES """

""" Global Variable x """

x = "awesome"  

""" defining function to use variable x locally - within the 
working area of function. """

def fnPrintX ():
    x = "fantastic"
    """This next line is using LOCAL variable x """
    print("Python is" + x)
    
fnPrintX()  ## Calling  - using the fucnction 

"""This next line is using global variable x """
print("Python is" + x)

""" Making local vaiable global """


""" Global Variable x """

x = "awesome"  

""" defining function to use variable x locally - within the 
working area of function. """

def fnPrintX ():
    global x    ## x becomes global and changes in vaiable explorer 
    x = "fantastic"
    """This next line is using LOCAL variable x """
    print("Python is" + x)
    
fnPrintX()  ## Calling  - using the fucnction 

"""This next line is using global variable x """
print("Python is" + x)

""" Exercise loop """

dsPlayers=["Kohli_WC","Dhavan_WC","Tapan","Riko","Tivo_WC","Ela","Seiko_WC"]
dWorldCup= []

for sParam in dsPlayers:
    if "_WC" in sParam:
        dWorldCup.append(sParam)
return

print(dWorldCup)


""" LIST Comprehenson """

dsPlayers=["Kohli_WC","Dhavan_WC","Tapan","Riko","Tivo_WC","Ela","Seiko_WC"]
dWorldCup= []

""" Interview special"""
""" Comprehension start reading from FOR and variable before FRO will be output """
 
dWorldCup = [Player for Player in dsPlayers if "_WC" in Player]

print(dWorldCup)




"""fills even nubers in the list  
Numbers tthat are divisible by 2 and no remainders"""

NumberList = [x for x in range (20) if x % 2 === 0]
 




"""fills even nubers in the list  
Numbers tthat are divisible by 2 and no remainders"""

NumberList = [x for x in range (20) if x % 2 == 0]
print(NumberList) 



""" TRY and EXCEPT BLOCKS """
x = "X is 1"

"""" first run it without choosing upper line - it will go to excet part """
try:
    print(x)
except:
    print("An exception occured.")

""" choose x wala line and run it will print x value"""


"""Finally wala part will happen regardless - of try workd or not 
and except worked or not """

x = "X is 1"

"""" first run it without choosing upper line - it will go to excet part """
try:
    print(x)
except:
    print("An exception occured.")
finally:
     print("Ye wala block to chalega hi")


