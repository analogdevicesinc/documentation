Setting-up Python Environment
=============================

-  Please install python into your local machine. The python scripts are developed and executed using python 3.9.0 version, so recommend using version 3.9.0 or beyond. `Download python <https://www.python.org/downloads/>`__
-  Once python is installed, make sure the environment path (on windows machine) is set properly. You can verify if python is installed properly by typing “python --version” command on command line tool such as gitbash, command prompt, power shell, etc.

|image1| |image2|

-  Install the “pyadi-iio” python package by executing command “python -m pip install pyadi-iio”. Detailed guide on installing it is available in `Python Interfaces for ADI Hardware <https://github.com/analogdevicesinc/pyadi-iio>`__

<fc #008000>\ *\*Make sure to install additional support packages by running requirements.txt file using command “python -m pip install -r requirements.txt from “scripts/” directory”*\ </fc>

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_pyadi-iio_installation.png
   :align: center
   :width: 600px

Modifying/running Python Scripts
================================

-  All python scripts specific to the IIO firmware are stored into “scripts” folder present in the project directory. So, any script must be executed from this folder.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_installing_dependencies.png
   :align: center
   :width: 600px

-  Update the ‘uri’ interface in script according to COM port assigned to your device (sdp-k1). Default COM port is set to COM16 in all scripts.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_update_uri.png
   :align: center
   :width: 600px

Output Obtained from the Python Script
======================================

While executing the *adxxxx_data_capture.py*, the command prompt requests for the number of samples to be entered by the user.

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_number_of_samples_request.png
   :align: center
   :width: 600px

On Entering the number of samples *n*, on successful completion of capturing *n* samples, the data points are stored in a csv as *adc_data_capture.csv* in the folder where the script is present.


|image3|

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_py_env_variable.png
   :width: 600px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_py_version_check.png
   :width: 600px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/ad717x_python_output.png
   :width: 600px
