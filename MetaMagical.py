# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 00:24:21 2020

@author: Edward Elric
"""
from math import comb
import numpy as np
import matplotlib.pyplot as plt

#%%

y = input("How many levels? ")
odds = input("What are the odds of survival in decimal form (eg. .9)? " )

y= int(y)
odds = float(odds)

chances = np.array([])

life_100 = odds**y
chances = np.append(chances, life_100)
print("Your chance of survival is ", life_100)

x = 1

while x < y:
    base_percent = (odds**(y-x))*((1-odds)**(x))
    #combo_factor = fac(y)/((fac(y-x))*fac(x))
    combo_factor = comb(y, x)
    complex_chance = base_percent * combo_factor
    chances = np.append(chances, complex_chance)
    #print("The probability of ", x, "deaths is", complex_chance)
    x = x+1

death_100 = (1-odds)**y
print("Your chance of becoming swiss cheese is ", death_100)
chances = np.append(chances, death_100)

print("Double checking!")
total = np.sum(chances)
print(total)


x = np.linspace(0, y, y+1)

plt.figure(dpi=100)

plt.plot(x, chances, color = 'green', linewidth = 2, linestyle = '-')
plt.axvline(x=y*(1-odds))

plt.grid()
plt.title("Distribution of Deaths at Set Survival Rate")
plt.legend(['Probability of Hitting Death Count', 'Levels * Survival Rate'], fontsize = 10) 
plt.xlabel('Number of Deaths')
plt.ylabel('Probability')
plt.xlim([-2,y+5])
plt.ylim([0, np.max(chances)*1.1])
     
plt.show()


