##########################################
# Rondenay, Jeanne, <6240890>
##########################################

import random
import matplotlib.pyplot as plt
import numpy as np

#Question 1 : Température du terrarium

def question1():
   print("Question 1 : Température du terrarium")
   print()

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

    print("Question 2 : Croissance d'une population bactérienne")
    print()
    pop_initiale=float(input("Veuillez entrer la population initiale de bactéries."))
    pop_chaque_heure=[]
    jour=[]
    for i in range(11):
        pop_chaque_heure.append(pop_initiale)
        pop_initiale=pop_initiale*(np.pi/1.5)
        jour.append(i)

    plt.figure(figsize=(10,10))
    plt.grid(True)
    plt.title("Croissance bactérienne")
    plt.xlabel("Heure")
    plt.ylabel("Population")
    plt.plot([0,10],[50000,50000],"r--")
    plt.plot([jour],[pop_chaque_heure],"*b")
    plt.show()

question2(100)



