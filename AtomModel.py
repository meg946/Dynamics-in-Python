from vpython import *
import random
import numpy as np



##CONSTANTS##
# Unit Conversions
eVc = 1.7826619216279e-36  # eV/c^2 convert to kilogram
fm = 1e-15  # femtometre to meter
qSqrt3 = 1 / sqrt(3)  # just to make it easier
dt = 1e-5  # time step

#Strong force (its springs)
Q_CENTER = 1e-28
Q_REPEL = 1e-43
N_CENTER = 1e-27
N_REPEL = 1e-39

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
QUARK_AVERAGE_RADIUS = (UP_TYPE_QUARK_RADIUS+DOWN_TYPE_QUARK_RADIUS) / 2

ELECTRON_RADIUS = UP_TYPE_QUARK_RADIUS * 300 #just to make them visible

QUARK_VERTEX = 2 * UP_TYPE_QUARK_RADIUS
HADRON_VERTEX = 2 * ((PROTON_RADIUS + NEUTRON_RADIUS) / 2)

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
        self.pos = position
        self.visual = sphere(pos=self.pos, radius=UP_TYPE_QUARK_RADIUS, color=color.red)

        self.vel = vector(0, 0, 0)
        self.accel = vector(0, 0, 0)
        self.force = vector(0, 0, 0)


    
    def update(self, parent_displacement=vector(0,0,0)):
        self.accel = self.force / self.mass
        self.vel += self.accel * dt
        displacement = self.vel * dt + parent_displacement
        self.pos += displacement
        self.visual.pos = self.pos

        self.force = vector(0, 0, 0)


class DownQuark:
    def __init__(self, position):
        self.charge = DOWN_TYPE_QUARK_CHARGE
        self.mass = DOWN_TYPE_QUARK_MASS
        self.spin = 1 / 2
        self.pos = position

        self.visual = sphere(pos=self.pos, radius=DOWN_TYPE_QUARK_RADIUS, color=color.blue)


        self.vel = vector(0, 0, 0)
        self.accel = vector(0, 0, 0)
        self.force = vector(0, 0, 0)
    
    def update(self, parent_displacement=vector(0,0,0)):
        self.accel = self.force / self.mass
        self.vel += self.accel * dt
        displacement = self.vel * dt + parent_displacement
        self.pos += displacement
        self.visual.pos = self.pos

        self.force = vector(0, 0, 0)


class Electron:
    def __init__(self, position,shell=1):
        self.charge = ELECTRON_CHARGE
        self.mass = ELECTRON_MASS
        self.spin = 1 / 2
        self.pos = position
        self.shell = shell
        self.energy = -13.6/(self.shell**2)         #energy is in electron Volts

        self.visual = sphere(pos=self.pos, radius = ELECTRON_RADIUS, color = color.yellow, opacity=0.3)

        self.vel = vector(0, 0, 0)
        self.accel = vector(0, 0, 0)
        self.force = vector(0, 0, 0)
    
    def 

    def update(self, parent_displacement=vector(0,0,0)):
        self.accel = self.force / self.mass
        self.vel += self.accel * dt
        displacement = self.vel * dt + parent_displacement
        self.pos += displacement
        self.visual.pos = self.pos

        self.force = vector(0, 0, 0)


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

        self.visual = sphere(pos=self.pos, radius=self.radius, color=color.red, opacity=0.3)

    def calculate_QCD(self):
        for q in self.quarks:
            q.update()
            
        quarks = self.quarks

        for i in range(len(quarks)):
            q1 = quarks[i]
            r_center = q1.pos - self.pos
            q1.force += -Q_CENTER * r_center

            for j in range(i + 1, len(quarks)):
                q2 = quarks[j]
                r_vec = q1.pos - q2.pos
                dist = mag(r_vec)

                min_dist = 2 * QUARK_AVERAGE_RADIUS

                if 0 < dist < min_dist:

                    overlap = min_dist - dist

                    f_mag = Q_REPEL * (overlap / min_dist)**2
                    repel_force = norm(r_vec) * f_mag

                    q1.force += repel_force
                    q2.force -= repel_force


    def get_total_charge(self):
        return sum(q.charge for q in self.quarks)
    

    def update(self, parent_displacement=vector(0,0,0)):
        self.calculate_QCD()
        
        self.vel *= 0.85

        self.accel = self.force / self.mass
        self.vel += self.accel * dt
        displacement = self.vel * dt + parent_displacement
        self.pos += displacement
        self.visual.pos = self.pos

        for q in self.quarks:
            q.update(displacement)

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

        self.visual = sphere(pos=self.pos, radius=self.radius, color=color.white, opacity=0.3)

    def calculate_QCD(self):
        for q in self.quarks:
            q.update()
            
        quarks = self.quarks

        for i in range(len(quarks)):
            q1 = quarks[i]
            r_center = q1.pos - self.pos
            q1.force += -Q_CENTER * r_center

            for j in range(i + 1, len(quarks)):
                q2 = quarks[j]
                r_vec = q1.pos - q2.pos
                dist = mag(r_vec)

                min_dist = 2 * QUARK_AVERAGE_RADIUS

                if 0 < dist < min_dist:

                    overlap = min_dist - dist

                    f_mag = Q_REPEL * (overlap / min_dist)**2
                    repel_force = norm(r_vec) * f_mag

                    q1.force += repel_force
                    q2.force -= repel_force

    def get_total_charge(self):
        return sum(q.charge for q in self.quarks)

    def update(self, parent_displacement=vector(0,0,0)):
        self.calculate_QCD()
        

        self.vel *= 0.85

        self.accel = self.force / self.mass
        self.vel += self.accel * dt
        displacement = self.vel * dt + parent_displacement
        self.pos += displacement
        self.visual.pos = self.pos

        for q in self.quarks:
            q.update(displacement)

        self.force = vector(0, 0, 0)


