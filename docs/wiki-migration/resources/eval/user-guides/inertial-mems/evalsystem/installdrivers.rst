How to Install Drivers (Without an Installer)
=============================================

This page describes how to install drivers without an installer, as in the case of the :doc:`ADXL362 Datalogger / Development Board </wiki-migration/resources/eval/user-guides/inertial-mems/accelerometers/adxl362/eval-adxl362z-db>`.

|

.. tip::

   Use the Table of Contents on the right to scroll to instructions for your operating system.

   | Note that your system may behave slightly differently, but the overall procedure remains the same.


Windows 7
---------

-  Connect the board to your computer via a USB cable.
-  If prompted to install drivers, choose **Install from a list or specific location (Advanced)**, then click **Next**. If no prompt appears, find the device in your computer's **Device Manager**:

.. container:: box

   -   Click the Windows button in the bottom left corner of the screen to open the Start menu.
   -   Right-click on **My Computer**, and select **Manage**. In the warning screen that comes up, click **Yes**.
   -   In the window that opens, select the **Device Manager** from the list on the left-hand side.
   -  The board will show up in the Device Manager as an **Unknown Device**. (If it shows up under **Ports (COM & LPT)** with a valid COM port, this means the drivers have already been installed and are working properly.)
   -  Right-click on the Unknown Device and select **Update Driver Installation...**. Follow the remaining instructions below.
   


-  Select **Let me pick...**, then click **Next**.

.. container:: indent


   ..

|image1|

-  Select **Show All Devices**, and click **Next**.

.. container:: indent


   ..

|image2|

-  Click **Have Disk...**.

.. container:: indent


   ..

|image3|

-  On the screen that opens, select **Browse...**

.. container:: indent


   ..

|image4|

-  Navigate to the ``.inf`` file on your hard drive or CD.

.. container:: indent


   ..

|image5|

-  Click **Open**, then in the **Install From Disk** prompt, click **OK**.

.. container:: indent


   ..

|image6|

-  Select "ADI Inertial Sensor Development Board" in the **Model** list, and click **Next >**.

.. container:: indent

   \


   |image7|

-  Respond **Continue Anyway** or **Install** to the warning.

.. container:: indent


   ..

|image8|

-  Click **Close** to complete the USB driver installation.

.. container:: indent

   
   |image9|\


--------------

Windows XP
----------

-  Connect the board to your computer via a USB cable.
-  When prompted to install drivers, choose **Install from a list or specific location (Advanced)**, then click **Next**.

.. container:: indent


   ..

|image10|

-  Select **Don't search. I will choose the driver to install**, then click **Next**.

.. container:: indent


   ..

|image11|

-  Select **Ports (COM & LPT)**, and click **Next**.

.. container:: indent


   ..

|image12|

-  Click **Have Disk...**.

.. container:: indent


   ..

|image13|

-  On the screen that opens, select **Browse...**.

.. container:: indent


   ..

|image14|

-  Navigate to the ``.inf`` file on your hard drive or CD and click **Open**.

.. container:: indent


   ..

|image15|

-  Click **Open**, then in the **Install From Disk** prompt, click **OK**.

.. container:: indent


   ..

|image16|

-  Select "ADI Inertial Sensor Development Board" in the **Model** list, and click **Next >**.

.. container:: indent


   ..

|image17|

-  Respond **Continue Anyway** to the warning.

.. container:: indent


   ..

|image18|

-  Click **Finish** to complete the USB driver installation.

.. container:: indent


   ..

|image19|

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_5.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_6.jpg
   :width: 400px
.. |image3| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_7.jpg
   :width: 400px
.. |image4| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_8.jpg
   :width: 400px
.. |image5| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_9.jpg
   :width: 400px
.. |image6| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_9p1.jpg
   :width: 400px
.. |image7| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_10.jpg
   :width: 400px
.. |image8| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_11.jpg
   :width: 400px
.. |image9| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/install_done.jpg
   :width: 400px
.. |image10| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall0.png
   :width: 400px
.. |image11| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall1.png
   :width: 400px
.. |image12| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall2.png
   :width: 400px
.. |image13| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall3.png
   :width: 400px
.. |image14| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall4.png
   :width: 400px
.. |image15| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall5.png
   :width: 400px
.. |image16| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall6.png
   :width: 400px
.. |image17| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall7.png
   :width: 400px
.. |image18| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall8.png
   :width: 400px
.. |image19| image:: https://wiki.analog.com/_media/resources/eval/user-guides/inertial-mems/evalsystem/winxpinstall9.png
   :width: 400px
