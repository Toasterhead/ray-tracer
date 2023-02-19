import math, fundamental

def translation(x, y, z):

    assert type(x) in (float, int), "X is not a real-number value."
    assert type(y) in (float, int), "Y is not a real-number value."
    assert type(z) in (float, int), "Z is not a real-number value."

    M = 4

    translationMatrix = fundamental.create_identity_matrix(M)

    translationMatrix[0][M - 1] = x
    translationMatrix[1][M - 1] = y
    translationMatrix[2][M - 1] = z

    return translationMatrix

def scaling(x, y, z):

    assert type(x) in (float, int), "X is not a real-number value."
    assert type(y) in (float, int), "Y is not a real-number value."
    assert type(z) in (float, int), "Z is not a real-number value."

    M = 4

    scalingMatrix = fundamental.create_identity_matrix(M)

    scalingMatrix[0][0] = x
    scalingMatrix[1][1] = y
    scalingMatrix[2][2] = z

    return scalingMatrix

def rotation_x(theta):

    assert type(theta) in (float, int), \
        "The argument is not a real-number value."

    M = 4

    rotationMatrix = fundamental.create_identity_matrix(M)

    rotationMatrix[1][1] =  math.cos(theta)
    rotationMatrix[1][2] = -math.sin(theta)
    rotationMatrix[2][1] =  math.sin(theta)
    rotationMatrix[2][2] =  math.cos(theta)

    return rotationMatrix

def rotation_y(theta):

    assert type(theta) in (float, int), \
        "The argument is not a real-number value."

    M = 4

    rotationMatrix = fundamental.create_identity_matrix(M)

    rotationMatrix[0][0] =  math.cos(theta)
    rotationMatrix[0][2] =  math.sin(theta)
    rotationMatrix[2][0] = -math.sin(theta)
    rotationMatrix[2][2] =  math.cos(theta)

    return rotationMatrix

def rotation_z(theta):

    assert type(theta) in (float, int), \
        "The argument is not a real-number value."

    M = 4

    rotationMatrix = fundamental.create_identity_matrix(M)

    rotationMatrix[0][0] =  math.cos(theta)
    rotationMatrix[0][1] = -math.sin(theta)
    rotationMatrix[1][0] =  math.sin(theta)
    rotationMatrix[1][1] =  math.cos(theta)

    return rotationMatrix

def shearing(xy, xz, yx, yz, zx, zy):

    assert \
           type(xy) in (int, float) and \
           type(xz) in (int, float) and \
           type(yx) in (int, float) and \
           type(yz) in (int, float) and \
           type(zx) in (int, float) and \
           type(zy) in (int, float), \
           "At least one argument is not a real-number value."

    M = 4

    shearingMatrix = fundamental.create_identity_matrix(M)

    shearingMatrix[0][1] = xy
    shearingMatrix[0][2] = xz
    shearingMatrix[1][0] = yx
    shearingMatrix[1][2] = yz
    shearingMatrix[2][0] = zx
    shearingMatrix[2][1] = zy

    return shearingMatrix