class Atom:
    def __init__(self, position, atomic_number=2):
        self.pos = position
        self.radius = 0
        self.charge = 0

        self.neutrons = []

        self.protons = []

        for _ in range(atomic_number):
            jitter_n = vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)) * fm * 0.1
            self.neutrons.append(Neutron(position=self.pos + jitter_n))
            
            jitter_p = vector(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)) * fm * 0.1
            self.protons.append(Proton(position=self.pos + jitter_p))

        for p in self.protons:
            self.radius += p.radius / 3
            self.charge += p.get_total_charge()

        for n in self.neutrons:
            self.radius += n.radius / 3


        offset_1 = vector(HADRON_VERTEX, HADRON_VERTEX, HADRON_VERTEX) * qSqrt3
        offset_2 = vector(HADRON_VERTEX, -HADRON_VERTEX, -HADRON_VERTEX) * qSqrt3
        offset_3 = vector(-HADRON_VERTEX, HADRON_VERTEX, -HADRON_VERTEX) * qSqrt3
        
        offset_electron_mag = (15 * (1 + self.radius*1e13)**3) * HADRON_VERTEX #shell distance

        self.electrons = []

        #electron shell calculation
        for i in range(atomic_number):          
            n = 1
            electronCapacity = 2 * (n**2)
            count = i + 1

            while count > electronCapacity:
                count -= electronCapacity
                n += 1
                electronCapacity = 2 * (n**2)

            shell_radius = (n**2) * offset_electron_mag

            theta = random.uniform(0,2 * pi)
            phi = acos(random.uniform(-1,1))

            offset_x = shell_radius * sin(phi) * cos(theta)
            offset_y = shell_radius * sin(phi) * sin(theta)
            offset_z = shell_radius * cos(phi)

            electron_shell_pos = self.pos + vector(offset_x, offset_y, offset_z)

            electron = Electron(position=electron_shell_pos,shell=n)

            self.electrons += [electron]

        self.vel = vector(0, 0, 0)
        self.accel = vector(0, 0, 0)
        self.force = vector(0, 0, 0)
        self.mass = sum(n.mass for n in self.neutrons) + sum(p.mass for p in self.protons)

        self.visual = sphere(pos=self.pos, radius=self.radius, color=color.white, opacity=0.0)
    
    def calculate_nucleon_forces(self):
        nucleons = self.protons + self.neutrons

        for i in range(len(nucleons)):
            n1 = nucleons[i]
            r_center = n1.pos - self.pos
            n1.force += -N_CENTER * r_center

            for j in range(i + 1, len(nucleons)):
                n2 = nucleons[j]
                r_vec = n1.pos - n2.pos
                dist = mag(r_vec)

                min_dist = 2 * PROTON_RADIUS

                if 0 < dist < min_dist:

                    overlap = min_dist - dist

                    f_mag = N_REPEL * (overlap / min_dist)**2
                    repel_force = norm(r_vec) * f_mag

                    n1.force += repel_force
                    n2.force -= repel_force

    def update(self):

        self.calculate_nucleon_forces()

        self.accel = self.force / self.mass
        self.vel += self.accel * dt
        displacement = self.vel * dt
        self.pos += displacement
        self.visual.pos = self.pos

        for p in self.protons:
            p.update(displacement)

        for n in self.neutrons:
            n.update(displacement)

        for e in self.electrons:
            e.update(displacement)
        
        self.force = vector(0, 0, 0)

##FUNCTIONS##


##Setup##

# Canvas

scene.width = 1000
scene.height = 1100
scene.background = color.black

# Objects


he = Atom(position=vector(0,0,0), atomic_number=8)
objectList = [he]

print(he.charge)

# Updates

while True:
    rate(60)
    for obj in objectList:
        obj.update()
#    scene.camera.follow(He.visual)

