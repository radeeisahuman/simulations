gravity = 9.81

def calculate_velocity(acceleration: float, time: float):
    return acceleration * time

def distance_travelled(velocity: float, time: float):
    return velocity * time

def kinetic_energy(velocity: float, mass: float):
    return (mass * (velocity ** 2))/2
