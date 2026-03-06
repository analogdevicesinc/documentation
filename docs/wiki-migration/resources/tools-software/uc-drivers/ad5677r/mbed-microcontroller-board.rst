AD5677R Evaluation Board and mbed Microcontroller Board
=======================================================

Hardware setup
--------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/uc-drivers/ad5677r/ad5677r_eval_board_chain_with_microcontroller_board.png
   :align: center
   :width: 600px

-  Connect the :adi:`EVAL-AD5677R evaluation board <en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/EVAL-AD5677R.html>` to your microcontroller board. If your microcontroller board has arduino style connectors, you should be able to connect directly the EVAL-5677R. Otherwise wire from your microcontroller board to the Arduino or PMOD connectors on the EVAL-AD5677R.
-  Connect your microcontroller board to your computer.

Software setup
--------------

.. image:: https://wiki.analog.com/_media/resources/tools-software/product-support-software/nanodac_software_layers.jpg
   :align: center
   :width: 250px

-  Make sure you have the `Mbed Online Compiler <https://ide.mbed.com/compiler>`__ installed.
-  Click "Import into Compiler" from the `EVAL-AD568x-AD569x <https://os.mbed.com/teams/AnalogDevices/code/EVAL-AD568x-AD569x/>`__ driver page. Despite its name, this driver library does support the AD5677R.
-  This driver defaults to supporting the AD5686R. To change to the AD5677R, edit the app_config.h file.
-  Ensure your microcontroller board is selected (top right of online-compiler page). Click Compile. This should download a binary file. Find the file in your Downloads folder.
-  In your windows file explorer window, you should see your microcontroller board as a drive on your computer. Copy the binary file into the Mbed enabled board drive. You can also drag and drop the file, like a USB stick.
-  To communicate with the board, use your favorite Terminal program, like `Putty <https://putty.org>`__, `Tera Term <http://ttssh2.osdn.jp/>`__ etc. To use Putty, download and install Putty from `here <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`__. Here are some `installation instructions <https://www.ssh.com/ssh/putty/windows/install>`__. Open Putty and select Serial connection type. Enter the serial port number and a baud rate of 115200. Click Open.
   NOTE: You can find the serial port (which constantly changes, every time you plug a device in), by checking device manager.

   |image1|

-  Reset the controller board and connect.
-  Use the menu provided over the terminal window to access the evaluation board.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/mbed/putty.png
   :width: 400px
