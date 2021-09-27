import numpy as np
import random

class Graph:
    def __init__(self, filepath, data):
        self.filepath = filepath
        self.file = open(self.filepath, 'w')

        self.classes = np.unique(data[:,-1])
        self.data = data
        
        self._write('newgraph')
        self.calc_axis()
        self.write_classes()

    def calc_axis(self):
        xRange = (np.min(self.data[:,0]), np.max(self.data[:,0]))
        yRange = (np.min(self.data[:,1]), np.max(self.data[:,1]))

        diff = xRange[1] - xRange[0]
        buffer = 10**(np.log10(diff) - 1)


        self._write(f'xaxis min {xRange[0]-buffer} max {xRange[1]+buffer}')
        self._write(f'yaxis min {yRange[0]-buffer} max {yRange[1]+buffer}')

    def write_classes(self):
        for cls in self.classes:
            mask = self.data[:,-1] == cls
            points = self.data[mask,:-1]
            color = [random.random(), random.random(), random.random()]
            self.write_points(points, color)


    def write_points(self, points, color):
        self._write(f'newcurve color {color[0]} {color[1]} {color[2]} pts')
        for point in points:
            self._write(f'\t{point[0]} {point[1]}')


    def _write(self, str):
        self.file.write(f'{str}\n')

    def close(self):
        self.file.close()
