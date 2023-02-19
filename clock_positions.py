import math, fundamental, transformation, canvas

NUM_POSITIONS = 12
CANVAS_SIZE_X = 100
CANVAS_SIZE_Y = 100
RADIUS_TO_CANVAS_RATIO = 0.25

hourPositions = []

for i in range(NUM_POSITIONS):
    
    theta = i * (math.pi / (0.5 * NUM_POSITIONS))

    #Twelve o' clock, unit length.    
    initialPosition = fundamental.create_point(0, 1, 0)
    
    matrixRotation = transformation.rotation_z(theta)
    matrixScaling = transformation.scaling(
        RADIUS_TO_CANVAS_RATIO * CANVAS_SIZE_X,
        RADIUS_TO_CANVAS_RATIO * CANVAS_SIZE_Y,
        0)
    matrixTranslation = transformation.translation(
        0.5 * CANVAS_SIZE_X,
        0.5 * CANVAS_SIZE_Y,
        0)
    
    hourPositions.append(
        fundamental.matrix_tuple_multiply(
            fundamental.matrix_multiply(
                matrixTranslation,
                fundamental.matrix_multiply(matrixScaling, matrixRotation)),
            initialPosition))

clockCanvas = canvas.Canvas(CANVAS_SIZE_X, CANVAS_SIZE_Y)

for position in hourPositions:
    clockCanvas.write_pixel(
        position[fundamental.X],
        position[fundamental.Y],
        fundamental.create_vector(1, 1, 1))

imageFile = open("clock_positions.ppm", 'w')
imageFile.writelines(clockCanvas.to_ppm())
imageFile.close()
    
