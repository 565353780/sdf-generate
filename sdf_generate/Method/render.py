import skimage
import numpy as np
import open3d as o3d


def toSDFMesh(sdf_data: np.ndarray) -> o3d.geometry.TriangleMesh:
    vertices, faces, normals, _ = skimage.measure.marching_cubes(sdf_data, level=0)

    sdf_mesh = o3d.geometry.TriangleMesh()

    sdf_mesh.vertices = o3d.utility.Vector3dVector(vertices)
    sdf_mesh.triangles = o3d.utility.Vector3iVector(faces)
    sdf_mesh.vertex_normals = o3d.utility.Vector3dVector(normals)

    return sdf_mesh


def toNearSurfaceSDFPcd(sdf_data: np.ndarray) -> o3d.geometry.PointCloud:
    positive_mask = sdf_data[:, 3] > 0.0
    negative_mask = ~positive_mask

    positive_points = sdf_data[positive_mask][:, :3]
    negative_points = sdf_data[negative_mask][:, :3]

    positive_colors = np.zeros_like(positive_points)
    negative_colors = np.zeros_like(negative_points)

    positive_colors[:, 0] = 1.0
    negative_colors[:, 2] = 1.0

    points = np.vstack([positive_points, negative_points])
    colors = np.vstack([positive_colors, negative_colors])

    points = negative_points
    colors = negative_colors

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    pcd.colors = o3d.utility.Vector3dVector(colors)

    return pcd
