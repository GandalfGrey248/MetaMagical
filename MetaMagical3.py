# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:41:27 2020

@author: Edward Elric
"""
from math import factorial as fac
import numpy as np
import matplotlib.pyplot as plt
#import winsound
#frequency = 600 # Set Frequency To 2500 Hertz
#duration = 500  # Set Duration To 1000 ms == 1 second
from time import time as tm
from scipy.stats import linregress


#%%

num_dice = np.array([])
chances = np.array([])
optimum_ratio = np.array([])

test = input("What is the max # of participants do you expect? ")
test = int(test)

y=2
i=1

t0 = tm()
while y < test+2:
    i=2
    single_winner_chances = np.array([])
    two_winner_chances = np.array([])
    null_winner_chances = np.array([])
    multi_winner_chances = np.array([])
    while i<(2*y)+2:    
        odds = 1-(1/i)
        
        z=1   
        base_percent = (odds**(y-z))*((1-odds)**(z))
        combo_factor = fac(y)/((fac(y-z))*fac(z))
        complex_chance = base_percent * combo_factor
        single_winner_chances = np.append(single_winner_chances, complex_chance)
        
        z=2
        base_percent = (odds**(y-z))*((1-odds)**(z))
        combo_factor = fac(y)/((fac(y-z))*fac(z))
        complex_chance = base_percent * combo_factor
        two_winner_chances = np.append(two_winner_chances, complex_chance)
        
        

        i = i + 1
    
    null_winner_chances = np.append(null_winner_chances, 1-(single_winner_chances + two_winner_chances))
    multi_winner_chances = np.append(multi_winner_chances, (two_winner_chances + single_winner_chances))
    marginal_goalfor_winner_chances = multi_winner_chances - null_winner_chances
    max_marginal_benefit_1 = np.max(marginal_goalfor_winner_chances)
    
    size = np.size(marginal_goalfor_winner_chances)
    q=0
    while q < size-1:
        if marginal_goalfor_winner_chances[q] == max_marginal_benefit_1:
            optimum_sides = q+2
            num_dice = np.append(num_dice, optimum_sides)
            chances = np.append(chances, multi_winner_chances[q])
            optimum_ratio = np.append(optimum_ratio, (optimum_sides/y))
            break
        q = q+1
    
    if (y) % ((test)/5) == 0: #rep tracker\n",
            t1 = tm() #setting the end time for the rep tracker
            time_elapsed = t1- t0 #calculating difference between beginning and end time of the tracker\n",
            print("Repct:", y, "; Timelap:", time_elapsed, "secs") #printing the results
            #winsound.Beep(frequency, duration)
            t0 = tm() #resetting the tracker\n",
    y = y+1

print("Done!")

x = np.linspace(2, test+2, test, endpoint=False)
plt.figure(1, dpi=100)

plt.subplot(131)
plt.plot(x, num_dice, color = 'purple', linewidth = 2, marker='.', linestyle = 'dashed')
plt.title("Number of Options Needed per # of Participants")
plt.xlabel('# of Participants')
plt.ylabel('# of Options')
plt.legend(['Trend'], loc='upper center', bbox_to_anchor=(0.5, 5), ncol=2) 
plt.grid()

info_1 = linregress(x, num_dice)
slope_1 = info_1[0]
intercept_1 = info_1[1]
rval_1 = info_1[2]
pval_1 = info_1[3]
std_1 = info_1[4] 

print("")
print("Data for Fig. 1: ")
print("Slope: ", slope_1)
print("Intercept: ", intercept_1)
print("Rval: ", rval_1)
print("Pval: ", pval_1)
print("Std: ", std_1)

plt.subplot(132)
plt.plot(x, chances, color = 'purple', linewidth = 2, marker = '.', linestyle = 'dashed')
plt.title("Probability of Achieving 1-2 Winners")
plt.xlabel('# of Participants')
plt.ylabel('Probability of 1-2 People Getting Chosen')
plt.legend(['Trend'], loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2) 
plt.grid()

plt.subplot(133)
plt.plot(x, optimum_ratio, color = 'blue', linewidth = 2, marker = '.', linestyle = 'dashed')
plt.title("Finding the Optimum Ratio of Options to Participants")
plt.xlabel('# of Participants')
plt.ylabel('Optimum Ratio of Options to Participants')
plt.legend(['Trend'], loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2) 
plt.grid()

plt.show()

np.savetxt("Optimum_options_meta3.csv", num_dice, delimiter = ",")
np.savetxt("Probability_meta3.csv", chances, delimiter = ",")
