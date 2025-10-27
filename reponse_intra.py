##########################################
# Rondenay, Jeanne, <6240890>
##########################################

import random
import matplotlib.pyplot as plt
import numpy as np

#Question 1 : Température du terrarium

def question1():
   print("Question 1 : Température du terrarium")

   for i in range(10):
        temperature_journee=round(random.uniform(20,35),1)

        if 24<=temperature_journee<=30:
            print("Jour", i+1, ":", temperature_journee,  "°C")
            print("OK")
        elif temperature_journee<24:
            print("Jour", i + 1, ":", temperature_journee, "°C")
            print("Trop froid")
        else:
            print("Jour", i + 1, ":", temperature_journee, "°C")
            print("Trop chaud")

   print("Fin")

question1()
print()

#Question 2 : Croissance d'une population bactérienne

def question2(pop_initiale):
    pop_initiale=float(input("Veuillez entrer la population initiale de bactéries."))
    pop_chaque_heure=[]
    jour=1
    for i in range(11):
        pop_chaque_heure.append(pop_initiale)
        pop_initiale=pop_initiale*(np.pi/1.5)

    plt.figure(figsize=(10,10))
    plt.grid(True)
    plt.title("Croissance bactérienne")
    plt.xlabel("Heure")
    plt.ylabel("Population")
    plt.plot([0,10],[50000,50000],"r--")
    plt.plot(0, pop_chaque_heure[0], "*b")
    plt.plot(1,pop_chaque_heure[1],"*b")
    plt.plot(2, pop_chaque_heure[2], "*b")
    plt.plot(3, pop_chaque_heure[3], "*b")
    plt.plot(4, pop_chaque_heure[4], "*b")
    plt.plot(5, pop_chaque_heure[5], "*b")
    plt.plot(6, pop_chaque_heure[6], "*b")
    plt.plot(7, pop_chaque_heure[7], "*b")
    plt.plot(8, pop_chaque_heure[8], "*b")
    plt.plot(9, pop_chaque_heure[9], "*b")
    plt.plot(10, pop_chaque_heure[10], "*b")
    plt.show()


question2(100)








