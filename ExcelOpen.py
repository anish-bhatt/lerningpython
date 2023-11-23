# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:26:49 2023

@author: Bhatt
"""
"""

## Pandas functions to be used 

import pandas as pd
from tkinter import filedialog
## show a dialog box to select an excel file to load 

def load_excel_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    return file_path

## read the excel file into a pandas dataframe

def read_excel_file(file_path):
    dfExlFile = pd.read_excel(file_path)
    return dfExlFile
"""
## Pandas functions to be used 

import pandas as pd 
import numpy as np  
import tkinter as tk
from tkinter import filedialog


## load the excel file

def load_excel():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

## put excel file content in to a dataframe 

def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df

df=dfExl

