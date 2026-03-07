| 
| ====== Data Logger ======

General Description
===================

The data logger tool is used to :

-  Display data as one of the following options :

   -  Signal
   -  Text
   -  Seven Segment Display

-  Save data to file
-  Import data from file

Pressing the "+" button will generate a new tool

Display Signals
===============

Using the left side menu user can select from the available device channels that will be displayed on the plot. The data is plotted in time based on the starting time (shown in the top right of the plot), the starting time reflects when the tool started collecting data and will reset on user pressing "Clear". The data that will be displayed is collected from the device on pressing "Run" button. The data collected will be removed on pressing "Clear" this will also reset the starting time. To use this option click "Plot" button on the bottom right

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dataloggersingaldisplay.png
   :align: center
   :width: 600px

Display Text
============

Using the left side menu user can select from the available devices, for the selected device channels last read value and the unit of measurement will be displayed in text format

To use this option click "Text" button on the bottom right

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dataloggertextdisplay.png
   :align: center
   :width: 600px

Display Seven Segment
=====================

Using the left side menu user can select from the available devices, for the selected device channels last read value, minimum and maximum recorded values and the unit of measurement will be displayed in seven segment display format

To use this option click "7 Segment" button on the bottom right

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/datalogger7segdisplay.png
   :align: center
   :width: 600px

Settings
========

The gear button in the top right corner of the plugin will open the settings allowing user to:


|image1|

-  Changing the title in settings from "DataMonitor" will reflect in the tool name
-  toggle between displaying real time or delta values. Real time values are based on the system time, delta values consider starting point as 0 and represents the amount of time passed since then.
-  toggle "PLOT NOW"

   -  when enabled will update the plot to the current time for each read
   -  when disabled will allow user to pick a date and a time to go to on the plot

-  Delta represents the interval displayed on the plot
-  Autoscale option changes the minimum and maximum of Y-Axis to fit all values recorded
-  Changing Min and Max will update the minimum respectively the maximum values of Y-Axis
-  Curve settings affect all curves on the plot
-  settings for seven segment section allow user to set precision of display values and toggle on/off the minimum and maximum values
-  Data logging section is used for saving and importing data from and to a specified CSV file like the one bellow

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dataloggerfileexample.png
   :align: center
   :width: 400px

Save data
=========

To save data to file there are two options

-  Toggle "Live data logging" on this will save to file data on each read for all enabled channels
-  Pressing "Save data" will override the selected CSV file with all the recorded values of the enabled channels

Import data
===========

On importing data a special menu is added containing the channels from file. Each channel contains the data from the CSV file from it's column, no extra data will be added to those channels when tool is recording. By pressing the "x" button all imported data is removed. Importing data multiple times from same CSV file will override current imported data Importing data from different CSV files will create new menus like the one bellow for each file

.. image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/dataloggerimportedch.png
   :align: center
   :width: 200px

.. |image1| image:: https://wiki.analog.com/_media/university/tools/m2k/scopy/test-cases/image_2024-04-04_121442134.png
   :width: 200px
