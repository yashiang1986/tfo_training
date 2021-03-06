# A python script to download the five tensorflow models
import six.moves.urllib as urllib
import tarfile
import os

def download_model(model_name, file_format='.tar.gz',\
                   base_url='http://download.tensorflow.org/models/object_detection/'):
 
    model_file =  model_name + file_format
    opener = urllib.request.URLopener()
    print("Downloading model: {}".format(model_name))
    opener.retrieve(base_url + model_file, model_file)
    tar_file = tarfile.open(model_file)
    for file in tar_file.getmembers():
     
        tar_file.extract(file, os.getcwd())
    print("Extraction Done: {}".format(model_name+file_format)) 
            
if __name__ == "__main__":
    
    model_names = ['faster_rcnn_inception_v2_coco_2017_11_08']
    
    for model_name in model_names:    
        download_model(model_name)