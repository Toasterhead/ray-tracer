import math, fundamental, ray, transformation, shape, lighting, canvas

rayOrigin = fundamental.create_point(0, 0, -5)
wallZ = 10
wallSize = 7

canvasSize = 100z #In pixels.
pixelSize = wallSize / canvasSize
halfWallSize = wallSize / 2

theCanvas = canvas.Canvas(canvasSize, canvasSize)
theColor = (1, 0, 0, 0) #Color - Red
theSphere = shape.Sphere()

theSphere.Material.color = fundamental.create_vector(1.0, 0.2, 1.0)
light = lighting.PointLight(
    fundamental.create_point(-10, 10, -10),
    fundamental.create_vector(1, 1, 1)) #Color - White

#theSphere.transform = transformation.scaling(1, 0.5, 1) #...! User setter instead.
#theSphere.transform = transformation.scaling(0.5, 1, 1)
#theSphere.transform = fundamental.matrix_multiply(
#    transformation.rotation_z(math.pi / 4.0),
#    transformation.scaling(0.5, 1, 1))
#theSphere.transform = fundamental.matrix_multiply(
#    transformation.shearing(1, 0, 0, 0, 0, 0),
#    transformation.scaling(0.5, 1, 1))

for y in range(canvasSize):

    worldY = halfWallSize - pixelSize * y

    for x in range(canvasSize):

        worldX = -halfWallSize  + pixelSize * x
        position = fundamental.create_point(worldX, worldY, wallZ)
        r = ray.Ray(
            rayOrigin,
            fundamental.normalized(fundamental.subtract_tuples(
                position,
                rayOrigin)))
        xs = shape.intersect_sphere(theSphere, r)
        rHit = ray.hit(xs)
        
        if rHit != None:
            point = r.position(rHit.T)
            normal = shape.Sphere.normal_at(rHit.Subject, point)
            eye = fundamental.negate_tuple(r.Direction)
            theColor = lighting.lighting(
                rHit.Subject.material,
                light,
                point,
                eye,
                normal)
            theCanvas.write_pixel(x, y, theColor)

    print("Determing pixel colors (" + str(y) + " of " + str(canvasSize) + " lines complete)...")

print("Writing to canvas...")
print(theCanvas.to_ppm())

