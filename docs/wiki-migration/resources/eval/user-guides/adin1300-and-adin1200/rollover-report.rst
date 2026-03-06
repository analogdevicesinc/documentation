KSZ8081 to ADIN1200 Rollover Guide
==================================

Introduction
------------

This report will give the details on how to use the ADIN1200 as a second source to Microchip’s KSZ8081. In summary, the ADIN1200 is not pin-to-pin compatible with KSZ8081 but there can be layout proposals to use the ADIN1200 with proper consideration of the original layout on KSZ8081. The document explains the similarities and differences in pin functions with features and layout. Please use this document in conjunction with the :doc:`ADIN1200 Circuit and Layout Considerations </wiki-migration/resources/eval/user-guides/adin1300-and-adin1200/layout-considerations>` and the ADIN1200 Datasheet.

Review of KSZ8081
~~~~~~~~~~~~~~~~~

The KSZ8081MNX is a 10/100 Ethernet PHY with a MAC of MII, whereas the KSZ8081RNB is a 10/100 Ethernet PHY with a MAC of RMII.

|image1| **Figure 1: KSZ8081MNX Pin Assignment**

|image2| **Figure 2. KSZ8081RNB Pin Assignment**

As compared to ADIN1200, the KSZ8081 sets MAC Interface thru different packages. ADIN1200 MAC Interface is selected using a configuration pin.

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/ksz8081rnb.jpg
   :width: 400px
.. |image2| image:: https://wiki.analog.com/_media/resources/eval/user-guides/adin1300-and-adin1200/ksz8081rnb.jpg
   :width: 400px
