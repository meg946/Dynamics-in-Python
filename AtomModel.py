from vpython import *
import random


##CONSTANTS##
# Unit Conversions
eVc = 1.7826619216279e-36  # eV/c^2 convert to kilogram
fm = 1e-15  # femtometre to meter
qSqrt3 = 1 / sqrt(3)  # just to make it easier
dt = 1 / 60  # time step


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
UP_TYPE_QUARK_RADIUS = 1e-2 * PROTON_RADIUS
DOWN_TYPE_QUARK_RADIUS = 1e-2 * PROTON_RADIUS
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
        self.spin = 1 / 2
        self.visual = sphere(pos=position, radius=UP_TYPE_QUARK_RADIUS, color=color.red)


class DownQuark:
    def __init__(self, position):
        self.charge = DOWN_TYPE_QUARK_CHARGE
        self.mass = DOWN_TYPE_QUARK_MASS
        self.spin = 1 / 2
        self.visual = sphere(
            pos=position, radius=DOWN_TYPE_QUARK_RADIUS, color=color.blue
        )


class Proton:
    def __init__(self, position):
        self.pos = position
        self.radius = PROTON_RADIUS

        offset_1 = vector(QUARK_VERTEX, QUARK_VERTEX, QUARK_VERTEX) * qSqrt3
        offset_2 = vector(QUARK_VERTEX, -QUARK_VERTEX, -QUARK_VERTEX) * qSqrt3
        offset_3 = vector(-QUARK_VERTEX, QUARK_VERTEX, -QUARK_VERTEX) * qSqrt3

        self.quarks = [
            UpQuark(position=self.pos + offset_1),
            UpQuark(position=self.pos + offset_2),
            DownQuark(position=self.pos + offset_3),
        ]

        self.vel = vector(0, 0, 0)
        self.accel = vector(0, 0, 0)
        self.force = vector(0, 0, 0)
        self.mass = sum(q.mass for q in self.quarks)

        self.visual = sphere(
            pos=self.pos, radius=self.radius, color=color.red, opacity=0.3
        )

    def get_total_charge(self):
        return sum(q.charge for q in self.quarks)

    def update(self):
        self.accel = self.force / self.mass
        self.vel += self.accel * dt
        displacement = self.vel * dt
        self.pos += displacement
        self.visual.pos = self.pos

        for q in self.quarks:
            q.visual.pos += displacement

        self.force = vector(0, 0, 0)


class Neutron:
    def __init__(self, position):
        self.pos = position
        self.radius = PROTON_RADIUS

        offset_1 = vector(QUARK_VERTEX, QUARK_VERTEX, QUARK_VERTEX) * qSqrt3
        offset_2 = vector(QUARK_VERTEX, -QUARK_VERTEX, -QUARK_VERTEX) * qSqrt3
        offset_3 = vector(-QUARK_VERTEX, QUARK_VERTEX, -QUARK_VERTEX) * qSqrt3

        self.quarks = [
            UpQuark(position=self.pos + offset_1),
            DownQuark(position=self.pos + offset_2),
            DownQuark(position=self.pos + offset_3),
        ]

        self.vel = vector(0, 0, 0)
        self.accel = vector(0, 0, 0)
        self.force = vector(0, 0, 0)
        self.mass = sum(q.mass for q in self.quarks)

        self.visual = sphere(
            pos=self.pos, radius=self.radius, color=color.white, opacity=0.3
        )

    def get_total_charge(self):
        return sum(q.charge for q in self.quarks)

    def update(self):
        self.accel = self.force / self.mass
        self.vel += self.accel * dt
        displacement = self.vel * dt
        self.pos += displacement
        self.visual.pos = self.pos

        for q in self.quarks:
            q.visual.pos += displacement

        self.force = vector(0, 0, 0)


##Setup##

# Canvas
scene.width = 1200
scene.height = 1200
scene.background = color.white

# Objects

p1 = Proton(position=vector(2 * fm, 0, 0))
n1 = Neutron(position=vector(0, 0, 0))

objectList = [p1, n1]

while True:
    rate(60)
    for obj in objectList:
        obj.update()
