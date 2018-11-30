# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:57:27 2018

@author: conno
"""

from ComputeFinalGrades import computeFinalGrades

#Input: Dataframe and a M x N matrix of grades
#Output: Dataframe with final grades

def gradeListGenerator(df,grades):
    gradesList = df #Redefine dataframe
    FinalGrade = computeFinalGrades(grades).tolist()
    gradesList['Final grade'] = FinalGrade
    gradesList = gradesList.sort_values('Name')
    return gradesList