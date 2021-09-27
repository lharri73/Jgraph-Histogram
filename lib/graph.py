import numpy as np
import random

class HistBar:
    """
    Class used to represent a single histogram bar. The transpose option 
    is used to plot the x-axis histogram.
    """
    def __init__(self, start, height, left, right, color, transpose=False):
        self.height = height
        self.start = start
        self.left = left
        self.right = right
        self.color = color
        self.transpose = transpose

    def __repr__(self):
        prefix = f"newline poly pcfill {self.color[0]:9.4f} {self.color[1]:9.4f} {self.color[2]:9.4f} "\
            f"color 0 0 0"
        if self.transpose:
            pts = f"\t\tpts {self.start:9.4f} {self.left:9.4f}  {self.height:9.4f} {self.left:9.4f}  {self.height:9.4f} {self.right:9.4f}  {self.start:9.4f} {self.right:9.4f}"
        else:
            pts = f"\t\tpts {self.left:9.4f} {self.start:9.4f}  {self.left:9.4f} {self.height:9.4f}  {self.right:9.4f} {self.height:9.4f}  {self.right:9.4f} {self.start:9.4f}"
        return f"{prefix}{pts}"

class Graph:
    def __init__(self, filepath, data, nbins):
        self.filepath = filepath
        self.file = open(self.filepath, 'w')
        self.nbins = nbins

        self.classes = np.unique(data[:,-1])
        self.data = data
        self.cls_colors = []

        self._write('newgraph')
        self._write('legend left')
        xRange, yRange = self.calc_axis()
        self.write_classes()
        self.create_histograms(xRange, yRange)

    def calc_axis(self):
        xRange = (np.min(self.data[:,0]), np.max(self.data[:,0]))
        yRange = (np.min(self.data[:,1]), np.max(self.data[:,1]))

        diff = xRange[1] - xRange[0]
        buffer = 10**(np.log10(diff) - 1)

        self._write(f'xaxis min {xRange[0]-buffer:.4f} max {xRange[1]+buffer:.4f} size 3')
        self._write(f'yaxis min {yRange[0]-buffer:.4f} max {yRange[1]+buffer:.4f}\n size 3')

        return xRange, yRange

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
                self._write(f'\t{point[0]:20.4f} {point[1]:20.4f}')

    def create_histograms(self, xRange, yRange):
        self._write('\n(* x histogram *)')
        self._write('copygraph')

        self._write('\ty_translate 3.25')
        self._write('\txaxis hash 0 mhash 0')
        tmp = " "*30 ## placeholder text. the max value should be no longer than 30 chars
        self.file.write("\tyaxis size 1.5 min 0 max ")
        xaxisLoc = self.file.tell()
        self._write(tmp)

        maxY = self.write_hist(xRange, axis=0)

        ## y histogram
        self._write('\n(* y histogram *)')
        self._write('copygraph 0')

        self._write('\tx_translate 3.25 y_translate 0')
        self._write('\tyaxis hash 0 mhash 0')
        tmp = " "*30
        self.file.write("\txaxis size 1.5 min 0 max ")
        yaxisLoc = self.file.tell()
        self._write(tmp)
        maxX = self.write_hist(yRange, axis=1)

        self.fix_axis(xaxisLoc, max(maxY, maxX))
        self.fix_axis(yaxisLoc, max(maxX, maxY))

    def write_hist(self, xRange, axis):
        bins = [0]*self.nbins
        for i, cls in enumerate(self.classes): ## i and cls should be the same
            mask = self.data[:,-1] == cls
            xhist, bounds = np.histogram(self.data[mask,axis], bins=self.nbins, range=(xRange[0], xRange[1]))
            for j, val in enumerate(xhist):
                bar = HistBar(bins[j], val+bins[j], bounds[j], bounds[j+1], self.cls_colors[i], transpose=axis)
                self._write(f"\t{str(bar)}")
                bins[j] += val
        maxVal = np.max(np.array(bins))
        self._write("")

        return maxVal

    def fix_axis(self, topAxis, maxY):
        self.file.seek(topAxis, 0)
        self.file.write(f"{maxY:<30d}")

    def _write(self, str):
        self.file.write(f'{str}\n')

    def close(self):
        self.file.close()
