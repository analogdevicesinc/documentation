:orphan:

..
  Remove :orphan: after including on a page (and this line)
  Event Management

The Industrial I/O subsystem provides support for passing hardware generated
events up to userspace.

In IIO events are not used for passing normal readings from the sensing devices
to userspace, but rather for out of band information. Normal data reaches
userspace through a low overhead character device - typically via either
software or hardware buffer. The stream format is pseudo fixed, so is described
and controlled via sysfs rather than adding headers to the data describing what
is in it.

Pretty much all IIO events correspond to thresholds on some value derived from
one or more raw readings from the sensor. They are provided by the underlying
hardware.

**Examples include**:

-  Straight crossing a voltage threshold
-  Moving average crosses a threshold
-  Motion detectors (lots of ways of doing this).
-  Thresholds on sum squared or rms values.
-  Rate of change thresholds.
-  Lots more variants...

Events have timestamps.

**The Interface**:

-  Single user at a time.

-  Simple chrdev per device (aggregation across devices doesn't really make
   sense for IIO as you tend to really care which sensor caused the event rather
   than just that it happened.)

**The format is**:

.. code:: c

   /**
    * struct iio_event_data - The actual event being pushed to userspace
    * @id:     event identifier
    * @timestamp:  best estimate of time of event occurrence (often from
    *      the interrupt handler)
    */
   struct iio_event_data {
       u64 id;
       s64 timestamp;
   };

