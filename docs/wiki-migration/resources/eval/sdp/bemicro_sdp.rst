BeMicro SDK/SDP Interposer
==========================

Preface
-------

| The BeMicro SDK/SDP Interposer board is an adaptor that allows Arrow’s `BeMicro SDK <https://www.arrow.com/en/datasheets/89166696/arrow-development-tools/bemicrosdk>`_ USB stick to connect to all daughter boards on the SDP Platform. The BeMicro SDK/SDP Interposer provides embedded FPGA system developers the chance to prototype their FPGA + ADI data converter, mixed signal or RF system concept quickly and easily.

More information
----------------

:adi:`BeMicro SDK/SDP Interposer <SDP-BEMICRO>` Information webpage on Analog.com

.. tip::

   This interposer is not an ADI product, and information here is shown to help out ADI's customers who which to evaluate an ADI product with the BeMicro SDK. The BeMicro SDK/SDP Interposer has nothing to do with the SDP Controller Boards, and the BeMicro SDK will not run the SDP product evaluation software. As such, it is not avalible for sale from ADI.


ADI Authorized Distributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `BeMicro SDK/SDP Interposer board <https://www.arrow.com/en/datasheets/2957953708/analog-devices/bemicrosdksdpinterposer>`_ at Arrow
-  `BeMicro SDK/SDP Schematics <https://static5.arrow.com/pdfs/2013/9/26/7/5/38/918/adi_/manual/bemicro-sdp-adapter.pdf>`_ at Arrow

Design Partner/Manufacture
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `Hitex Interposer page <http://www.ehitex.de/p_info.php?xPD=113_129&products_id=622>`_

Product Overview
----------------

| |image1|
| Fig 1 : BeMicro SDK/SDP Adapter Board

| 

| The BeMicro SDK/SDP Interposer routes signals from the BeMicro SDK to the SDP daughter board. There is no additional logic on board. There is a mating edge connector for the BeMicro SDK and a 120 pin connector header for connecting to the SDP daughter boards.
| The BeMicro SDK, developed by Arrow in association with Altera, is a complete soft core embedded processor evaluation system on a USB stick. It makes embedded FPGA design simpler and easier. The BeMicro SDK/SDP Interposer offer unparalleled design flexibility and protection against processor obsolescence in an easy-to-use USB platform that’s ready to go as soon as it’s plugged in.

The complete setup is shown below:

-  BeMicro SDK
-  BeMicro SDK/SDP Interposer
-  SDP Daughtercard

| |BeMicro SDK and SDP Daughtercard seperate|
| Fig 2 : BeMicro SDK and SDP Daughtercard seperate

| |BeMicro SDK and SDP Daughtercard combined|
| Fig 3 : BeMicro SDK and SDP Daughtercard combined

As such, in order to properly use the BeMicro SDK/SDP Interposer, you will need both of:

-  the `BeMicro SDK <https://www.arrow.com/en/datasheets/89166696/arrow-development-tools/bemicrosdk>`_
-  an :adi:`ADI SDP Daughter Board </sdp#exallist>`

Sample Projects/Code
--------------------

| Projects which show basic connectivity between the BeMicro SDK and the ADI SDP Daughter cards are available on the below link
| :doc:`BeMicro Code </wiki-migration/resources/fpga/altera/all_hdl>`

.. |image1| image:: https://wiki.analog.com/_media/resources/eval/sdp/adapter-1.jpg
   :width: 500px
.. |BeMicro SDK and SDP Daughtercard seperate| image:: https://wiki.analog.com/_media/resources/eval/sdp/kompl-top-4.jpg
   :width: 600px
.. |BeMicro SDK and SDP Daughtercard combined| image:: https://wiki.analog.com/_media/resources/eval/sdp/kompl-top-3.jpg
   :width: 600px
