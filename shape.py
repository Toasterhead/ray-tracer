import math, fundamental, ray, lighting

class Sphere(object):

    def __init__(self):

        self.origin = fundamental.create_point(0, 0, 0)
        self.transform = fundamental.create_identity_matrix()
        self.material = lighting.Material()

    @property
    def Origin(self):       return self.origin

    @property
    def Transform(self):    return self.transform
    
    @property
    def Material(self):     return self.material
    
    @Transform.setter
    def Transform(self, value):
        
        assert fundamental.is_matrix(value), "Argument must be a matrix."
        
        self.transform = value

    @Material.setter
    def Material(self, value):

        assert fundamental.is_color(value), "Argument must be a color."

        self.material = value

    def normal_at(s, worldPoint):

        assert type(s) == Sphere, \
               "First argument must be a sphere."
        assert fundamental.is_point(worldPoint), \
               "Second argument must be a point."

        objectPoint = fundamental.matrix_tuple_multiply(
            fundamental.matrix_inverse(s.transform),
            worldPoint)
        objectNormal = fundamental.subtract_tuples(
            objectPoint,
            fundamental.create_point(0, 0, 0))
        worldNormal = fundamental.matrix_tuple_multiply(
            fundamental.transpose(fundamental.matrix_inverse(s.transform)),
            objectNormal)
        worldNormal = fundamental.create_vector(
            worldNormal[fundamental.X],
            worldNormal[fundamental.Y],
            worldNormal[fundamental.Z])

        return fundamental.normalized(worldNormal)

def intersect_sphere(s, r):

    assert type(s) == Sphere,   "First argument must be a sphere."
    assert type(r) == ray.Ray,  "Argument must be a ray."

    rTranformed = r.transform(fundamental.matrix_inverse(s.transform))

    sphereToRay = fundamental.subtract_tuples(rTranformed.origin, s.origin)

    a = fundamental.dot_product(rTranformed.Direction, rTranformed.Direction)
    b = 2 * fundamental.dot_product(rTranformed.Direction, sphereToRay)
    c = fundamental.dot_product(sphereToRay, sphereToRay) - 1

    discriminant = pow(b, 2) - (4 * a * c)

    if discriminant < 0: return ()

    return (
        ray.Intersection((-b - math.sqrt(discriminant)) / (2 * a), s),
        ray.Intersection((-b + math.sqrt(discriminant)) / (2 * a), s))
