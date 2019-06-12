import numpy
import os
import sys

def calculate_distance(coords1,coords2):
    """
    This function has two arguments, the coordinates of two atoms. It returns the distance between atoms.
    """
    x_dists = coords1[0] - coords2[0]
    y_dists = coords1[1] - coords2[1]
    z_dists = coords1[2] - coords2[2]
    dists_12 = numpy.sqrt(x_dists**2 + y_dists**2 + z_dists**2)
    return dists_12

def bond_checks(distance,minimum=0,maximum=1.5):
    """
    Check a distance to see if it is a bond. Has two returns; true or false. User specifies minimum and maximum values
    for bond. Default minimum is 0, default maximum is 1.5.
    """
    if distance>minimum and distance<maximum:
        return True
    else:
        return False

geometry_file = sys.argv[1]
geometry = numpy.genfromtxt(fname=geometry_file, dtype='unicode', skip_header=2)
headers = geometry[:,0]
geometries = geometry[:,1:]
geometries = geometries.astype(numpy.float)

num_atoms=len(headers) #with functions!
for num1 in range(0,num_atoms):
    for num2 in range(0,num_atoms):
        if num1>num2:
            distances = calculate_distance(geometries[num1],geometries[num2])
            if bond_checks(distances,0,1.5) is True:
                print(F'{headers[num1]} to {headers[num2]} : {distances:.3f}')
