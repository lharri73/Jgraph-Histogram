import numpy as np
from argparse import ArgumentParser


def main():
    for i in range(args.num_classes):
        points = np.random.normal([args.mean_x, args.mean_y], [args.std_x, args.std_y], size=(args.points_per_class, 2))
        cur_cls = np.full((args.points_per_class, 1), i)
        points = np.hstack((points, cur_cls))
        with open(args.file_location, "a") as f:
            np.savetxt(f, points, fmt="%.5f %.5f %d")


if __name__ == "__main__":
    parser = ArgumentParser('data_maker.py')
    parser.add_argument('file_location')
    parser.add_argument('num_classes', type=int)
    parser.add_argument('points_per_class',type=int)
    parser.add_argument('--mean_x', type=float, default=0.0)
    parser.add_argument('--mean_y', type=float, default=0.0)
    parser.add_argument('--std_x', type=float, default=1.0)
    parser.add_argument('--std_y', type=float, default=1.0)

    args = parser.parse_args()
    main()
