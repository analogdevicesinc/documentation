..
  IIO device files

Each and every IIO device, typically a hardware chip, has a device folder under
*/sys/bus/iio/devices/iio:deviceX*.
Where X is the IIO index of the device. Under every of these directory folders
reside a set of files, depending on the characteristics and features of the
hardware device in question.

These files are consistently generalized and documented in the IIO ABI
documentation. In order to determine which IIO deviceX corresponds to which
hardware device, the user can read the name file
*/sys/bus/iio/devices/iio:deviceX/name*.
In case the sequence in which the iio device drivers are loaded/registered is
constant, the numbering is constant and may be known in advance.
