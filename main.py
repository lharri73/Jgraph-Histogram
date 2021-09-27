from graph import Graph
import sys
from argparse import ArgumentParser
import numpy as np

def main():
    data = np.loadtxt(args.file_location, dtype=np.float32)
    classes = np.unique(data[:,-1]) ## list of all classes in dataset

    garph = Graph(args.graph_location, data)
    garph.close()

    

if __name__ == "__main__":
    parser = ArgumentParser('main.py')
    parser.add_argument('file_location', help='location of file to load')
    parser.add_argument('graph_location', help='location of the graph to write')

    args = parser.parse_args()
    main()
