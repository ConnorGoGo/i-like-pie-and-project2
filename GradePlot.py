# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 01:03:56 2018

@author: conno
"""

from ComputeFinalGrades import computeFinalGrades

import matplotlib.pyplot as plt
import numpy as np
import random

def gradePlot(grades):

    #Plot 1
    finalGrades = computeFinalGrades(grades)
    finalGradesList = finalGrades.tolist()
    
    #The range of x is set to the amount of grade-types
    xAxis = range(7)
    #Sets the y-axis to be the amount of each grade given
    yAxis = [finalGradesList.count(-3), finalGradesList.count(0), finalGradesList.count(2), finalGradesList.count(4), finalGradesList.count(7), finalGradesList.count(10), finalGradesList.count(12)]
    
    gradeNumbers = ('-3','00','02','4','7','10','12')
    
    #Make bar plot, lable and title and set the grade types under each bar:
    plt.bar(xAxis, yAxis, alpha=0.5, color="slateblue")  
    plt.xlabel('Final grades') 
    plt.ylabel('Number of students') 
    plt.title('Final grades', fontsize=15) 
    plt.xticks(xAxis, gradeNumbers)
    plt.grid()
    plt.show()
    
    
    #Plot 2
    
    numberOfAssignments = np.size(grades[0,:])
    
    #Points
    x1 = np.array([])
    y1 = np.array([])
    for i in range(numberOfAssignments):  #  +1?
        x1 = np.append(x1, (np.arange(numberOfAssignments) + 1 + random.uniform(-0.1, 0.1)) )
        y1 = np.append(y1, (grades[i,:] + random.uniform(-0.1, 0.1)))
        
    #average grade line plot
    y2 = np.array([])
    x2 = np.arange(1, numberOfAssignments+1)
    for j in range(numberOfAssignments):
        y2 = np.append(y2, np.mean(grades[:,j]))
    
    plt.plot(x1, y1, 'bo')
    plt.plot(x2, y2, label='Mean grade for assignment',linestyle='-')

    
    gradeTypes = np.array([-3,0,2,4,7,10,12])
    
    plt.yticks(gradeTypes)  
    plt.xticks(range(1, numberOfAssignments+1))
    plt.xlabel('Assignments') 
    plt.ylabel('Grades') 
    plt.title('Grades per assignment', fontsize=15) 
    plt.grid()
    plt.show()
