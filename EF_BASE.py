from vpython import *

##CONSTANTS##

    #Coulombs Constant
SPEED_OF_LIGHT = 299792458                                      #Meters per Second
MAGNETIC_CONSTANT = 1.25663706127e-6                            #Newtons per Ampere
EPSILON_NAUGHT = 1/(MAGNETIC_CONSTANT * SPEED_OF_LIGHT**2)      #Farad per (1/meter)
COULOMB_CONSTANT = 1/(4*pi) * (EPSILON_NAUGHT**-1)              #Newtons per (meters^2/Coulomb^2)

    #Elementary Charge
E = 1.602176634e-19                                             #Coulombs
UP_TYPE_QUARK = (2/3)*E                                         #Coulombs
DOWN_TYPE_QUARK = (-1/3)*E                                      #Coulombs
#UP_TYPE_ANTIQUARK = - UP_TYPE_QUARK                            #Coulombs
#DOWN_TYPE_ANTIQUARK = -DOWN_TYPE_QUARK                         #Coulombs

    #Hadron Charge
PROTON_CHARGE = UP_TYPE_QUARK * 2 + DOWN_TYPE_QUARK
NEUTRON_CHARGE = UP_TYPE_QUARK + DOWN_TYPE_QUARK * 2
ELECTRON_CHARGE = -E

