import numpy as np
import random

class Graph:
    def __init__(self, filepath, data):
        self.filepath = filepath
        self.file = open(self.filepath, 'w')

        self.classes = np.unique(data[:,-1])
        self.data = data
        self.cls_colors = []

        self._write('newgraph')
        self.calc_axis()
        self.write_classes()

    def calc_axis(self):
        xRange = (np.min(self.data[:,0]), np.max(self.data[:,0]))
        yRange = (np.min(self.data[:,1]), np.max(self.data[:,1]))

        diff = xRange[1] - xRange[0]
        buffer = 10**(np.log10(diff) - 1)

        self._write(f'xaxis min {xRange[0]-buffer:.4f} max {xRange[1]+buffer:.4f}')
        self._write(f'yaxis min {yRange[0]-buffer:.4f} max {yRange[1]+buffer:.4f}\n')

    def write_classes(self):
        for cls in self.classes:
            mask = self.data[:,-1] == cls
            points = self.data[mask,:-1]
            color = [random.random(), random.random(), random.random()]
            self.cls_colors.append(color)

            self._write(f'(* cls = {int(cls)} *)')
            self._write('newcurve')
            self._write(f'\tcolor {color[0]:.3f} {color[1]:.3f} {color[2]:.3f}')
            self._write('\tmarktype circle')
            self._write(f'\tlabel : class = {int(cls):d}')
            self._write('\tpts')
            for point in points:
                self._write(f'\t{point[0]:+20.4f} {point[1]:+20.4f}')


    def _write(self, str):
        self.file.write(f'{str}\n')

    def close(self):
        self.file.close()
