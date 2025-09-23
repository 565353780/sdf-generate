cd ..
git clone https://github.com/565353780/data-convert.git

cd data-convert
./setup.sh

sudo apt-get install -y ninja-build libxi6

pip install git+https://github.com/ashawkey/cubvh

cd ../sdf-generate/sdf_generate/Lib/ManifoldPlus
rm -rf build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j

cd ../../mesh_to_sdf
pip install .

pip install -U open3d tqdm trimesh scikit-image diso \
  argparse pysdf fpsample numpy point_cloud_utils

pip install bpy==4.0.0
pip install numpy==1.26.4
