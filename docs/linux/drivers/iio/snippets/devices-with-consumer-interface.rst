:orphan:

..
  Remove :orphan: after including on a page (and this line)
  IIO devices with trigger consumer interface

If deviceX supports triggered sampling, it’s a so called trigger consumer and
there will be an additional folder */sys/bus/iio/device/iio:deviceX/trigger*.
In this folder there is a file called current_trigger, allowing controlling and
viewing the current trigger source connected to deviceX. Available trigger
sources can be identified by reading the name file
*/sys/bus/iio/devices/triggerY/name*. The same trigger source can connect to
multiple devices, so a single trigger may initialize data capture or reading
from a number of sensors, converters, etc.

.. tip::

   **Trigger Consumers:**
   Currently triggers are only used for the filling of software ring buffers
   and as such any device supporting INDIO_RING_TRIGGERED has the consumer
   interface automatically created.

**Description:** Read name of triggerY

.. shell::

   /sys/bus/iio/devices/triggerY
   $cat name irqtrig56

**Description:** Make irqtrig56 (trigger using system IRQ56, likely a GPIO IRQ),
to current trigger of deviceX

.. shell::

   /sys/bus/iio/devices/iio:deviceX/trigger
   $echo irqtrig56 > current_trigger

**Description:** Read current trigger source of deviceX

.. shell::

   /sys/bus/iio/devices/iio:deviceX/trigger
   $cat current_trigger irqtrig56


