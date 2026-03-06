Using EVAL-ADICUP360 with IAR and Keil IDEs
===========================================

| 
| This page provides detailed information about using the EVAL-ADICUP360 board with other IDEs than Eclipse, such as IAR Embedded Workbench and Keil µVision. You can find here how to import, build and debug existing IAR/Keil project and how to create your own projects for ADuCM360.

.. note::

   Our intent is to keep the same structure as for Eclipse project so the user does not have to do more than IDE specific configuration.


This page will outline:

-  How to import and run an existing project
-  How to create a new project for ADuCM360

.. important::

   Before using below steps check your IAR and Keil software package version. If you want to use CMSIS-DAP interface you need to use the latest versions that have support for **CMSIS-DAP Debugger**.


| 
| ====== How to import and run an existing project ======
| You can find the already created <fc #008080>IAR</fc> and <fc #008080>Keil</fc> projects on the **EVAL-ADICUP360 Git repository**, together with <fc #008080>Eclipse</fc> project. Further it will be used as example the **ADuCM360_demo_blink** projects. Please use the link below to download the package:

| 
|

.. admonition:: Download
   :class: download

   
   :git-EVAL-ADICUP360:`ADuCM360_demo_blink projects <projects/ADuCM360_demo_blink>`
   


Inside of the **ADuCM360_demo_blink** folder find **ADuCM360_demo_blink.eww** for <fc #008080>IAR</fc> and **ADuCM360_demo_blink.uvprojx** for <fc #008080>Keil</fc>.

   


| 

Run an existing IAR project
---------------------------

|

| Open **ADuCM360_demo_blink.eww** project and press <fc #ffa500>Make</fc> button:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/blink_demo_iar_1.png
   :width: 650px

| 
| Connect **EVAL-ADICUP360** via DEBUG USB and press <fc #ffa500>Download and Debug</fc> button:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/blink_demo_iar_2.png
   :width: 650px

| 
| A Debug session will open. You can run the program or can debug step by step:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/blink_demo_iar_3.png
   :width: 650px

| 
| ===== Run an existing Keil project =====
| Open **ADuCM360_demo_blink.uvprojx** project and press <fc #ffa500>Build</fc> button:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/blink_demo_keil_1.png
   :width: 650px

| 
| Connect **EVAL-ADICUP360** via DEBUG USB and press <fc #ffa500>Download</fc> button:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/blink_demo_keil_2.png
   :width: 650px

| 
| A Debug session will open. You can run the program or can debug step by step:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/blink_demo_keil_3.png
   :width: 650px

| 
| ====== How to create a new project for ADuCM360 ======
| Both IDEs offer support for ADuCM360 microcontroller which make it very easy to use them with **EVAL-ADICUP360** board. In this chapter will be presented basic setup how to create a new ADuCM360 project. The build, download and debug steps were already explained above.

| 
| ===== Create IAR new project =====
| Open **IAR Embedded Workbench**, go to <fc #4682b4>\ **Project**\ </fc> tab and select <fc #ffa500>Create New Project</fc> -> select an <fc #ffa500>Empty project</fc> as *Project Template* -> press <fc #ffa500>OK</fc> and save the project on your drive:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_iar_1.png
   :width: 650px

| 
| Select project in left window -> <fc #4682b4>\ **Project**\ </fc> and select <fc #ffa500>Add Group</fc> - to create project folders and for each folder create new files (<fc #4682b4>\ **File**\ </fc> -> <fc #ffa500>New</fc> -> <fc #ffa500>File</fc>) or you can add files (<fc #4682b4>\ **Project**\ </fc> -> <fc #ffa500>Add files</fc>):

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_iar_2.png
   :width: 650px

   | 
|

.. note::

   You need to have a startup code for ADuCM360 microcontroller. Write your own or just use the *startup_ADuCM360.s* file that we provide (:doc:`How to import and run an existing project </wiki-migration/resources/eval/user-guides/eval-adicup360/quickstart/keil_iar_support>`).


| 
| Select project in the left window -> <fc #4682b4>\ **Project**\ </fc> -> <fc #ffa500>Options</fc>:

-  <fc #ffa500>General Options</fc> ->\ **Target** tab -> select **Device** -> *AnalogDevices ADuCM360*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_iar_3.png
   :width: 650px

| 
| \* <fc #ffa500>General Options</fc> -> **Library Configuration** tab -> check *Use CMSIS*

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_iar_4.png
   :width: 650px

| 

-  <fc #ffa500>C/C++ Compiler</fc> -> **Preprocessor** tab -> *Additional include directories* - add path for all include files that will be used in the project:


|image1|

.. note::

   For **debugger** configuration you can select: **CMSIS-DAP** or **J-Link** interface (depending on your hardware possibilities).


-  <fc #ffa500>Debugger</fc> -> **Setup** tab -> **Driver** -> *CMSIS DAP*:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_iar_6.png
   :width: 650px

.. note::

   You can use **CMSIS-DAP interface** with default settings and only connecting an USB cable to ADICUP360 board using **DEBUG** USB.


-  <fc #ffa500>Debugger</fc> -> **Setup** tab -> **Driver** -> *J-Link/J-Trace*:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_iar_8.png
   :width: 650px

.. note::

   You can use **J-Link interface** with default settings and with J-Link adapter connected to ADICUP360 board using **P16** connector.


-  <fc #ffa500>Debugger</fc> -> **Download** tab -> check *Use flash loader(s)*:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_iar_7.png
   :width: 650px

| 
| ===== Create Keil new project =====
| Open **Keil µVision**, go to <fc #4682b4>\ **Project**\ </fc> tab and select <fc #ffa500>New µVision Project</fc> -> give a name -> select in the <fc #ffa500>Device</fc> window -> *ADuCM360* -> press *OK*:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_keil_1.png
   :width: 650px

| 
| In the pop-up window check under <fc #ffa500>CMSIS</fc> -> *CORE* and under <fc #ffa500>Device</fc> -> *Startup*:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_keil_2.png
   :width: 650px

| 
| Select <fc #4682b4>\ **Target 1**\ </fc> -> go to <fc #ffa500>Manage Project Items</fc> button and add your project folders and necessary files:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_keil_3.png
   :width: 650px

| 
| Select <fc #4682b4>\ **Target 1**\ </fc> -> go to <fc #ffa500>Options</fc> button -> <fc #ffa500>Debug</fc> tab -> select *CMSIS-DAP Debugger*:

.. image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_keil_4.png
   :width: 650px

| 

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/eval-adicup360/reference_designs/demo_iar_5.png
   :width: 650px
