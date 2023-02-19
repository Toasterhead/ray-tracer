import fundamental

class PointLight(object):

    def __init__(self, position, intensity):

        assert fundamental.is_point(position),  \
            "First argument must be a point."
        assert fundamental.is_color(intensity), \
            "Second argument must be a color/vector."

        self.position   = position
        self.intensity  = intensity

    @property
    def Position(self):     return self.position

    @property
    def Intensity(self):    return self.intensity

    @Position.setter
    def Transform(self, value):
        
        assert fundamental.is_pointx(value), "Argument must be a point."
        
        self.position = value

    @Intensity.setter
    def Transform(self, value):

        assert fundamental.is_color(value), "Argument must be a color/vector."

        self.intensity = value

class Material(object):

    def __init__(
        self,
        color       = fundamental.create_vector(1, 1, 1),
        ambient     = 0.1,
        diffuse     = 0.9,
        specular    = 0.9,
        shininess   = 200.0):

        assert fundamental.is_color(color)
        assert \
            type(ambient) == float and \
            ambient >= 0.0 and ambient <= 1.0 and \
            type(diffuse) == float and \
            diffuse >= 0.0 and diffuse <= 1.0 and \
            type(specular) == float and \
            specular >= 0.0 and specular <= 1.0, \
            "The second through fourth arguments must be a float from 0 to 1."
        assert \
            type(shininess) in (int, float) and shininess > 0, \
            "The fourth argument must be a number greater than zero."

        self.color      = color
        self.ambient    = ambient
        self.diffuse    = diffuse
        self.specular   = specular
        self.shininess  = float(shininess)

def lighting(material, light, point, vEye, vNormal):

    effectiveColor = fundamental.hadamard_product(
        light.intensity,
        material.color)
    vLight = fundamental.normalized(
        fundamental.subtract_tuples(
            light.position,
            point))
    ambient = fundamental.scalar_multiply_tuple(
        material.ambient,
        effectiveColor)
    lightDotNormal = fundamental.dot_product(vLight, vNormal)

    if lightDotNormal < 0:
        diffuse     = fundamental.create_vector(0, 0, 0) #Color - Black
        specular    = fundamental.create_vector(0, 0, 0) #Color - Black
    else:
        diffuse = fundamental.scalar_multiply_tuple(
            material.diffuse * lightDotNormal,
            effectiveColor)
        vReflect = fundamental.reflect(
            fundamental.negate_tuple(vLight),
            vNormal)
        reflectDotEye = fundamental.dot_product(vReflect, vEye)

        if reflectDotEye <= 0:
            specular = fundamental.create_vector(0, 0, 0) #Color - Black
        else:
            factor = pow(reflectDotEye, material.shininess)
            specular = fundamental.scalar_multiply_tuple(
                factor,
                fundamental.scalar_multiply_tuple(
                    material.specular,
                    light.intensity))

    return fundamental.add_tuples(
        ambient,
        fundamental.add_tuples(
            diffuse,
            specular))

#Test
import math
m = Material()
position = fundamental.create_point(0, 0, 0)
vEye = fundamental.create_vector(0, 0, -1)
vNormal = fundamental.create_vector(0, 0, -1)
light = PointLight(fundamental.create_point(0, 0, 10), fundamental.create_vector(1, 1, 1))
result = lighting(m, light, position, vEye, vNormal)
