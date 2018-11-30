# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 20:52:07 2018

@author: conno
"""


import os
import numpy as np
import pandas as pd
pd.set_option('display.expand_frame_repr', False)


from DataLoadGrade import dataLoadGrade
from GradeListGenerator import gradeListGenerator
from GradePlot import gradePlot

#MAIN SCRIPT:
grades = np.array([])
df = np.array([])

while True:
    print('------------------------------------')
    fileSelect = input('Welcome to the Program for grading students.\n\nPlease input filename of csv-file or type (q) to quit the program: ')
    
    #The existing file gets loaded
    if os.path.exists(fileSelect):
    
        grades = (dataLoadGrade(fileSelect))[0]
        df = (dataLoadGrade(fileSelect))[1]
        errorStudentID = (dataLoadGrade(fileSelect))[2]
        errorGrades = (dataLoadGrade(fileSelect))[3]
        
        
        MenuSelect = ()
        #Menu is executed after the file is loaded
        while True:
            try:
                print('------------------------------------')
                print('Active file:\n', fileSelect)
                print('File path:\n',os.path.abspath(os.path.dirname(fileSelect)))
                print('\n------------------------------------')
                print("Main menu:\n1. Load new data\n2. Check for data errors\n3. Generate plots\n4. Display list of grades\n5. Quit")
                print('------------------------------------')        
                MenuSelect = float(input('Choose from the menu above by entering the number of the desired option here: '))
                #Load new data
                if MenuSelect == 1:
                    while True:
                        
                        newFileSelect = input('\nPlease input filename of csv-file or type (q) and press Enter to return to main menu: ')
                        
                        if os.path.exists(newFileSelect):
                            
                            newFileSelect = fileSelect
                            grades = (dataLoadGrade(fileSelect))[0]
                            df = (dataLoadGrade(fileSelect))[1]
                            errorStudentID = (dataLoadGrade(fileSelect))[2]
                            errorGrades = (dataLoadGrade(fileSelect))[3]
                            
                            break
                        if newFileSelect == 'q':
                            print('\nYou have now returned to the main menu\n')
                            break
                        else:
                            print('\nError: Filename is either not valid or it does not exist in current folder.\n')
                #Check for data errors
                elif MenuSelect == 2:
                    if len(errorStudentID) == 0:
                        print('No error in ID')
                    
                    if len(errorStudentID) > 0:
                        print('\nError: Student ID is repeated in lines {}'.format(errorStudentID))
                    
                    if len(errorGrades) == 0:
                        print('No error in grades')
                    
                    if len(errorGrades) > 0:
                        print('\nError: Grades in lines {} are not on the 7-step-scale\n'.format(errorGrades[0]))
                    else:
                        pass
                #Plots
                elif MenuSelect == 3:
                    #Call GradePlot - function
                    gradePlot(grades)
            
                    #Display list of grades
                elif MenuSelect == 4:
                    #Call GradeListGenerator - function
                    print(gradeListGenerator(df,grades))
                #Quit
                elif MenuSelect == 5:
                    break
                if not MenuSelect in range(1,6):
                    print('\nNot valid number-input for the Main Menu. Please choose an option between 1 and 5.\n')
            except ValueError:
                print('\nLetter/symbol-input not valid. You have to input a number in the menu.\n')
        
        break
    
    #If the user types "q", the user exits the program
    if fileSelect == 'q':
        print('\nYou have now exited the program\n')
        break
    #If the file is not valid, print error
    else:
        print('\nError: Filename is either not valid or it does not exist in current folder.\n')
        pass