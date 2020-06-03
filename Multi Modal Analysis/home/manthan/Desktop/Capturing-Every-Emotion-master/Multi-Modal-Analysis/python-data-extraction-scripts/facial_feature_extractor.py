'''
Script to run OpenFace Toolkit on every video in the dataset
'''

import os
from os.path import exists, join, basename, splitext
#installations
git_repo_url = 'https://github.com/TadasBaltrusaitis/OpenFace.git'
project_name = splitext(basename(git_repo_url))[0]
# clone openface
!git clone -q --depth 1 $git_repo_url
!cd OpenFace && bash ./download_models.sh && sudo bash ./install.sh

#run algo
input_path = '/content/vid/*.mp4*'
output_path = '/content/vid_csv/'
for f in glob.glob(input_path):
    v_name = f.rsplit('/',1)[-1]
    print(v_name)
    #!./OpenFace/build/bin/FaceLandmarkVidMulti -f vid/video.mp4 -out_dir processed
    args = "./OpenFace/build/bin/FeatureExtraction -f " + f + " -of " + output_path + v_name +".csv -q"
    print(args)
    #subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)
    subprocess.call(args, shell=True)