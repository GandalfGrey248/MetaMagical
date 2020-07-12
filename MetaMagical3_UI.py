import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

optimum_options = np.loadtxt("Optimum_options_meta3.csv", delimiter=",")
probability = np.loadtxt("Probability_meta3.csv", delimiter=",")
optimum_ratio = np.loadtxt("Optimum_ratio_meta3.csv", delimiter=",")
size = np.size(optimum_ratio)

i = 0
while i == 0:
    print("")
    print("Choose Option:")
    print("[1] - View Graphs")
    print ("[2] - Identify Optimum # of Options for Select # of Participants")
    print("[3] - Exit")
    print("")
    choice = input("=> ")
    choice = int(choice)
    if choice == 1:
        print("")
        print("Choose Option:")
        print("[1] Default Range")
        print("[2] Customized Range")
        print("[3] - Return to Main")
        print("")
        choice_2 = input("=> ")
        choice_2 = int(choice_2)
        
        if choice_2 == 1:
            x = np.linspace(2, size+1, size, endpoint=True)

            plt.figure(1, dpi=100)

            plt.subplot(131)
            plt.plot(x, optimum_options, color = 'purple', linewidth = 2, marker='.', linestyle = 'dashed')
            plt.title("Number of Options Needed per # of Participants")
            plt.xlabel('# of Participants')
            plt.ylabel('# of Options')
            plt.legend(['Trend'], loc='upper center', bbox_to_anchor=(0.5, 5), ncol=2) 
            plt.grid()

            info_1 = linregress(x, optimum_options)
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
            plt.plot(x, probability, color = 'purple', linewidth = 2, marker = '.', linestyle = 'dashed')
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

            continue
        if choice_2 == 2:
            min = int(input("What min value? "))
            max = int(input("What max value? "))

            x = np.linspace(min, max, (max-min+1), endpoint=True)
            optimum_options_custom = optimum_options[(min-2):(max-1)]
            probability_custom = probability[(min-2):(max-1)]
            optimum_ratio_custom = optimum_ratio[(min-2):(max-1)]

            plt.figure(1, dpi=100)

            plt.subplot(131)
            plt.plot(x, optimum_options_custom, color = 'purple', linewidth = 2, marker='.', linestyle = 'dashed')
            plt.title("Number of Options Needed per # of Participants")
            plt.xlabel('# of Participants')
            plt.ylabel('# of Options')
            plt.legend(['Trend'], loc='upper center', bbox_to_anchor=(0.5, 5), ncol=2) 
            plt.grid()

            info_1 = linregress(x, optimum_options_custom)
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
            plt.plot(x, probability_custom, color = 'purple', linewidth = 2, marker = '.', linestyle = 'dashed')
            plt.title("Probability of Achieving 1-2 Winners")
            plt.xlabel('# of Participants')
            plt.ylabel('Probability of 1-2 People Getting Chosen')
            plt.legend(['Trend'], loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2) 
            plt.grid()

            plt.subplot(133)
            plt.plot(x, optimum_ratio_custom, color = 'blue', linewidth = 2, marker = '.', linestyle = 'dashed')
            plt.title("Finding the Optimum Ratio of Options to Participants")
            plt.xlabel('# of Participants')
            plt.ylabel('Optimum Ratio of Options to Participants')
            plt.legend(['Trend'], loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2) 
            plt.grid()

            plt.show()
            continue
        if choice_2 == 3:
            continue
    if choice == 2:
        number_testers = input("How many people are there (must be 2<= & >= 10000)? ")
        number_testers = int(number_testers)
        index = (number_testers-2)
        options_needed = optimum_options[index]
        probability_specific = round(probability[index]*100, 2)
        print("You need ", options_needed, "options. You have a", probability_specific, "% chance of getting only 1-2 winners." )

        continue
    if choice == 3:
        break