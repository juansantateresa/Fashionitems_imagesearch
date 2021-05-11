import os
import numpy as np
import pandas as pd
import pickle
import tensorflow
from keras import models
from keras.preprocessing.image import load_img, img_to_array, array_to_img
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import dill
import pickle
import streamlit


def similar_five_prediction(image):
  
  with open('test_pickle', 'rb') as f:
    test_arr = pickle.load(f)
  img_dim = (28,28)
  model = models.load_model('/content/model_4.h5')
  image = ImageOps.fit(image, img_dim, Image.ANTIALIAS)
  image_to_predict_tensor = img_to_array(image)
  image_to_predict_tensor /= 28
  image_to_predict_tensor = cv2.cvtColor(image_to_predict_tensor,cv2.COLOR_RGB2GRAY)
  image_to_predict_tensor = np.reshape(image_to_predict_tensor, (1,28,28,1))
  prediction = np.argmax(model.predict(image_to_predict_tensor))
  global_prediction = model.predict(test_arr)
  n_cols = 5
  labels = []
  for i in range(n_cols):
    for j in range(0, len(test_arr)):
        if  prediction == np.argmax(global_prediction[j]):
          labels.append(j)
          i+=1
                    
  fig, ax = plt.subplots(1, 5, figsize=(10,10))
  
  for n in range(5):
    ax[n].imshow(test_arr[labels[n]].reshape(28,28)) 
    ax[n].axis("off")
  streamlit.pyplot(fig)
