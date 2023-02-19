import fundamental

TUPLE_SIZE = fundamental.TUPLE_SIZE
MAX_COLOR_VALUE = fundamental.MAX_COLOR_VALUE

R = fundamental.R
G = fundamental.G
B = fundamental.B

class Canvas(object):

    def __init__(self, width, height):

        assert type(width)  == int and width    > 0, \
            "Width must be a positive integer."
        assert type(height) == int and height   > 0, \
            "Height must be a positive integer."

        self.width  = width
        self.height = height

        self.pixels = []

        for columnIndex in range(width):
            column = []
            for rowIndex in range(height):
                column.append((0, 0, 0, 0))
            self.pixels.append(column)

    @property
    def Width(self):    return self.width

    @property
    def Height(self):   return self.height

    def write_pixel(self, x, y, color):

        assert type(x) in (int, float), "X position must be a numeric value."
        assert type(y) in (int, float), "Y position must be a numeric value."
        assert fundamental.is_ray_tracing_tuple(color)
        
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            
            self.pixels[int(x)][int(y)] = color

    def pixel_at(self, x, y):

        assert type(x) == int and x >= 0 and x < self.width, \
            "X position must be a positive integer within the canvas size."
        assert type(y) == int and y >= 0 and y < self.height, \
            "Y position must be a positive integer within the canvas size."

        return self.pixels[x][y]

    def to_ppm(self):

        s = "P3\n" + \
            str(self.width) + " " + str(self.height) + "\n" + \
            str(MAX_COLOR_VALUE) + "\n"

        for i in range(self.height):
            
            for j in range(self.width):
                
                isEndOfLine = (i * self.height + j + 1) % 20 == 0

                r = self.pixels[j][i][R] * MAX_COLOR_VALUE
                g = self.pixels[j][i][G] * MAX_COLOR_VALUE
                b = self.pixels[j][i][B] * MAX_COLOR_VALUE

                r = r if r <= MAX_COLOR_VALUE else MAX_COLOR_VALUE
                g = g if g <= MAX_COLOR_VALUE else MAX_COLOR_VALUE
                b = b if b <= MAX_COLOR_VALUE else MAX_COLOR_VALUE

                r = r if r >= 0 else 0
                g = g if g >= 0 else 0
                b = b if b >= 0 else 0

                r = int(r + 0.5) #Round to nearest integer.
                g = int(g + 0.5)
                b = int(b + 0.5)
                
                s += \
                  str(r) + " " + \
                  str(g) + " " + \
                  str(b) + ("\n" if isEndOfLine else " ")

        if s[len(s) - 1] == " ": s = s[:len(s) - 1] + "\n"
        
        return s
