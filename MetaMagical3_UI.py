import numpy as np
optimum_options = np.loadtxt("Optimum_options_meta3.csv", delimiter=",")
probability = np.loadtxt("Probability_meta3.csv", delimiter=",")

number_testers = input("How many people are there (must be >= 2)? ")
number_testers = int(number_testers)
index = (number_testers-2)
options_needed = optimum_options[index]
probability_specific = round(probability[index]*100, 2)
print("You need ", options_needed, "options. You have a", probability_specific, "% chance of getting only 1-2 winners." )