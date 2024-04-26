if [ "$(uname)" == "Darwin" ]; then
	pip install open3d==0.15.1
elif [ "$(uname)" = "Linux" ]; then
	pip install -U open3d
fi

cd ../sdf-generate/sdf_generate/Lib/Manifold
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j

cd ../../mesh_to_sdf
pip install .

pip install -U tqdm trimesh scikit-image
