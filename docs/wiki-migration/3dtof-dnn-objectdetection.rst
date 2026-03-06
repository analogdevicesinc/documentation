Deep Neural Network Object Classification with 3D ToF Python Demo
=================================================================

Description
-----------

The Python example uses a pre-trained deep neural network (DNN), which is trained to classify 20 objects. The network is described by two files, which are loaded into the script and converted into a classifier structure using OpenCV’s “dnn” module. After establishing a connection with the 3D ToF camera, the depth map and a blended image from the IR image and the depth image are streaming. The classifier is applied to the video stream of the blended image in real time.

Build
-----

Presuming the 3D ToF SDK has already been built on your machine, in order to build the Python bindings, you’ll need to do the following, depending on your host platform :

Linux
~~~~~

::

   cmake -DWITH_PYTHON=on ..
   make -j4

Windows
~~~~~~~

::

   cmake -DWITH_PYTHON=on ..
   cmake --build . --config Release (or Debug depending on the configuration) -j 4

This step will create the python aditof library. It will also ensure that the two files that describe the network -- MobileNetSSD_deploy.prototxt and MobileNetSSD_deploy.caffemodel -- are downloaded. In order for the Python example to work, the OpenCV python package needs to be installed, via pip.

::

   pip3 install opencv-contrib-python

Run
---

To run the application, run the dnn.py script either from your Python IDE or directly from the command line. The example can be found under bindings/python/examples/dnn. For the script to be able to load the network model, the location of the network files must be given as an argument, as illustrated below. Alternatively, you can copy the MobileNetSSD_deploy.prototxt and MobileNetSSD_deploy.caffemodel next to the dnn script.

::

   python3 dnn.py --prototxt \pathTo\MobileNetSSD_deploy.prototxt  
           --weights \pathTo\MobileNetSSD_deploy.caffemodel

The example provides the option to run it both locally and on network backend. If you want to run it on network, you must give the device’s ip as an argument with the --ip option.

Once the application is started, the camera’s parameters will be printed in the console and the video stream will be shown on screen.

.. image:: https://wiki.analog.com/_media/dnn-preview.png
   :alt: dnn-preview.png

Process
-------

This demo is a combination of SSD Mobilenet object detection example from OpenCV and ToF SDK. In order to build the network model, the two downloaded files are loaded. The MobileNetSSD_deploy.prototxt is a text file which describes the architecture of the network, containing features such as input dimensions, layer types and hierarchy. The second file, MobileNetSSD_deploy.caffemodel, contains the weights of the model. After building the classifier model, a connection to the ToF device is established and frames are requested. The process of computing and displaying IR and depth maps is also illustrated in this example. A blended image is created, which is results as a mixture of the depth and IR frame. With the aid of the depth map, the area of interest is easily identified. The network then determines the class of object detected based on its shape.
