IIO Plugin for Visual Analog
============================

.. important::

   This software is `deprecated <https://en.wikipedia.org/wiki/Deprecation>`_ and is no longer supported/tested. It is described here for historical purposes only. If you have questions, please try things out with `IIO Scope <https://wiki.analog.com/../../iio_oscilloscope>`_, or ask questions on :ez:`EngineerZone <linux-device-drivers/linux-software-drivers>`.


About
-----

IIO Plugin is a :adi:`Visual Analog <en/design-center/interactive-design-tools/visualanalog.html>` component designed to create a communication channel between Visual Analog and the evaluation board attached to an embedded platform for the purpose of streaming data from the ADCs available on the board. The plugin can be used in conjunction with signal analysis components provided by Visual Analog in order to evaluate the performance of the board.

Installation
------------

The IIO plugin depends on the :doc:`libiio </wiki-migration/resources/tools-software/linux-software/libiio>` library which needs to be installed separately in order for the plugin to work.

Downloads
=========

.. admonition:: Download
   :class: download

   
   -  `IIO Plugin installer (old) <http://swdownloads.analog.com/cse/va/VA_IIOPluginSetup.exe>`_
   -  `IIO Plugin for Visual Analog <https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_iiopluginsetup.zip>`_
   


.. note::

   
   -  The old plugin can be used by users that still run old versions of libiio on their targets. It also installs Libiio locally, next to the plugin.
   -  The new plugin works with Libiio 0.10 which needs to be installed separately. \**First, look for 'LibIIO Setup x86' in 'Programs and Features' and uninstall it, then uninstall the old IIO plugin, if exists \*\* and then install the new one.
   


Setup
=====

In order to establish the connection between the host PC and the target, there are several steps you need to follow on both sides.

Target side:

-  Make sure the latest version of libiio is installed on target by following these :doc:`instructions </wiki-migration/resources/tools-software/linux-software/libiio>`.
-  Determine the IP address of the target by typing ``ifconfig`` in a terminal/console.

PC side:

-  Install :adi:`Visual Analog <en/design-center/interactive-design-tools/visualanalog.html>` on your system.
-  Run the Visual Analog IIO Plugin installer available in the `Downloads <https://wiki.analog.com/>`_ section.
-  Fill the **Server IP Address** field of the plugin configuration panel, with the IP address of the target.

User Guide
==========

-  Run :adi:`Visual Analog </en/design-center/interactive-design-tools/visualanalog.html>`.
-  Choose **Blank Canvas** as a template.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_new_canvas.png
   :align: center

-  To use the plugin, drag the **IIO Client** element onto the canvas surface. The element can be found on the left side of the screen, in the **Components** tree view, under the **Board Interfaces** category.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_plugin_component_select.png
   :align: center

-  Click on the **Settings** icon of the component to bring up the configuration panel of the plugin.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_plugin_component_layout.png
   :align: center

-  Set the **IP Address** field in the **Server** section with the network address of the remote device and click the **Connect** button.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_plugin_connect.png
   :align: center

-  A successful network connection to the remote target will make the **Data** section of the configuration panel become active. There are a number of configurations that can be made through the plugin:

   -  **Device**: Allows to choose between IIO ADC devices available on the remote target.
   -  **Sample frequency (MHz)**: The sampling frequency that the ADC is configured with. Read only.
   -  **Channels**:

      -  **Channels**: Name of the channel of to the selected device.
      -  **Enable**: Whether data should be captured on this channel or not.
      -  **Samples**: Number of samples to be captured every run.
      -  **Test Enable**: Whether the Test Modes should apply or not.
      -  **Test Modes**: Allows to choose one of the test modes available for the device.

-  A click on the **OK** button will use the above properties to configure the device and then close the configuration panel. A click on the **Apply** button will configure the device immediately but keep the configuration panel open. A click on the **Cancel** button will close the configuration panel without configuring the device and without remembering the latest user changes.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_plugin_settings.png
   :align: center

-  The component will be the data source of your signal chain. To connect it to output components such as a Graph or data format components such as an Input Formatter use the right sided connectors of the component. You should use as many connectors as the number of enabled channels otherwise the extra connectors will be invalidated (the grey square icon will turn white and when the Run or Continuous Run buttons are pressed the software will mark the lines as invalid using red crosses).

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_plugin_component_pins.png
   :align: center

-  The default height of the component allows for a maximum of 4 connectors. In certain situations where a device has more channels you can always resize the height of the component to get access to as many connectors as you need.

.. image:: https://wiki.analog.com/_media/resources/tools-software/linux-software/libiio/clients/va_plugin_extend_connectors.png
   :align: center
