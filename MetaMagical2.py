# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:48:39 2020

@author: Edward Elric
"""

from math import comb
import numpy as np
import matplotlib.pyplot as plt
#import winsound
#frequency = 750 # Set Frequency To 2500 Hertz
#duration = 1000  # Set Duration To 1000 ms == 1 second
from time import time as tm

#%%
y = input("How many participants are there? ")
y = int(y)

i=1
t0 = tm()
single_winner_chances = np.array([])
no_winner_chances = np.array([])
two_winner_chances = np.array([])
multi_winner_chances = np.array([])
null_winner_chances = np.array([])
null2_winner_chances = np.array([])

while i<(y+1):    
    odds = 1-(1/i)
    
    z=1
    base_percent = (odds**(y-z))*((1-odds)**(z))
    #combo_factor = fac(y)/((fac(y-z))*fac(z))
    combo_factor = comb(y, z)
    complex_chance = base_percent * combo_factor
    single_winner_chances = np.append(single_winner_chances, complex_chance)
    
    z=2
    base_percent = (odds**(y-z))*((1-odds)**(z))
    #combo_factor = fac(y)/((fac(y-z))*fac(z))
    combo_factor = comb(y, z)
    complex_chance = base_percent * combo_factor
    two_winner_chances = np.append(two_winner_chances, complex_chance)
    
    no_winner_chance = odds**y
    no_winner_chances = np.append(no_winner_chances, no_winner_chance)
    
    if (i) % (y/5) == 0: #rep tracker\n",
        t1 = tm() #setting the end time for the rep tracker
        time_elapsed = t1- t0 #calculating difference between beginning and end time of the tracker\n",
        print("Repct:", i, "; Timelap:", time_elapsed, "secs") #printing the results
        #winsound.Beep(frequency, duration)
        t0 = tm() #resetting the tracker\n",
    i= i+1
#winsound.Beep(frequency, duration)
print("Done!")        

multi_winner_chances = two_winner_chances + single_winner_chances

marginal_sing_winner_chances = single_winner_chances - no_winner_chances
max_marginal_benefit_1 = np.max(marginal_sing_winner_chances)
#location_2_1 = np.where(marginal_sing_winner_chances == max_marginal_benefit_1)

marginal_two_winner_chances = two_winner_chances - no_winner_chances
max_marginal_benefit_2 = np.max(marginal_two_winner_chances)
#location_2_2 = np.where(marginal_two_winner_chances == max_marginal_benefit_2)

marginal_multi_winner_chances = multi_winner_chances - no_winner_chances
max_marginal_benefit_3 = np.max(marginal_multi_winner_chances)
#location_2_3 = np.where(marginal_multi_winner_chances == max_marginal_benefit_3)
#location_2_4 = np.where(multi_winner_chances == np.max(multi_winner_chances))

null_winner_chances = np.append(null_winner_chances, 1-(single_winner_chances + two_winner_chances))
null2_winner_chances = np.append(null2_winner_chances, 1-(single_winner_chances))

marginal_goalfor_winner_chances = multi_winner_chances - null_winner_chances
max_marginal_benefit_4 = np.max(marginal_goalfor_winner_chances)
location_2_5 = np.where(marginal_goalfor_winner_chances == max_marginal_benefit_4)

#print(location_2_1)
#print(location_2_3)
#print(location_2_2)
#print(location_2_4)
#print(location_2_5)

x = np.linspace(0, y, y)
plt.figure(dpi=100)
plt.plot(x, single_winner_chances, color = 'green', linewidth = 2, linestyle = '-')
#plt.plot(x, no_winner_chances, color = 'red', linewidth = 2, linestyle = '-')
plt.plot(x, two_winner_chances, color = 'blue', linewidth = 2, linestyle = '-')
plt.plot(x, multi_winner_chances, color = 'pink', linewidth = 2, linestyle = '-')
plt.plot(x, null_winner_chances, color = 'purple', linewidth = 2, linestyle = '-')
plt.plot(x, null2_winner_chances, color = 'orange', linewidth = 2, linestyle = '-')

#plt.axvline(x = location_2_1)
#plt.axvline(x = location_2_2)
#plt.axvline(x = location_2_3)
#plt.axvline(x = location_2_4)
plt.axvline(x = location_2_5)

plt.grid()
plt.title("Finding Optimum # of Options for Set # of Participants")
plt.legend(['One', 'Two', 'One&Two', 'All minus One&Two', 'All minus One'], bbox_to_anchor=(1, 1), ncol=2) 
plt.xlabel('# of Options')
plt.ylabel('Probability')
plt.xlim([0, y])
plt.ylim([0, 1])

plt.show()

print(location_2_5)





