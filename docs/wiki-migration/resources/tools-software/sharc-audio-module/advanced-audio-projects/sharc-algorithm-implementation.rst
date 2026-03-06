Implementing SHARC Algorithm on Audio Starters
==============================================

//This is a tutorial that covers implementation of audio algorithms in Audio Starter frameworks. //

Overview
--------

SHARC processing can be utilized to implement complex audio processing algorithms. IPC mechanism is already in place to pass the data from ARM core to the SHARC cores and vice versa. This page refers to audio gain as one algorithm that is implemented for reference. The algorithm parameters are passed from shell command and processed in SHARC cores.

--------------

Prerequisites
-------------

-  Local copy of SAM Audio Starter repository – https://bitbucket.analog.com/scm/nafaeproj/sam-audio-starter.git
-  Branch name (note: this is under review and not merged to the main branch yet) – FAESWPROJ-219-SHARC-Algo
-  Follow instructions from README to build and run audio starter on SC589

--------------

Update global ARM context
-------------------------

-  Add a new algorithm parameter to struct \_APP_CONTEXT in – <project>\\ARM\\src\\context.h
-  Refer to gain that is added to this structure
-  If needed, initialize this parameter in – static portTASK_FUNCTION( startupTask, pvParameters )
-  Refer to gain initialization – global_gain_init(context);
-  Construct and send IPC message to SHARC cores in – static portTASK_FUNCTION( houseKeepingTask, pvParameters )
-  Refer to construction of IPC gain message under this function

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/arm_context_algo.jpg
   :align: center
   :width: 100px

--------------

Update IPC structures
---------------------

-  Add a new algorithm parameter to the IPC message structure in – <project>\\ALL\\include\\ipc.h
-  Refer to struct \_IPC_MSG_GAIN
-  Make sure to align all the members of this structure according to the architecture
-  Future enhancement – Update the name of this structure to be more like IPC_MSG_SHARC_ALGORITMS and update all the references to it

--------------

Add support to handle in SHARC cores
------------------------------------

-  Audio processing in SHARC cores is implemented under these files – <project>\\SHARC0\\src\\sharc<0/1>_main.c
-  Refer to how “gain” is implemented under processAudio ()
-  IPC receive message handler in these files is implemented under ipcMsgRx ()
-  Refer to how switch case IPC_TYPE_GAIN is handled in this function that updates the static global variable in these files to keep an updated copy of “gain” passed from ARM core
-  Future enhancement – Update the name of messages handled in Rx handler to be more like IPC_MSG_SHARC_ALGORITMS

|image1|

.. important::

   In ProcessAudio () on SHARC cores, do processing of algorithm parameters after needed normalization


   |image2|

--------------

Implement new shell command
---------------------------

-  All the shell commands are implemented under this file – sam-audio-starter\\ARM\\src\\oss-services\\shell\\shell_cmds.c
-  Refer to how shell command “gain” is implemented under shell_gain ()
-  Validate and handle the limits of the inputs passed to the command
-  Construct and send IPC message to SHARC cores
-  Refer to construction of IPC gain message under shell_gain ()

.. image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/shell_algo.jpg
   :align: center
   :width: 100px

--------------

`Shell Commands#.|Advanced Audio Projects#.debug-session|Setup a Debug Session <https://wiki.analog.com/_media/navigation SHARC Algorithm Implementation#.shell-commands>`__

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sharc_algo_1.jpg
   :width: 100px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sharc-audio-module/advanced-audio-projects/sharc_algo_2.jpg
   :width: 100px
