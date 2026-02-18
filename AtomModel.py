from vpython import *
import random


##CONSTANTS##
# Unit Conversions
eVc = 1.7826619216279e-36  # eV/c^2 convert to kilogram
fm = 1e-15  # femtometre to meter
qSqrt3 = 1 / sqrt(3)  # just to make it easier

# Coulombs Constant
SPEED_OF_LIGHT = 299792458  # Meters per Second
MAGNETIC_CONSTANT = 1.25663706127e-6  # Newtons per Ampere
EPSILON_NAUGHT = 1 / (MAGNETIC_CONSTANT * SPEED_OF_LIGHT**2)  # Farad per (1/meter)
COULOMB_CONSTANT = (
    1 / (4 * pi) * (EPSILON_NAUGHT**-1)
)  # Newtons per (meters^2/Coulomb^2)

# Elementary Charges
E = 1.602176634e-19  # Coulombs
UP_TYPE_QUARK_CHARGE = (2 / 3) * E  # Coulombs
DOWN_TYPE_QUARK_CHARGE = (-1 / 3) * E  # Coulombs

# Elementary Mass
UP_TYPE_QUARK_MASS = 2.16 * eVc
DOWN_TYPE_QUARK_MASS = 4.7 * eVc
ELECTRON_MASS = 0.51099895069 * eVc

# Elementary Radius
PROTON_RADIUS = 0.84075 * fm
NEUTRON_RADIUS = 0.8 * fm
UP_TYPE_QUARK_RADIUS = 1e-4 * PROTON_RADIUS
DOWN_TYPE_QUARK_RADIUS = 1e-4 * PROTON_RADIUS
QUARK_VERTEX = 2 * UP_TYPE_QUARK_RADIUS

# Hadron Charges
PROTON_CHARGE = UP_TYPE_QUARK_CHARGE * 2 + DOWN_TYPE_QUARK_CHARGE
NEUTRON_CHARGE = UP_TYPE_QUARK_CHARGE + DOWN_TYPE_QUARK_CHARGE * 2
ELECTRON_CHARGE = -E


##CLASSES##


# Elementary Classes
class UpQuark:
    def __init__(self, position):
        self.charge = UP_TYPE_QUARK_CHARGE
        self.mass = UP_TYPE_QUARK_MASS
        self.visual = sphere(pos=position, radius=UP_TYPE_QUARK_RADIUS, color=color.red)


class DownQuark:
    def __init__(self, position):
        self.charge = DOWN_TYPE_QUARK_CHARGE
        self.mass = DOWN_TYPE_QUARK_MASS
        self.visual = sphere(
            pos=position, radius=DOWN_TYPE_QUARK_RADIUS, color=color.blue
        )


##Setup##

ProtonSphere = sphere(
    pos=vector(0, 0, 0), radius=PROTON_RADIUS, color=color.white, opacity=0.5
)
q1 = UpQuark(vector(QUARK_VERTEX, QUARK_VERTEX, QUARK_VERTEX) * qSqrt3)
q2 = UpQuark(vector(QUARK_VERTEX, -QUARK_VERTEX, -QUARK_VERTEX) * qSqrt3)
q3 = DownQuark(vector(-QUARK_VERTEX, QUARK_VERTEX, -QUARK_VERTEX) * qSqrt3)


print(q1.charge + q2.charge + q3.charge)
