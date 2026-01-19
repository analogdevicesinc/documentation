:orphan:

..
  Remove :orphan: after including on a page (and this line)
  Typical event attributes

| **/sys/bus/iio/devices/iio:deviceX/events**
| Configuration of which hardware generated events are passed up to user-space.

Threshold Events
----------------

| **<type>Z[\_name]_thresh[\_rising|falling]_en**
| Event generated when channel passes a threshold in the specified
  (\_rising|_falling) direction. If the direction is not specified, then either
  the device will report an event which ever direction a single threshold value
  is called in (e.g. <type>[Z][\_name]\_<raw|input>_thresh_value) or
  <type>[Z][\_name]\_<raw|input>_thresh_rising_value and
  <type>[Z][\_name]\_<raw|input>_thresh_falling_value may take different values,
  but the device can only enable both thresholds or neither. Note the driver
  will assume the last p events requested are to be enabled where p is however
  many it supports (which may vary depending on the exact set requested. So if
  you want to be sure you have set what you think you have, check the contents
  of these attributes after everything is configured. Drivers may have to buffer
  any parameters so that they are consistent when a given event type is enabled
  a future point (and not those for whatever event was previously enabled).

| **<type>Z[\_name]_thresh[\_rising|falling]_value**
| Specifies the value of threshold that the device is comparing against for the
  events enabled by <type>Z[\_name]_thresh[\_rising|falling]_en. If separate
  attributes exist for the two directions, but direction is not specified for
  this attribute, then a single threshold value applies to both directions. The
  raw or input element of the name indicates whether the value is in raw device
  units or in processed units (as \_raw and \_input do on sysfs direct channel
  read attributes).

Rate of Change Events
---------------------

| **<type>[Z][\_name]_roc[\_rising|falling]_en**
| Event generated when channel passes a threshold on the rate of change (1st
  differential) in the specified (\_rising|_falling) direction. If the direction
  is not specified, then either the device will report an event which ever
  direction a single threshold value is called in (e.g.
  <type>[Z][\_name]\_<raw|input>_roc_value) or
  <type>[Z][\_name]\_<raw|input>_roc_rising_value and
  <type>[Z][\_name]\_<raw|input>_roc_falling_value may take different values,
  but the device can only enable both rate of change thresholds or neither. Note
  the driver will assume the last p events requested are to be enabled where p
  is however many it supports (which may vary depending on the exact set
  requested. So if you want to be sure you have set what you think you have,
  check the contents of these attributes after everything is configured. Drivers
  may have to buffer any parameters so that they are consistent when a given
  event type is enabled a future point (and not those for whatever event was
  previously enabled).

| **<type>[Z][\_name]_roc[\_rising|falling]_value**
| Specifies the value of rate of change threshold that the device is comparing
  against for the events enabled by <type>[Z][\_name]_roc[\_rising|falling]_en.
  If separate attributes exist for the two directions, but direction is not
  specified for this attribute, then a single threshold value applies to both
  directions. The raw or input element of the name indicates whether the value
  is in raw device units or in processed units (as \_raw and \_input do on sysfs
  direct channel read attributes).

Magnitude Events
----------------

| **<type>Z[\_name]_mag[\_rising|falling]_en**
| Similar to in_accel_x_thresh[\_rising|_falling]_en, but here the magnitude of
  the channel is compared to the threshold, not its signed value.

| **<type>Z[\_name]_mag[\_rising|falling]_value**
| The value to which the magnitude of the channel is compared. If number or
  direction is not specified, applies to all channels of this type.

Temporal Conditions
-------------------

| **<type>[Z][\_name][\_thresh|_roc][\_rising|falling]_period**
| Period of time (in seconds) for which the condition must be met before an
  event is generated. If direction is not specified then this period applies to
  both directions.

