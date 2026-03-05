:orphan:

..
  Remove :orphan: after including on a page (and this line)
  Typical ADC scan elements

| **in_voltageX_en / in_voltageX-voltageY_en / timestamp_en:**
| Scan element control for triggered data capture. Writing 1 will enable the
  scan element, writing 0 will disable it

| **in_voltageX_type / in_voltageX-voltageY_type / timestamp_type:**
| Description of the scan element data storage within the buffer and therefore
  in the form in which it is read from user-space. Form is
  [s|u]bits/storage-bits. s or u specifies if signed (2's complement) or
  unsigned. bits is the number of bits of data and storage-bits is the space
  (after padding) that it occupies in the buffer. Note that some devices will
  have additional information in the unused bits so to get a clean value, the
  bits value must be used to mask the buffer output value appropriately. The
  storage-bits value also specifies the data alignment. So u12/16 will be a
  unsigned 12 bit integer stored in a 16 bit location aligned to a 16 bit
  boundary. For other storage combinations this attribute will be extended
  appropriately.

| **in_voltageX_index / in_voltageX-voltageY_index / timestamp_index**
| A single positive integer specifying the position of this scan element in the
  buffer. Note these are not dependent on what is enabled and may not be
  contiguous. Thus for user-space to establish the full layout these must be
  used in conjunction with all \_en attributes to establish which channels are
  present, and the relevant \_type attributes to establish the data storage
  format.

