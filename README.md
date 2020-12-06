# TensorFlow-2.x-YOLOv3

YOLOv3 and YOLOv4 implementation in TensorFlow 2.x, with support for training, transfer training, object tracking mAP and so on...
Code was tested with following specs:
- i5-7300HQ- CPU and Nvidia 1050TI GPU
- OS Ubuntu 18.04
- CUDA 10.1
- cuDNN v7.6.5
- TensorRT-6.0.1.5
- Tensorflow-GPU 2.3.1
- Code was tested on Windows 10 (TensorRT not supported officially)
## GPU compatibility on Windows 10
- check if your GPU is compatible
- install GPU driver
  https://www.nvidia.com/download/index.aspx?lang=en-us
- download and install CUDA 10.1
  https://developer.nvidia.com/cuda-10.1-download-archive-base
- download and unzip cuDNN v7.6.5, may require creating free account
  https://developer.nvidia.com/rdp/cudnn-archive
- move from unziped cuda (cuDNN) folder to installed NVIDIA GPU Computing Toolkit/CUDA/v10.1 folder: from -> to
- bin/cudnn64_7.dll -> bin
- include/cudnn.h -> include
- lib/x64/cudnn.lib -> lib

## Installation
First, clone or download this GitHub repository.
Install requirements and download pretrained weights:
```
pip install -r ./requirements.txt

# yolov3
wget -P model_data https://pjreddie.com/media/files/yolov3.weights

Download VLC Media Player and add its directory to environmental variable PATH
https://www.videolan.org/vlc/index.pl.html

``` 
## Run program
- Go to TensorFlow-2.x-YOLOv3 directory
- run GUI from command line:
- python app.py


## Enjoy :)
