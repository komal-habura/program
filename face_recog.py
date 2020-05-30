#!/usr/bin/env python
# coding: utf-8

# In[9]:



from keras.applications.vgg16 import  VGG16
from glob import glob
from keras.layers  import Dense, Flatten,Lambda
from keras.applications.vgg16 import preprocess_input
from keras.preprocessing import image
model=VGG16(weights='imagenet',include_top=False,input_shape=(224,224,3))
train_path='face_detection/traindata/'
test_path='face_detection/test/'
len(test_path)
len(train_path)
for layer in model.layers:
    layer.trainable=False
folders=glob('../face_detection/traindata/*')
len(folders)
top_model=Flatten()(model.output)
top_model=Dense(len(folders),activation='softmax')(top_model)
from keras.models import Model
newmodel=Model(input=model.input,output=top_model)
newmodel.summary()
newmodel.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy'],
    
)
from keras.preprocessing.image import ImageDataGenerator
train_datagen=ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,

)
test_datagen=ImageDataGenerator(rescale=1./255)

train_dataset=train_datagen.flow_from_directory(
                    '../face_detection/traindata',
                    target_size=(224, 224),
                    batch_size=32,
                    class_mode='categorical')



test_dataset=test_datagen.flow_from_directory(
                     '../face_detection/test/',
                     target_size=(224, 224),
                     batch_size=32,
                     class_mode='categorical')
n=5
r=newmodel.fit_generator(
        train_dataset,
        steps_per_epoch=len(train_dataset),
        epochs=n,
        validation_data=test_dataset,
        validation_steps=len(test_dataset)
    
)
import pandas as pd
accu=pd.DataFrame(newmodel.history.history)
accuracy =accu['accuracy']
accuracy

import numpy as np
acuu=accuracy[n-1]
accu=np.array(acuu)
accuracy=accu*100
    
    


# In[ ]:





# In[ ]:





# In[10]:


msg='your model accuracy {}'.format(accuracy)


# In[11]:


msg


# In[ ]:





# In[8]:


import smtplib
mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.starttls()
mailServer.login('komalhabura2@gmail.com' , '8774komal@9690')
mailServer.sendmail('komalhabura2@gmail.com' , 'komalhabura5@gmail.com' , msg)
print("\n sent! ")
mailServer.quit() 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[7]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[133]:


accu


# In[ ]:




