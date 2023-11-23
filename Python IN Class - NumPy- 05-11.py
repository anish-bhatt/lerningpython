# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:24:35 2023

@author: Bhatt
"""


""" DATA STRUCTURES """
""" NumPy : is a library of mumerical and statistial funtions 
this used for mathamatical data processing """


import numpy as np

"""defines one dimensional array """
aArray1 = np.array([1,2,3,4,5,6,7,8])


""" visualises the shape of array """
aArray1.shape
""" gives only a digit and comma - as this is ony one line  data """


aArray2 = np.array([ [23, 33, 28],
                     [43, 33, 26],
                     [43, 42, 33] ])
""" see it in variable explorer """

""" Shows shape as 3,3 = 3 row 3 col """
aArray2.shape

""" Shows dimensions as 2 """
aArray2.ndim

""" makes first element of first row 900 """
aArray2[0] = 900 

aArray2[2,1] = 00
""" chages 2nd element of third row  """

""" Shows shape of array """
aArray2.shape

""" shows memory allocation size """
aArray2.size 

""" tells type of elements in an array """
aArray2.dtype 


""" Reshaping array """

aArray2 = np.array([ [23, 33, 28],
                     [43, 33, 26],
                     [43, 33, 26],
                     [43, 42, 33] ])

aArray2.size
aArray2 = aArray2.reshape(3,4)

""" ERROR """
aArray2 = aArray2.reshape(3,3)

""" Size should be same  """
aArray2 = aArray2.reshape(4,3)  

aArray2 = aArray2.reshape(2,6)  

aArray2 = aArray2.reshape(12,1)

aArray2 = aArray2.reshape(1,12)  




""" Matrices   = matrix 

number of row x number of col same = square matrix 
elemts are checked in index manner 

col of matrix a should be same as row of matrix b 

2x3 = 0 zero matitx filled with 0 
"""

mtOne = np.zeros((3,4))

mtTwo = np.eye(5)  

print(mtOne.shape)

aArray3 = np.array([ [1, 2, 3],
                     [4, 4, 6],
                     [7, 7, 9],
                     [10, 11, 12] ])

""" reating an array from one line  
"""

""" array starting from 0, upto 60, icreaennt by 5, type integer """
aAutoArr= np.arange(0,60,5,dtype="int")  
aAutoArr.ndim
aAutoArr=aAutoArr.reshape(4,3)
aAutoArr.ndim



""" how the control moves in an array 
MISTAKE
"""

aArray3 = np.array([ [1, 2, 3],
                     [4, 4, 6],
                     [7, 7, 9],
                     [10, 11, 12] ])
aArray3.ndim
for itr in np.nditer(aArray3):
    print(itr * itr, end=",")

""" makes new arrray C Repeats to fill values
"""
c=np.resize(aArray3,(5,4)) 

""" Like excel transpose rows and cols switch places """
aTranspose=np.transpose(aArray3)

""" try using debug 
"""
aAutoArr= np.arange(0,60,5,dtype="int")  
aResizeTrans=np.transpose(np.resize(aAutoArr,(4,4)))

""" Mathamatical expressions """
array1.sqrt 
array1.exp
array1.log
array1.std

"""
HomeWrok 
dff between flatten and ravel

"""
aAutoArr.flatten()
np.ravel(aAutoArr)




 




