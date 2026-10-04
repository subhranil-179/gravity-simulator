import uuid
import pygame

from .scale import scale_down
from .utils import calc_g_force

class Space:
    def __init__(self, bodies):
        self.bodies = bodies

    def render(self, screen, is_scale_down):
        for body in self.bodies:
            body.render(screen, is_scale_down)
            body.draw_path(screen)

    def update(self, dt):
        for body in self.bodies:
            print(f"BODY: {body}")
            bodies = list(self.bodies)
            bodies.remove(body)
            print(f"BODIES: {bodies}")
            body.calculate_forces(bodies, dt)

        for body in self.bodies:
            body.velocity = body.velocity + (body.acceleration * dt)
            print(f"VELOCITY: {body.velocity}")

        for body in self.bodies:
            body.pos = body.pos + (body.velocity * dt)
            body.path.append(body.pos.copy())
            print(f"POSITION: {body.pos}")

class Body:
    def __init__(self, name, radius, mass, color, coordinates = (0, 0), velocity = (0, 0), acceleration = (0, 0)):
        self.id = uuid.uuid4()
        self.name = name
        self.pos = pygame.Vector2(coordinates)
        self.velocity = pygame.Vector2(velocity)
        self.acceleration = pygame.Vector2(acceleration)
        self.color = color
        self.radius = radius
        self.mass = mass
        self.path = []

    def render(self, screen, is_scale_down):
        pos = scale_down(self.pos) if is_scale_down else self.pos
        pygame.draw.circle(screen, self.color, pos, self.radius)

    def draw_path(self, screen):
        if len(self.path) > 1:
            pygame.draw.aalines(screen, self.color, False, self.path)

    def calculate_forces(self, bodies, dt):
        net_force = pygame.Vector2(0, 0)
        for body in bodies:
            r = self.pos.distance_to(body.pos)
            f_magnitude = calc_g_force(self.mass, body.mass, r)
            direction = body.pos - self.pos
            direction = direction.normalize()
            force = direction * f_magnitude
            net_force += force
            print(f"FORCE [{body}]: {force}")
        self.acceleration = net_force / self.mass
        print(f"ACCELERATION: {self.acceleration}")
        print("NET FORCE:", net_force)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
