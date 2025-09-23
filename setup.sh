cd ..
git clone https://github.com/565353780/data-convert.git

cd data-convert
./setup.sh

cd ../sdf-generate/sdf_generate/Lib/ManifoldPlus
rm -rf build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j

cd ../../mesh_to_sdf
pip install .

pip install -U open3d tqdm trimesh scikit-image
