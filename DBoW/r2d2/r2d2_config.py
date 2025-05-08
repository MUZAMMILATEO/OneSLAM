# import argparse

# def init_configs():
#     parser = argparse.ArgumentParser("Extract keypoints for a given image")
#     parser.add_argument("--model", type=str, help='model path', default='./DBoW/r2d2/models/faster2d2_WASF_N16.pt')
#     parser.add_argument("--images", type=str, nargs='+', help='images / list')
#     parser.add_argument("--tag", type=str, default='r2d2', help='output file tag')

#     parser.add_argument("--top-k", type=int, default=300, help='number of keypoints')

#     parser.add_argument("--scale-f", type=float, default=2**0.25)
#     parser.add_argument("--min-size", type=int, default=256)
#     parser.add_argument("--max-size", type=int, default=1024)
#     parser.add_argument("--min-scale", type=float, default=0)
#     parser.add_argument("--max-scale", type=float, default=1)

#     parser.add_argument("--reliability-thr", type=float, default=0.7)
#     parser.add_argument("--repeatability-thr", type=float, default=0.7)

#     parser.add_argument("--gpu", type=int, nargs='+', default=[0], help='use -1 for CPU')
#     args = parser.parse_args()
#     return args