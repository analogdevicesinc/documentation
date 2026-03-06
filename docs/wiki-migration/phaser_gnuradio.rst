Phaser Setup With GNUradio
==========================

The phaser can be controlled with GNUradio either directly on the raspberry pi, or remotely on a Windows computer. This page will have instructions for setting up both of these use cases.

Prerequisite: ADI Kuiper Linux
------------------------------

Installing the ADI Kuiper Linux OS is required to use the phaser, and instructions for doing so can be found in the :doc:`Quick Start Guide </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0566/quickstart>`.

Running on the Raspberry Pi
---------------------------

ADI Kuiper Linux already comes with GNUradio pre-installed, so comparatively little work is required to control the Phaser through GNUradio on the RasPi. However, for creating and editing GNUradio flowgraphs, the desktop installation below can be easier to work with.

Procedure
~~~~~~~~~

-  Download the required files here , and transfer them to the Raspberry Pi

.. note::

   add zip download


-  Unzip and place phaser_rev4.grc and ADAR_pyadi_functions_edited.py into the **~/pyadi-iio/examples/phaser** folder on the Raspberry Pi
-  Run the following command in the terminal to rename iio.py to iiopy.py:

.. container:: center round box

   
   ``sudo mv /usr/local/lib/python3.9/dist-packages/iio.py /usr/local/lib/python3.9/dist-packages/iiopy.py``


-  Then run each of these commands to access "rx_tx.py" and "context_manager.py", and **edit the "import iio" statement to "import iiopy as iio"**:

.. container:: center round box

   
   | ``sudo mousepad /usr/local/lib/python3.9/dist-packages/adi/rx_tx.py``
   | ``sudo mousepad /usr/local/lib/python3.9/dist-packages/adi/context_manager.py``


-  Now open phaser_rev4.grc using gnuradio-companion, which should bring up the flowgraph
-  Edit the signal_freq parameter box to have your source's frequency as default, and change the tx_mode default value to match your source
-  Now pressing the run button should run the flowgraph, and bring up the GUI.

.. note::

   The sliders within the GUI currently do not properly update the tx_mode or signal_freq parameters, so they need to be updated before running the flowgraph


Running on a Windows Computer
-----------------------------

Controlling the Phaser with GNUradio on a Windows machine requires significantly more steps, but will also likely be much faster than the Raspberry Pi both when running and editing the flowgraphs. This procedure is based on using Miniconda to create an enclosed environment for GNUradio and its required packages.

Part 1: Miniconda installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Install Miniconda from the `official Anaconda webpage <https://docs.conda.io/projects/miniconda/en/latest/>`__
-  Open the Anaconda prompt
-  Create a new environment for GNUradio named "gnuradio" with the following command:

.. container:: center round box

   
   ``conda create -n gnuradio``


-  Then enter the environment with:

.. container:: center round box

   
   ``conda activate gnuradio``


-  Set the environment to install packages from the conda-forge channel with these commands:

.. container:: center round box

   
   ``conda config --env --add channels conda-forge conda config --env --set channel_priority strict``


-  Now install GNUradio using this command:

.. container:: center round box

   
   ``conda install gnuradio=3.10.6.0``


.. note::

   try install with gnuradio 3.8 as well, to be thorough


-  After installing GNUradio, install pyadi-iio with

.. container:: center round box

   
   ``conda install -c conda-forge pyadi-iio``


.. note::

   check if not putting conda-forge channel in command still downloads from conda-forge


-  **Optional**: install the Spyder IDE, this can be skipped if there is another IDE that you prefer

.. container:: center round box

   
   ``conda install spyder``


Part 2: Connectivity and Network Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Download and install the Windows drivers for the Pluto :doc:`here </wiki-migration/university/tools/pluto/drivers/windows>`. This is needed for Windows to detect the Pluto properly
-  Power up the phaser, connect the Phaser/Raspberry Pi's ethernet port to your computer's ethernet port, and connect the Pluto to your computer via USB
-  In the windows terminal, SSH into the Raspberry Pi with the command below, and enter the password "**analog**" when prompted

.. container:: center round box

   
   ``ssh analog@phaser.local``


.. important::

   If you have not run the setup script to configure the SD card, as explained in :doc:`this section </wiki-migration/resources/eval/user-guides/circuits-from-the-lab/cn0566/quickstart>`, the SSH command will not work.


