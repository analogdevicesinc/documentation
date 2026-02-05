:orphan:

..
  Remove :orphan: after including on a page (and this line)
  _Buffer management

The Industrial I/O subsystem provides support for various ring buffer based data
acquisition methods. Apart from device specific hardware buffer support, the
user can chose between two different software ring buffer implementations. One
is the IIO lock free software ring, and the other is based on Linux kfifo.
Devices with buffer support feature an additional sub-folder in the
*/sys/bus/iio/devices/deviceX/* folder hierarchy.
Called deviceX:bufferY, where Y defaults to 0, for devices with a single buffer.

Every buffer implementation features a set of files:

| **length**
| Get/set the number of sample sets that may be held by the buffer.

| **enable**
| Enables/disables the buffer. This file should be written last, after length
  and selection of scan elements.

| **watermark**
| A single positive integer specifying the maximum number of scan elements to
  wait for. Poll will block until the watermark is reached. Blocking read will
  wait until the minimum between the requested read amount or the low water mark
  is available. Non-blocking read will retrieve the available samples from the
  buffer even if there are less samples then watermark level. This allows the
  application to block on poll with a timeout and read the available samples
  after the timeout expires and thus have a maximum delay guarantee.

| **data_available**
| A read-only value indicating the bytes of data available in the buffer. In the
  case of an output buffer, this indicates the amount of empty space available
  to write data to. In the case of an input buffer, this indicates the amount of
  data available for reading.

| **length_align_bytes**
| Using the high-speed interface. DMA buffers may have an alignment requirement
  for the buffer length. Newer versions of the kernel will report the alignment
  requirements associated with a device through the ``length_align_bytes``
  property.

| **scan_elements**
  The scan_elements directory contains interfaces for elements that will be
  captured for a single triggered sample set in the buffer.

