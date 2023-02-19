import fundamental, shape

class Ray(object):

    def __init__(self, origin, direction):

        assert fundamental.is_point(origin), \
            "Origin must be a point."
        assert fundamental.is_vector(direction), \
            "Direction must be a vector."

        self.origin     = origin
        self.direction  = direction

    @property
    def Origin(self):       return self.origin

    @property
    def Direction(self):    return self.direction

    def position(self, t):

        assert type(t) in (int, float), "Argument must be a numeric value."

        return fundamental.add_tuples(
            self.origin,
            fundamental.scalar_multiply_tuple(t, self.direction))

    def transform(self, matrix):

        assert fundamental.is_matrix(matrix)

        origin      = fundamental.matrix_tuple_multiply(matrix, self.Origin)
        direction   = fundamental.matrix_tuple_multiply(matrix, self.Direction)
        
        return Ray(origin, direction)
class Intersection(object):

    def __init__(self, t, subject):

        assert type(t) in (int, float), \
               "First argument must be a numeric value."

        self.t          = t
        self.subject    = subject

    @property
    def T(self):        return self.t

    @property
    def Subject(self):  return self.subject

def sorted_intersections(intersections):

    assert type(intersections) in (tuple, list), "Argument must be a list."

    for i in intersections: assert type(i) is Intersection, \
        "Item in iterable collection is not an intersection."

    result = []

    for i in intersections: result.append(i)

    result.sort(key = lambda x: x.T)

    return result
    
def hit(intersections):

    sortedIntersections = sorted_intersections(intersections)

    for i in sortedIntersections:
        
        if i.T >= 0: return i

    return None