-  Once connected to the Raspberry Pi via SSH, run the command below to edit the dhcpcd.conf file

.. container:: center round box

   
   ``sudo nano /etc/dhcpcd.conf``


-  Add the following lines to the bottom of the file to set the Raspberry Pi's ethernet port IP address (example value shown)

.. container:: center round box

   
   ``interface eth0 static ip_address=192.168.3.1``


   
   |image1|

-  Exit and save the file, then reboot the system with

.. container:: center round box

   
   ``sudo reboot``


-  In Windows, go to *Control Panel > Network and Sharing Center > Change Adapter Settings* to view the computer's current connections, and select the ethernet connection that is not the Pluto, or any wired internet connection

.. image:: https://wiki.analog.com/_media/network_connections.png
   :align: center
   :width: 600px

-  Open it's properties, then open the properties for **IPV4**, and manually set it's IP address to the same subnet as the one used for the Raspberry Pi (example value shown)

.. image:: https://wiki.analog.com/_media/ethernet_ip_crop.png
   :align: center
   :width: 400px

-  Optional check: in Windows Powershell, run ``ping {ip}`` to see if the Phaser and Pluto are able to communicate with your computer (default Pluto IP is 192.168.2.1)

.. image:: https://wiki.analog.com/_media/powershell.png
   :align: center
   :width: 600px

Part 3: GNUradio project setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Create a new folder to use as the GNUradio project directory
-  Download the GNUradio flowgraph and related files here, extract them and move them to your project directory

.. note::

   add zip download


-  Download the pyadi-iio package files from Github :git-pyadi-iio>`__ (or find it on the Raspberry Pi), and from the pyadi-iio:`pyadi-iio <examples/Phaser folder, copy the following files into the project directory

.. container:: center round box

   
   ``phaser_find_hb100.py phaser_examples.py phaser_functions.py config.py SDR_functions.py LTE20_MHz.ftr``


.. note::

   decide whether to include these files in the zip along with gnuradio files and ADAR_edited


-  Edit the files ``phaser_find_hb100.py`` (at line 71) and ``phaser_examples.py`` (at line 125), changing the IP address of the ad9361 to **192.168.2.1** (Pluto default IP)

.. image:: https://wiki.analog.com/_media/edit_to_phaser_examples.png
   :align: center
   :width: 800px

-  From the terminal, navigate to the project directory, then run the following command to find the frequency of the HB100 (Ensure HB100 is turned on and directed at Phaser)

.. container:: center round box

   
   ``python phaser_find_hb100.py``


-  Next, run the following command to calibrate the Phaser's array, following the instructions printed from the terminal

.. container:: center round box

   
   ``python phaser_examples.py cal``


Part 4: Running the GNUradio Flowgraph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  In the anaconda prompt, enter the commands below to activate the environment previously created, and then run GNUradio Companion

.. container:: center round box

   
   ``conda activate gnuradio gnuradio-companion``


-  In GNUradio Companion, open the phaser_rev4.grc file in the project directory

.. important::

   Double check that config.py is in the project directory! If config.py is not present, GNUradio Companion will crash upon saving or running the flowgraph.


-  In the flowgraph, open the properties of the *Phaser Python Control Block*, and select the "Open in editor" button

.. tip::

   To set the default editor for GNUradio Companion on Windows, follow the instructions stated `here <https://wiki.gnuradio.org/index.php/Embedded_Python_Block#User_notes>`\


-  Edit the ``Sys.path.append()`` statement (located with the import statements) so that it appends the path of your project directory, for example:

.. container:: center round box

   
   ``Sys.path.append("C:\Users\USER\Desktop\GNUradio_project_folder")``


-  Save the file, then return to GNUradio Companion and click "OK" to close the Phaser block window

.. tip::

   GNUradio Companion will run the python code for the Phaser block every time there are changes made to it, which will cause it to attempt connection to the Phaser. This will cause GNUradio Companion to freeze for a short (sometimes long) while, this is expected behavior and you can see the connection attempts being printed in the anaconda prompt window.


-  Press the run button in the toolbar to run the flowgraph and launch the GUI

.. |image1| image:: https://wiki.analog.com/_media/raspi_dhcpcd.png
   :width: 800px
