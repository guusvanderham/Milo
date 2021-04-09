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
from sklearn.neighbors import (NeighborhoodComponentsAnalysis,KNeighborsClassifier)
from joblib import load
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
#load classifier
knn = load('knn.joblib')
#%%
def resize(frame, size):
    #crop to square
    if(frame.shape[1]>frame.shape[0]):
        cropside=int((frame.shape[1]-frame.shape[0])/2)
        cropped=frame[:,cropside:frame.shape[1]-cropside,:]
    #resize
    resized = cv2.resize(cropped, size, interpolation = cv2.INTER_AREA)
    
    return resized

def cut_out_detection(image, coords ):
    sizex,sizey,_=image.shape
    ymin=(coords[0]*sizey).astype(np.uint64)
    xmin=(coords[1]*sizex).astype(np.uint64)
    ymax=(coords[2]*sizey).astype(np.uint64)
    xmax=(coords[3]*sizex).astype(np.uint64)
    boxsizex=(((xmax-xmin)*0.30)/2).astype(np.uint64)
    boxsizey=(((ymax-ymin)*0.30)/2).astype(np.uint64)
    image = image[ymin+boxsizey:ymax-boxsizey,xmin+boxsizex:xmax-boxsizex,:]
    return image

def dominant_color(image):
    pixels = np.float32(image.reshape(-1, 3))
    n_colors = 2
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS
    if(pixels.shape[0]>0):
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
        return palette
    else:
        return [[],[]]
    

def detect(image,output_dict, category_index, knn):
    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key:value[0, :num_detections].numpy() for key,value in output_dict.items()}
    output_dict['num_detections'] = num_detections
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)
    best_detection = output_dict['detection_classes'][0]
    nn_detection=category_index[best_detection]['name']  
    scores=output_dict['detection_multiclass_scores'][0,:]
    if nn_detection =='ezel':
        
        if scores[0]<0.80:
            scores = np.delete(scores,0)
            print(len(scores))
            nextbest=np.argmax(scores)+2

            nn_detection=category_index[nextbest]['name'] 
            if nn_detection == 'hond':
                nn_detection = 'koe'
    elif nn_detection == 'koe'and  scores[2]<0.6:
                nn_detection = 'kuiken'
    elif nn_detection == 'schaap':
        scores=output_dict['detection_multiclass_scores'][0,:]
        if scores[5]<0.70:
            #np.delete(scores,5)
            #nextbest=np.argmax(scores)
            nn_detection='kuiken'#category_index[nextbest]['name'] 
        
    coords=output_dict['detection_boxes'][0]
    cutout=cut_out_detection(image,coords)
    color1, color2=dominant_color(cutout)
    if any(color1):
        knn_detection = knn.predict([np.array([color1,color2]).flatten().tolist()])
    else:
        knn_detection='none'
    
    return output_dict, knn_detection, nn_detection, color1




#%%

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # resize and make tensor
    size=(480,480)
    resized=resize(frame,size)
    
    #make tensor
    input_tensor = tf.convert_to_tensor(resized)
    input_tensor = input_tensor[tf.newaxis,...]
    
    #predict
    output_dict = model_fn(input_tensor)
    #detect
    output_dict, knn_detection, nn_detection, color1 = detect(frame, output_dict, category_index, knn)
    print(nn_detection)
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
    bar=np.ones((480,20,3)) 
    if any(color1):
        bar=np.ones((480,20,3))*color1  
    # Display the resulting frame
    image2=np.zeros((480,500,3))
    image2[0:480,0:480,:]=resized
    image2[0:480,480:500,:]=bar
    image2=image2.astype(np.uint8)
    #image=np.concatenate((image,bar),axis=2)
    cv2.imshow('frame',image2)
    
    
    
    #Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
