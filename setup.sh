cd ../sdf-generate/sdf_generate/Lib/Manifold
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j

cd ../../mesh_to_sdf
pip install .

pip install -U open3d tqdm
