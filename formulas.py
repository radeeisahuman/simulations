gravity = 98.1

def calculate_velocity(time: float):
    return gravity * time

def distance_travelled(velocity: float, time: float):
    return velocity * time

def kinetic_energy(velocity: float, mass: float):
    return (mass * (velocity ** 2))/2
