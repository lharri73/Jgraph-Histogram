from lib.graph import Graph
import sys
from argparse import ArgumentParser
import numpy as np

def main():
    data = np.loadtxt(args.file_location, dtype=np.float32)

    garph = Graph(args.graph_location, data, args.nbins)
    garph.close()
    

if __name__ == "__main__":
    parser = ArgumentParser('main.py')
    parser.add_argument('file_location', help='location of file to load')
    parser.add_argument('graph_location', help='location of the graph to write')
    parser.add_argument('--nbins', help="number of histogram bins", type=int, default=10)

    args = parser.parse_args()
    main()
