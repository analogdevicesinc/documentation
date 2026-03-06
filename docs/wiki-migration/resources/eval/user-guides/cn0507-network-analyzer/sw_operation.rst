The Software GUI
================

The important parts of the CN-0507 software GUI is shown in the next figure.


|image1|

How to use the GUI
------------------

Connection
~~~~~~~~~~

After launching the software GUI. The connection window will be first shown. It lists all the available serial ports. To start using the GUI, choose the COM port of the EVAL-ADICUP3029 used. Have the baud rate set to the default, 115200, then click \*\* Connect \*\*. The connection window will automatically close after a successful connection.


|image2|

Performing a Sweep
~~~~~~~~~~~~~~~~~~

To perform a sweep, just click the \*\* Start Sweep \*\* button. With the default sweep setting values, this is an example of an open sweep.


|image3|

The default settings have it set at 25 steps, with a start frequency of 1700 MHz, and a stop frequency of 3400 MHz. The frequency range that the CN-0507 can handle is from 1700 to 3400 MHz, hence the default values. The number of steps can be chosen between the available value of 25, 50, 100, 500, and 1000 steps. The expected time per sweep is indicated at the right of the steps box. The S-parameters that will be plotted may also be selected at the sweep settings card. It is recommended to have all the S-parameters checked since it is also possible to hide a plot by clicking its legend at the top.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/cn0507-network-analyzer/palantir_gui_overview.png
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/cn0507-network-analyzer/connection_screen.png
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/cn0507-network-analyzer/sweep_open_default_settings.png
