CN0363 Colorimeter Application User Guide
=========================================

Starting the Application
------------------------

.. important::

   Before starting the application please close all the running ADI IIO Oscilloscope instances.


.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/cn0363_startup.png
   :alt: Launch ADI CN0363 Colorimeter Application
   :align: left
   :width: 250px

The CN0363 Colorimeter Application can be launched from the top-left **"Applications Menu"** in the **"Other"** section.


Analyzing a Sample
------------------

The Colorimeter application has three main tabs `#automated_data_collection <https://wiki.analog.com/>`_, `absorbance_measurement <https://wiki.analog.com/>`_ and the `#sample_library <https://wiki.analog.com/>`_.

Automated Data Collection
-------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/colorimeter_automated_data_collection.png
   :alt: Automated Data Collection Tab
   :align: center
   :width: 500px


Analyze Sample
~~~~~~~~~~~~~~

Clicking the **Analyze Sample** button will perform an automated sample analyzes which will cycle through all three colors and calculate the absorbence factor for each of them. The analyzing process will take a few seconds and a progress-bar will be updated to indicate the current step. Once the process has completed the absorbance values will be displayed.

Once the analyzing process has finished it is also possible to either try to match the sample to a existing sample from the sample library or save the sample into the sample library for future use.

Match Sample
~~~~~~~~~~~~

Clicking the **Match Sample** button will compare the current sample to all samples in the sample library. If a sample is found that has a close enough matching score the sample including its name and match score will be displayed.

Save Sample
~~~~~~~~~~~

Captured data samples can be saved into the sample library for later use by clicking the **Save Sample** button. Samples that have been saved into the library are used in the sample matching process.

Current/Absorbance Measurement
------------------------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/colorimeter_current_absorbance_measurement.png
   :alt: Current/Absorbance Measurement Tab
   :align: right
   :width: 500px

In the Current/Absourbance Measurement tab gives direct access to the LED and gain controls and allows to periodically capture and view raw data.

On the left side are various controls that allow to change certain parameters.

-  **Excitation Frequency**: Selects the frequency of the excitation signal
-  **Excitation Current**: Selects the current of the excitation signal
-  **LED**: Selects the currently active LED. Options are None, Red, Green and Blue.
-  **Reference Channel Gain**: Selects the gain applied for the reference channel. Options are 33k Ohm and 1M Ohm.
-  **Sample Channel Gain**: Selects the gain applied for the sample channel. Options are 33k Ohm and 1M Ohm.

On the right side are three data plots. One plot each for the reference channel and the sample channel which show the measured current. And one plot for the absorbance that is derived from the currents.

Clicking the **Acquire Data** button below the plots will start the data capture process and the plots will be periodically update with new data. Clicking the button while the data capture process is active will stop it again.

Settings can be changed on the fly while the capture process is active to see their effect on the captured data.


Sample Library
--------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/colorimeter_sample_library.png
   :alt: Sample Library Tab
   :align: right
   :width: 500px

The sample library allows to manage and compare previously saved sample data. On the left side is a list of all samples. On the right side the absorbance values for the currently selected samples is displayed. It is possible to select multiple samples by holding the Ctrl key, this can be used to directly compare the absorbance of multiple samples to each other.

Samples can also be removed from the library by selecting the sample and then clicking the **Remove** button. A sample that has been removed from the library can not be restored.


Calibration
-----------

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/colorimeter_calibration.png
   :alt: Calibration Dialog
   :align: right
   :width: 400px

For optimum performance it is necessary to calibrate the application to the connected board and the environment. This calibration can be performed in the calibration dialog which can be opened from the application's menu. It allows to set the calibration parameters the LEDs and photo-diodes as well as performing a automated calibration.

Calibration must be performed with distilled water in both the reference and the sample probes. It is also recommended that during calibration the photo-diodes are shielded from ambient light.

Start the automatic calibration procedure in the software; from the Menu bar, open the **Calibration** dialog box, and click **Calibrate**. Once the calibration is done the calibration values will be updated.

It is also possible to save the current calibration data for later use by clicking the **Export** button or to load previously saved calibration data by clicking the **Import** button.

Calibration data includes a zero-offset for each channel and gain setting, which removes any potential offset that is measured if no excitation signal is present. The calibration data also includes a gain factor which expresses the relative relationship of the reference and sample channel values at full-scale excitation.

Source code
-----------

The source code for the Colorimeter application can be found on the `Analog Devices GitHub account <https://github.com/orgs/analogdevicesinc>`_ in the `colorimeter repository <https://github.com/analogdevicesinc/colorimeter>`_.

<div> **Install colorimeter application**

::

   <nowiki>$ git clone https://github.com/analogdevicesinc/colorimeter.git
   Cloning into 'colorimeter'...
   remote: Counting objects: 65, done.
   remote: Compressing objects: 100% (33/33), done.
   remote: Total 65 (delta 13), reused 2 (delta 2), pack-reused 28
   Unpacking objects: 100% (65/65), done.
   Checking connectivity... done.
   $ make
   cc -shared -o capture.so capture.c -liio -lm -Wall -Wextra -fPIC -std=gnu99 -pedantic -O3
   $ make install
   sed 's/@PREFIX@/\/usr\/local/' adi-colorimeter.desktop.in > adi-colorimeter.desktop
   sed 's/@PREFIX@/\/usr\/local/' lib/config.py.in > lib/config.py
   root@analog:~/colorimeter# make install
   install -d //usr/local/bin
   install -d //usr/local/share/adi_colorimeter/
   install -d //usr/local/lib/adi_colorimeter/
   install ./adi_colorimeter //usr/local/bin/
   install ./capture.so //usr/local/lib/adi_colorimeter/
   install ./adi_colorimeter.glade //usr/local/share/adi_colorimeter/
   ./setup.py install --prefix=/usr/local --root=/
   running install
   running build
   running build_py
   copying lib/config.py -> build/lib.linux-armv7l-2.7/adi_colorimeter
   running install_lib
   copying build/lib.linux-armv7l-2.7/adi_colorimeter/config.py -> /usr/local/lib/python2.7/dist-packages/adi_colorimeter
   byte-compiling /usr/local/lib/python2.7/dist-packages/adi_colorimeter/config.py to config.pyc
   running install_egg_info
   Removing /usr/local/lib/python2.7/dist-packages/adi_colorimeter-1.0-py2.7.egg-info
   Writing /usr/local/lib/python2.7/dist-packages/adi_colorimeter-1.0-py2.7.egg-info
   xdg-icon-resource install --noupdate --size 16 ./icons/adi-colorimeter16.png adi-colorimeter
   xdg-icon-resource install --noupdate --size 32 ./icons/adi-colorimeter32.png adi-colorimeter
   xdg-icon-resource install --size 64 ./icons/adi-colorimeter64.png adi-colorimeter
   xdg-desktop-menu install adi-colorimeter.desktop</nowiki>

</div>

Supported Devices
-----------------

-  :adi:`CN0363` + `ZED Board <http://zedboard.org/product/zedboard>`_, Rev C or later

More Information
----------------

-  :doc:`EVAL-CN0363-PMDZ User Guide </wiki-migration/resources/eval/user-guides/eval-cn0363-pmdz>`
