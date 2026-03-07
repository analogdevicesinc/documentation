How to Download AD594x Source Code
==================================

The AD594x is an SPI slave device that is controlled by a host microcontroller. The microcontroller supplied with the AD594x evaluation kits is the ADuCM3029. There are a number of example projects developed which run on the ADuCM3029 to control the AD594x. The source code is stored and version controlled on GitHub.com.

Both the AD5940 and AD5941 share the same code base. Note that AIN6 and GP3-GP7 are not available on the AD5941.

.. admonition:: Download
   :class: download

   
   `AD5940 Source Code <https://github.com/analogdevicesinc/ad5940-examples>`_


Repository Structure
--------------------

The repository has 3 main folders

-  LICENSE - this has details on the license of the source code
-  doc - has available documentation
-  examples - contains all the example programs

Within the examples folder there is a folder called ad5940lib. This is a sub-module and is source controlled in a separate repository. It is important to do a recursive clone of the repository to ensure this sub-module is cloned also. If downloading the source code via a zip or tar file the ad5940lib will need to be downloaded separately and added the the ad5940lib folder in examples

How to clone the AD5940 Git Repository
--------------------------------------

To clone the AD5940 code repository

-  Navigate to the link above and copy the URL.
-  Open Git bash or your preferred Git tool and change directory to where you want to save the files
-  Type in "git clone --recursive https://github.com/analogdevicesinc/ad5940-examples.git"
-  This command copies the entire ad5940 module and sub-modules into the folder
-  The source code should now be downloaded in the specified folder
