# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 17:03:18 2021

@author: guusv
"""
import io
import os
import scipy.misc
import numpy as np
import six
import time
import glob
from IPython.display import display

from six import BytesIO

import matplotlib
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import cv2
import tensorflow as tf
from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
#%%
#load the model
tf.keras.backend.clear_session()
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        tf.config.experimental.set_virtual_device_configuration(gpus[0], [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
    except RuntimeError as e:
        print(e)
model = tf.saved_model.load(r'model\saved_model')
model_fn = model.signatures['serving_default']

#create category index
labelmap_path=r'model\label_map.pbtxt'
category_index = label_map_util.create_category_index_from_labelmap(labelmap_path, use_display_name=True)
#%%
def resize(frame, size):
    #crop to square
    if(frame.shape[1]>frame.shape[0]):
        cropside=int((frame.shape[1]-frame.shape[0])/2)
        cropped=frame[:,cropside:frame.shape[1]-cropside,:]
    #resize
    resized = cv2.resize(cropped, size, interpolation = cv2.INTER_AREA)
    
    return resized

def detect(output_dict, category_index):
    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key:value[0, :num_detections].numpy() for key,value in output_dict.items()}
    output_dict['num_detections'] = num_detections
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
    
    
    best_detection = output_dict['detection_classes'][0]
    print(category_index[best_detection]['name'])
    return output_dict



#%%

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resize and make tensor
    size=(512,512)
    resized=resize(frame,size)
    
    #make tensor
    input_tensor = tf.convert_to_tensor(resized)
    input_tensor = input_tensor[tf.newaxis,...]
    
    #predict
    output_dict = model_fn(input_tensor)
    #detect
    output_dict = detect(output_dict, category_index)
    #visualize
    image = vis_util.visualize_boxes_and_labels_on_image_array(
        resized,
        output_dict['detection_boxes'],
        output_dict['detection_classes'],
        output_dict['detection_scores'],
        category_index,
        instance_masks=output_dict.get('detection_masks_reframed', None),
        use_normalized_coordinates=True,
        line_thickness=8)
        
    # Display the resulting frame
    cv2.imshow('frame',image)
    
    
    #Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
