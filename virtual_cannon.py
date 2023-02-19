import fundamental, canvas

TUPLE_SIZE = fundamental.TUPLE_SIZE

class Projectile(object):

    def __init__(self, position, velocity):

        assert  fundamental.is_point(position) and \
                fundamental.is_vector(velocity)

        self.position = position
        self.velocity = velocity

    @property
    def Position(self): return self.position
    
    @property
    def Velocity(self): return self.velocity

class Environment(object):

    def __init__(self, gravity, wind):

        assert  fundamental.is_vector(gravity) and \
                fundamental.is_vector(wind)

        self.gravity    = gravity
        self.wind       = wind

    @property
    def Gravity(self):  return self.gravity

    @property
    def Wind(self):     return self.wind
        
def tick(environment, projectile):

    position = fundamental.add_tuples(projectile.Position, projectile.Velocity)
    velocity = fundamental.add_tuples(fundamental.add_tuples(
        projectile.Velocity, environment.Gravity), environment.Wind)

    return Projectile(position, velocity)

def test(): #
    
    start = fundamental.create_point(0, 1, 0)
    velocity = fundamental.scalar_multiply_tuple(
        11.25,
        fundamental.normalized(fundamental.create_vector(1, 1.8, 0)))
    p = Projectile(start, velocity)
    gravity = fundamental.create_vector(0, -0.1, 0)
    wind = fundamental.create_vector(-0.01, 0, 0)
    e = Environment(gravity, wind)
    c = canvas.Canvas(900, 550)
    red = (1, 0, 0, 0)
    for i in range(c.Width):
        c.write_pixel(p.Position[0], c.Height - p.Position[1], red)
        p = tick(e, p)
        print("(" + str(p.Position[0]) + ", " + str(p.Position[1]) + ")")
    fundamental.write_image(c.to_ppm(), "cannon_trajectory.ppm")
