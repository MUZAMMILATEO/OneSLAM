import numpy as np
import argparse
from scipy.spatial.transform import Rotation as R

def quaternion_to_matrix(qx, qy, qz, qw, tx, ty, tz):
    # Convert quaternion to rotation matrix
    rot = R.from_quat([qx, qy, qz, qw])
    R_mat = rot.as_matrix()
    
    # Create 4x4 transformation matrix
    T = np.eye(4)
    T[:3, :3] = R_mat
    T[:3, 3] = [tx, ty, tz]
    return T

def convert_poses(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    out_lines = []
    counter = 0
    for line in lines:
        line = line.strip()
        if line.startswith('#') or not line:
            continue

        parts = line.split()
        frame_id = int(parts[0])
        tx, ty, tz = map(float, parts[1:4])
        qx, qy, qz, qw = map(float, parts[4:8])

        T = quaternion_to_matrix(qx, qy, qz, qw, tx, ty, tz)
        
        # if counter==0:
        #     out_lines.append(f"0 0 1")
        # else:
            # out_lines.append(f"{frame_id-1} {frame_id-1} {frame_id}")
        out_lines.append(f"{frame_id} {frame_id} {frame_id+1}")
         
        for row in T:
            out_lines.append(' '.join(f"{val:.8f}" for val in row))
        counter += 1

    with open(output_file, 'w') as f:
        f.write('\n'.join(out_lines))
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert camera poses from txt to trajectory format.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Input poses file (e.g., poses_pred.txt)")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output trajectory file (e.g., trajectory.txt)")
    
    args = parser.parse_args()
    convert_poses(args.input, args.output)