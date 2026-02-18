from vpython import *
import random


##CONSTANTS##

    #Coulombs Constant
SPEED_OF_LIGHT = 299792458                                      #Meters per Second
MAGNETIC_CONSTANT = 1.25663706127e-6                            #Newtons per Ampere
EPSILON_NAUGHT = 1/(MAGNETIC_CONSTANT * SPEED_OF_LIGHT**2)      #Farad per (1/meter)
COULOMB_CONSTANT = 1/(4*pi) * (EPSILON_NAUGHT**-1)              #Newtons per (meters^2/Coulomb^2)

    #Elementary Charge
E = 1.602176634e-19                                             #Coulombs
UP_TYPE_QUARK_CHARGE = (2/3)*E                                  #Coulombs
DOWN_TYPE_QUARK_CHARGE = (-1/3)*E                               #Coulombs

    #Elementary Mass
UP_TYPE_QUARK_MASS = random.uniform(1.7,3.3)
DOWN_TYPE_QUARK_MASS = random.uniform(4.1,5.8)

    #Hadron Charge
PROTON_CHARGE = UP_TYPE_QUARK_CHARGE * 2 + DOWN_TYPE_QUARK_CHARGE
NEUTRON_CHARGE = UP_TYPE_QUARK_CHARGE + DOWN_TYPE_QUARK_CHARGE * 2
ELECTRON_CHARGE = -E


##CLASSES##

    #Elementary Classes
class UpQuark:
    def __init__(self,position):
        self.charge = UP_TYPE_QUARK_CHARGE
        self.mass   = UP_TYPE_QUARK_MASS
        self.visual = sphere(pos=vector(0, 1 + -1/3, 0), radius=1/3, color=color.red)
class DownQuark:
    def __init__(self,position):
        self.charge = DOWN_TYPE_QUARK_CHARGE
        self.mass   = DOWN_TYPE_QUARK_MASS
        self.visual = sphere(pos=vector(0,-1 + 1/3, 0), radius=1/3, color=color.blue)


##Setup##

ProtonSphere = sphere(pos=vector(0, 0, 0), radius=1, color=color.white, opacity=0.5)