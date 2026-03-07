Status Bar
==========

The status bar at the bottom of the application gives information about the hardware status, and the most recent operation performed by the application. Four pieces of information are available if a board is in context as shown in bellow.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/Status.PNG
   :alt: Information available in status bar
   :align: right

The state tells the operator the status of the board in

context. It will be updated if the poll state button in the toolbar is clicked. |Poll.png| The value of the state can be any of the following options:    Unavailable – The hardware is not acquired by ACE.

::

   *Unknown - Communication with the hardware is not reliable, it is not setup or the state cannot be determined by the software.

::

   *Uninitialized - The hardware is in its default power on state and has not been configured or setup.

  

::

   *Good - The hardware communication is good, it has been setup and various parameters are as expected.

If a board or chip is in context, then the status bar will report the context at the board level. It will also report the latest transaction completed. This will match the last transaction in the Macro Tools recorded sequence. The time of completion for the latest transaction will be appended to the end of the status.

Error Notification
------------------

The status bar will indicate when communication with hardware fails. When this happens, a popup will open to describe the error.  The popup message can be dismissed by clicking the button, which indicates to ACE that the user is aware of the error.  After that, if the same error happens again, ACE won’t automatically pop up the message again.  When the popup is closed, it can be reopened by clicking the icon.

.. image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/ErrorNotification.png
   :alt: ErrorNotification.png
   :align: right

.. |Poll.png| image:: https://wiki.analog.com/_media/resources/tools-software/ace/understandingtheui/Poll.png
