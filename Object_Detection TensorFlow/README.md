# Object-Detection using TensorFlow

1. Download Models from https://github.com/tensorflow/models

2. pip install tensorflow. (You should be having Tensorflow version greater than 1.4.0 to run this
  
3. Download Google Protobuf https://github.com/google/protobuf Windows v3.4.0 release “protoc-3.4.0-win32.zip”
  (I have also uploaded the compiled protoc files check)

4. Extract the Protobuf download to Program Files, specifically
   <br><code>C:\Program Files\protoc-3.4.0-win32</code>

5. Now cd into models\research.
   <br><code>cd path\to\models\research</code>  
   
6. Execute the protobuf compile
   <br><code>“C:\Program Files\protoc-3.4.0-win32\bin\protoc.exe” object_detection/protos/*.proto --python_out=.</code>
   
7. Now navigate to models\research\object_detection\protos and and verify the .py files were created successfully as a result of the compilation. (only the .proto files were there to begin with)

8. cd to \models\research\object_detection. Open the jupyter notebook object_detection_tutorial.ipynb. Here you can play with the API.

# Object Detection in Video:

1. For that we need "moviepy". 
   This library helps to edit video frame by frame do the object detection on that than merge all the frame to make a video.
  
   <code>pip install moviepy</code>

2. I have uploaded the video you can download and see the results.

Thanks to: 

https://github.com/tensorflow/models/tree/master/research/object_detection
https://towardsdatascience.com/is-google-tensorflow-object-detection-api-the-easiest-way-to-implement-image-recognition-a8bd1f500ea0
https://medium.com/@rohitrpatil/how-to-use-tensorflow-object-detection-api-on-windows-102ec8097699
