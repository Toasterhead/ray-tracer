import math

TUPLE_SIZE = 4
MAX_COLOR_VALUE = 255

X = 0
Y = 1
Z = 2
W = 3

R = X
G = Y
B = Z

deepMatrixValidationOn = True

def create_point(x, y, z):  return (x, y, z, 1)

def create_vector(x, y, z): return (x, y, z, 0)

def create_empty_matrix(m, n):

    assert type(m) == int   and type(n) == int, \
        "At least one argument is not an integer."
    assert m >= 0           and n >= 0, \
        "At least one argument is negative."

    a = []

    for i in range(m):
        row = []
        for j in range(n): row.append(0)
        a.append(row)

    return a

def create_identity_matrix(size = TUPLE_SIZE):

    assert type(size) == int, "The argument is not an integer."

    identityMatrix = create_empty_matrix(size, size)

    for i in range(size): identityMatrix[i][i] = 1

    return identityMatrix

def is_ray_tracing_tuple(item):

    if not (type(item) == tuple and len(item) == TUPLE_SIZE): return False

    for i in item:
        if not (type(i) in (int, float)): return False

    return True

def is_point(item):

    return is_ray_tracing_tuple(item) and item[len(item) - 1] == 1

def is_vector(item):

    return is_ray_tracing_tuple(item) and item[len(item) - 1] == 0

def is_color(item): return is_vector(item)

def is_matrix(item):

    if deepMatrixValidationOn: return is_matrix_deep(item)

    return is_matrix_shallow(item)                     

def is_matrix_shallow(item):

    return \
           type(item)       in (tuple, list) and \
           type(item[0])    in (tuple, list) and \
           type(item[0][0]) in (int, float)

def is_matrix_deep(item):

    #Computationally expensive. Only use for testing.

    if not type(item) in (tuple, list): return False
    
    n = 0

    if type(item[0]) in (tuple, list): n = len(item[0])
    
    for i in item:
          
        if      not type(i) in (tuple, list):   return False
        elif    not len(i) == n:                return False

        for j in i:
            if not type(j) in (int, float): return False

    return True

def floats_equal(left, right, epsilon = 0.00001):

    return abs(left - right) < epsilon

def tuples_equal(left, right):

    assert len(left) == TUPLE_SIZE and len(right) == TUPLE_SIZE, \
        "At least one argument is not a ray-tracing tuple."
        
    return \
        floats_equal(left[X], right[X]) and \
        floats_equal(left[Y], right[Y]) and \
        floats_equal(left[Z], right[Z]) and \
        floats_equal(left[W], right[W])

def matrices_equal(left, right):

    assert is_matrix(left) and is_matrix(right), \
        "At least one argument is not a matrix."

    for i in range(len(left)):
        for j in range(len(left[0])):
            if not floats_equal(left[i][j], right[i][j]): return False

    return True

def add_tuples(left, right):

    assert is_ray_tracing_tuple(left) and is_ray_tracing_tuple(right), \
        "At least one argument is not a ray-tracing tuple."
    
    return ( \
        left[X] + right[X],
        left[Y] + right[Y],
        left[Z] + right[Z],
        left[W] + right[W])

def subtract_tuples(left, right):

    assert is_ray_tracing_tuple(left) and is_ray_tracing_tuple(right), \
        "At least one argument is not a ray-tracing tuple."
    
    return ( \
        left[X] - right[X],
        left[Y] - right[Y],
        left[Z] - right[Z],
        left[W] - right[W])

def negate_tuple(a):

    assert is_ray_tracing_tuple(a), "Argument is not a ray-tracing tuple."
    
    return (-a[X], -a[Y], -a[Z], -a[W])

def scalar_multiply_tuple(scalar, a):

    assert type(scalar) == int or type(scalar) == float, \
        "The scalar must be a numerical value."
    assert is_ray_tracing_tuple(a), \
        "Argument is not a ray-tracing tuple."

    return ( \
        scalar * a[X],
        scalar * a[Y],
        scalar * a[Z],
        scalar * a[W])

def matrix_multiply(left, right):

    assert is_matrix(left) and is_matrix(right), \
        "At least one argument is not a matrix."
    assert len(left[0]) == len(right), \
        "The width of the left matrix must be equal to the height of the " + \
        "right matrix."
    
    elementsCount   = len(left[0])
    productM        = len(left)
    productN        = len(right[0])
    product         = create_empty_matrix(productM, productN)

    for i in range(productM):
        
        for j in range(productN):

            row         = left[i]
            column      = obtain_column(j, right)
            dotProduct  = 0
            
            for elementsIndex in range(elementsCount):
                dotProduct += row[elementsIndex] * column[elementsIndex]

            product[i][j] = dotProduct
                
    return product

def matrix_tuple_multiply(matrix, raytracingTuple):

    assert is_matrix(matrix), \
        "First argument must be a matrix."
    assert is_ray_tracing_tuple(raytracingTuple), \
        "Second argument must be a ray-tracing tuple."

    productMatrix   = matrix_multiply(matrix, tuple_as_matrix(raytracingTuple))
    productTuple    = []

    for i in range(len(productMatrix)):
        productTuple.append(productMatrix[i][0])

    return tuple(productTuple)

def magnitude(v):

    assert is_vector(v), "Argument is not a vector."

    return math.sqrt(pow(v[X], 2) + pow(v[Y], 2) + pow(v[Z], 2))

def normalized(v):

    assert is_vector(v), "Argument is not a vector."

    vBar = magnitude(v)

    return (v[X] / vBar, v[Y] / vBar, v[Z] / vBar, v[W] / vBar)

def dot_product(left, right):

    assert is_ray_tracing_tuple(left) and is_ray_tracing_tuple(right), \
        "At least one argument is not a ray-tracing tuple."

    return \
        left[X] * right[X] + \
        left[Y] * right[Y] + \
        left[Z] * right[Z] + \
        left[W] * right[W]

def cross_product(left, right):

    assert is_ray_tracing_tuple(left) and is_ray_tracing_tuple(right), \
        "At least one argument is not a ray-tracing tuple."

    return ( \
        (left[Y] * right[Z]) - (left[Z] * right[Y]),
        (left[Z] * right[X]) - (left[X] * right[Z]),
        (left[X] * right[Y]) - (left[Y] * right[X]),
        0)

def hadamard_product(left, right):

    assert is_ray_tracing_tuple(left) and is_ray_tracing_tuple(right), \
        "At least one argument is not a ray-tracing tuple."

    return ( \
        left[X] * right[X],
        left[Y] * right[Y],
        left[Z] * right[Z],
        left[W] * right[W])

def reflect(vIn, vNormal):

    assert is_vector(vIn) and is_vector(vNormal), \
        "At least one argument is not a vector."

    return subtract_tuples(
        vIn,
        scalar_multiply_tuple(
            2 * dot_product(vIn, vNormal),
            vNormal))

def transpose(a):

    assert is_matrix(a), "The argument is not a matrix."

    initialM = len(a)
    initialN = len(a[0])
    
    aT = create_empty_matrix(len(a[0]), len(a))

    for i in range(initialM):
        for j in range(initialN):
            aT[j][i] = a[i][j]

    return aT

def determinant(a):

    assert is_matrix(a),        "The argument is not a matrix."
    assert len(a) == len(a[0]), "The argument is not a square matrix."

    result = 0

    m = len(a)

    if m == 2:
        
        return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])
    
    else: 

        for i in range(m):
            result += a[0][i] * cofactor(a, 0, i)

    return result

def submatrix(a, removeI, removeJ):

    assert is_matrix(a), \
        "The first argument is not a matrix."
    assert type(removeI) == int and type(removeJ) == int, \
        "The second or third argument is not an integer."

    m = len(a)
    n = len(a[0])

    b = create_empty_matrix(m - 1, n - 1)

    for i in range(m):
        for j in range(n):
            if i < removeI:
                if      j < removeJ: b[i][j]            = a[i][j]
                elif    j > removeJ: b[i][j - 1]        = a[i][j]
            elif i > removeI:
                if      j < removeJ: b[i - 1][j]        = a[i][j]
                elif    j > removeJ: b[i - 1][j - 1]    = a[i][j]
    
    return b

def minor(a, minorI, minorJ):

    assert is_matrix(a), \
        "The first argument is not a matrix."
    assert type(minorI) == int and type(minorJ) == int, \
        "The second or third argument is not an integer."

    return determinant(submatrix(a, minorI, minorJ))

def cofactor(a, cofactorI, cofactorJ):

    assert is_matrix(a), \
        "The first argument is not a matrix."
    assert type(cofactorI) == int and type(cofactorJ) == int, \
        "The second or third argument is not an integer."

    minorValue = minor(a, cofactorI, cofactorJ)

    return minorValue if cofactorI % 2 == cofactorJ % 2 else -minorValue

def matrix_inverse(a):

    assert is_matrix(a),        "Argument is not a matrix."
    assert len(a) == len(a[0]), "Argument is not a square matrix."

    m = len(a)
    n = len(a[0])

    b = create_empty_matrix(m, n)

    for i in range(m):
        for j in range(n): b[i][j] = cofactor(a, i, j)

    bT = transpose(b)

    c       = create_empty_matrix(m, n)
    aDet    = determinant(a)

    for i in range(m):
        for j in range(n): c[i][j] = bT[i][j] / aDet

    return c

def obtain_column(j, a):

    assert type(j) == int and j >= 0, \
        "First argument must be a positive integer."
    assert is_matrix(a), "Second argument is not a matrix."

    column = []

    for row in a: column.append(row[j])
    
    return column

def tuple_as_matrix(raytracingTuple):

    assert len(raytracingTuple) == TUPLE_SIZE, \
        "The argument is not a ray-tracing tuple."

    #Converts a tuple to a single-column matrix.

    a = create_empty_matrix(TUPLE_SIZE, 1)

    for i in range(TUPLE_SIZE): a[i][0] = raytracingTuple[i]

    return a

def write_image(s, filename):

    assert type(s) == str and type(filename) == str

    theFile = open(filename, 'w')
    theFile.write(s)   
    theFile.close()
