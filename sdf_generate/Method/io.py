import numpy as np

def load_obj(path):
    vertices, normals, face_vertices_indcies, face_normal_indices = [], [], [], []
    with open(path, mode='r') as f:
        for line in f.readlines():
            splited_text = line.split()
            if len(splited_text) == 0:
                continue
            if splited_text[0] == 'v':
                vertices.append([float(splited_text[1]), float(splited_text[2]), float(splited_text[3])])
            elif splited_text[0] == 'vn':
                normals.append([float(splited_text[1]), float(splited_text[2]), float(splited_text[3])])
            elif splited_text[0] == 'f':
                if "//" in splited_text[1]:
                    face_vertices_indcies.append(
                        [int(splited_text[1].split('//')[0]) - 1, int(splited_text[2].split('//')[0]) - 1,
                         int(splited_text[3].split('//')[0]) - 1])
                    face_normal_indices.append(
                        [int(splited_text[1].split('//')[1]) - 1, int(splited_text[2].split('//')[1]) - 1,
                         int(splited_text[3].split('//')[1]) - 1])
                elif "/" in splited_text[1]:
                    face_vertices_indcies.append(
                        [int(splited_text[1].split('/')[0]) - 1, int(splited_text[2].split('/')[0]) - 1,
                         int(splited_text[3].split('/')[0]) - 1])
                    face_normal_indices.append(
                        [int(splited_text[1].split('/')[1]) - 1, int(splited_text[2].split('/')[1]) - 1,
                         int(splited_text[3].split('/')[1]) - 1])
                else:  # only face
                    face_vertices_indcies.append(
                        [int(splited_text[1]) - 1, int(splited_text[2]) - 1, int(splited_text[3]) - 1])

        return np.array(vertices), np.array(normals), np.array(face_vertices_indcies), np.array(face_normal_indices)


def save_obj(path, vertices_arr, faces_arr):
    print("Writing the mesh.....")
    f = open(path, 'w')

    for i in range(vertices_arr.shape[0]):
        f.write(f'v {vertices_arr[i][0]} {vertices_arr[i][1]} {vertices_arr[i][2]}\n')

    for i in range(faces_arr.shape[0]):
        f.write(f'f {faces_arr[i][0] + 1} {faces_arr[i][1] + 1} {faces_arr[i][2] + 1}\n')

    f.close()
    print("Done Writing the mesh.....")


