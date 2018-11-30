# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 01:07:48 2018

@author: conno
"""

#Mathilde Tannebæk

import numpy as np

#Function for rounding the grades:
    #Input (grades): A vector of grades in decimal numbers in the interval [-3,12] that does not necesarily follow the 7-step scale
    #Output (gradesRounded): A vector of each grade rounded to the nearest grade on the 7-step scale
             #presumption: if a grade is exactly between two grades on the 7-step scale, it is rounded up
             
def roundGrade(grades):
    
    #Empty array later to be filled up with the rounded grades
    gradesRounded = np.array([])
    
    #Loop that goes through each not-rounded grade
    for i in grades:
        
        #if the respective grade is bigger than or equals to 11, a grade 12 is added to the gradesRounded-array
        if i >= 11:
            gradesRounded = np.append(gradesRounded, 12)
        #if the respective grade is in the interval [8.5, 11[, a grade 10 is added to the gradesRounded-array
        elif (i >= 8.5) and (i < 11):
            gradesRounded = np.append(gradesRounded, 10)
        #if the respective grade is in the interval [5.5, 8.5[, a grade 7 is added to the gradesRounded-array
        elif (i >= 5.5) and (i < 8.5):
            gradesRounded = np.append(gradesRounded, 7)
        #if the respective grade is in the interval [3, 5.5[, a grade 4 is added to the gradesRounded-array
        elif (i >= 3) and (i < 5.5):
            gradesRounded = np.append(gradesRounded, 4)
        #if the respective grade is in the interval [1, 3[, a grade 2 is added to the gradesRounded-array
        elif (i >= 1) and (i < 3):
            gradesRounded = np.append(gradesRounded, 2)
        #if the respective grade is in the interval [-1.5, 1[, a grade 0 is added to the gradesRounded-array
        elif (i >= -1.5) and (i < 1):
            gradesRounded = np.append(gradesRounded, 0)
        #if the respective grade is lower than -1.5, a grade -3 is added to the gradesRounded-array
        elif i < -1.5:
            gradesRounded = np.append(gradesRounded, -3)
    
    #returns the array gradesRounded that has been filled up with the rounded grades of the input
    return gradesRounded
