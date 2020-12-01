import os

caffe_path = "/opt/caffe/python"

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))

ecd_path = os.path.join(
    parent_path, "data", "scene_understanding/EurasianCitiesDatabase")
yud_path = os.path.join(
    parent_path, "data", "scene_understanding/YorkUrbanDatabase")
# hlw_path = os.path.join(
#    parent_path,"data","scene_understanding","HLW")

cnn_weights_path = os.path.join(parent_path, "cnn", "weights.caffemodel")
cnn_mean_path = os.path.join(parent_path, "cnn", "mean.binaryproto")
cnn_config_path = os.path.join(parent_path, "cnn", "deploy.prototxt")
