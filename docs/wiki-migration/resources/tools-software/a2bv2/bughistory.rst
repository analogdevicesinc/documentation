Bugs fixed in A2B Plugin for SigmaStudio+ v2.0.0
================================================

-  After discovery, a fault is detected even though no actual fault was introduced, when partial discovery is enabled
-  Partial discovery works only once after the post discovery fault and bus restoration message is incorrect
-  Node is discovered back with open wire faults with no stream configuration
-  Discovery Process getting aborted due to peripheral config failure at the main node
-  Partial Discovery fails after 50 attempts
-  Mailbox transction is not initiated from Host if the Smartsub node is after 3 nodes in network
-  Rediscovery is not attempting morethan once if we remove the power supply on LPS node
-  User doesn't know how much msg queue is left to pass message while using commch
-  Null checks are missed for a2b_msgalloc() which leads to stack crash
-  I2STEST Register for external loopback is not written during discovery for AD2433
-  BP short to Vbat Anomaly handling in apllication
-  Post Discovery faults are not notified to the application - SRF Miss error
-  Mailbox authentication timeout in 10ms where the Sub node host take more time to respond to the Mailbox response
-  Bus Self Discovery is not working as expected
-  Commandlist export has Mailbox register for Main Node
-  Command List export is not including the commands for all slaves
-  Audio is heard only when downloaded from stream configuration for advanced discovery
-  Stack and SS+ behavior are different on peripheral failure
-  Chiron SYNC issue when only a SOFTRST is provided at the main node
-  Partial discovery fails when a node is dropped and there is no upstream from the dropped node
-  Security Vulnerabilities Addressed - nanopb version(To encode and decode dat) migrated to 0.4.9.1
