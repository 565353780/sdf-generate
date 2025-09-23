cd ..
git clone https://github.com/565353780/data-convert.git
git clone --recursive https://github.com/ashawkey/cubvh

sudo apt-get install -y ninja-build libxi6

cd data-convert
./setup.sh

cd ../cubvh
pip install . --no-build-isolation

pip install -U open3d tqdm trimesh scikit-image diso \
  argparse pysdf fpsample numpy point_cloud_utils

pip install numpy==1.26.4
pip install bpy==4.0.0 --extra-index-url https://download.blender.org/pypi/
