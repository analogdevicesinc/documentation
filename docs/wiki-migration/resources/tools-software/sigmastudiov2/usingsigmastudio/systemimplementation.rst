:doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio>`

System Implementation
=====================

| SigmaStudio+ introduces a system design approach while programming or configuring components of the system. It provides a top-down perspective of designing the system right from table-top setup to the component level network.
| The diagram below illustrates an example of an A2B network setup where SigmaStudio+ is connected to a three-node A2B network over USBi communication device. To design such a network, users can create a new SigmaStudio+ project and in the System canvas that opens up, drag and drop the platforms required and make the connections as per the setup as shown.
| |image1|
| Double click on the first A2B platform to see the how the components inside the platform are designed.
| |image2|
| Inside the first platform, we have a ADAU1452 processor that drives the ADAA2457 A2B main node, ADAU1761 codec, microphone array and programmable EEPROM devices. This can be seen in the project tree on the right side of the image that lists all the components inside the platform. Within the ADAU1452 processor, customers can design the audio signal flow as per their choice with a wide variety of signal processing modules.
| Inside a single SigmaStudio+ project file, users can

-  Design an audio signal flow, evaluate its execution on the DSP and tune the designed algorithms
-  Configure the processor settings and registers
-  Configure the A2B connectivity registers according to the transceiver manual
-  Configure entire A2B network to perform audio routing from one platform to another through A2B

| |image3|
| Thus SigmaStudio+ serves as a one stop integrated system solution for programming, configuring and tuning software for audio processors, A2B® transceivers and Algorithms/IPs.

.. |image1| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/systemview.png
   :width: 800px
.. |image2| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/platformview.png
   :width: 800px
.. |image3| image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/usingsigmastudio/systemdesign.png
   :width: 800px
