ADRD5161-01Z CANopen reference
==============================

The ADRD5161-01Z module implements CiA 419 Device Profile for Battery Charger and exposes the following CANopen objects:

* ``6000`` batteryStatus
* ``6001`` chargerStatus
* ``6010`` temperature
* ``6052`` ahReturnedDuringLastCharge
* ``6060`` batteryVoltage
* ``6080`` chargerStateOfCharge
* ``6081`` batteryStateOfCharge
* ``6070`` chargeCurrentRequested

The following manufacturer-specific objects provide additional information:

* ``2060`` batteryCellVoltages (array with sub-indices 0-3)
* ``2071`` current
