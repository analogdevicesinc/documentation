| 
| :doc:`Click here to return back </wiki-migration/resources/tools-software/sigmastudiov2/tutorials>`
| ======Remotely Download and Tune Target Platform======

.. note::

   This feature is available from SigmaStudio+ 1.2.0


SigmaStudio+ can remotely download and tune target platforms. SigmaStudio+ supports two types of remote connections.

-  **Remote setup using Scripting**: The SigmaStudio+ is running on remote machine ‘A’ and hardware is connected to the same machine. This can be accessed from another machine ‘B’ on the same network using Scripting.
-  **Remote setup using TCP/IP**: Hardware is connected to a remote machine ‘A’ and SigmaStudio+ is running on machine ‘B’. It is possible to download and tune the target connected to a remote machine 'A' from SigmaStudio running on machine 'B' using TCP/IP communication.

| 
| ====Remote setup using Scripting==== While using scripting, SigmaStudio+ with hardware setup will be running on machine ‘A’ (remote machine) and will act as the scripting server. A scripting client application should be hosted in machine ‘B’. Refer to :doc:`scripting </wiki-migration/resources/tools-software/sigmastudiov2/usingsigmastudio/scripting>` for more details on scripting. Example client applications implemented in C# and Python are provided as part of the package. These example applications (CSharp client / Python client) can be launched using windows command prompt or any suitable IDE.

IP Address and Port Number of the remote machine should be entered are arguments in the client application to establish connection. Default port number is 9090. A different port number for connection can be setup in SigmaStudio+ under the Settings window. Below message appears after a successful connection.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/remote1.png
   :align: center

Type command ‘SSPAPI’ and press enter key to get the list of all APIs supported in the client application.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/remote2.png
   :align: center

To execute any of the listed API, user has to provide the API name along with required argument. e.g. To perform OpenProject action, user needs to enter the OpenProject keyword along with the file path as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/remote3.png
   :align: center

This command will open the project in the remote machine. Use API name along with ‘-Help’ keyword to get help. API argument details will be displayed as shown below.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/remote4.png
   :align: center

| Use ‘Exit’ keyword to terminate the client application.
| ====Remote setup using TCP/IP==== SigmaStudio+ supports TCP/IP communication to establish remote connection where hardware is connected to the remote machine ‘A’ and SigmaStudio+ application is running on the host machine ‘B’. ‘SimpleServer’ TCPIP example server is provided as an example. This application running on the remote machine will receive the TCP/IP packets from SigmaStudio and convert them into SPI packets using USBi.

.. important::

   Currently this feature is supported only on ADAU145x and ADAU146x targets


The application will display the remote machine IP address and port number when launched.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/remote5.png
   :align: center

Open SigmaStudio+ and create a schematic. Use TCP/IP as the communication device. Double click on the TCP/I shape to launch the TCP/IP configuration. Enter the IP address and port number of the remote machine.

.. image:: https://wiki.analog.com/_media/resources/tools-software/sigmastudiov2/tutorials/remote6.png
   :align: center

Then connect to the server application using by clicking on the 'Open Connection' button. Once connection has been established, server will notify the user by displaying the successful message. Users can now perform Link-Compile-Download and Tune parameters on the schematic. SigmaStudio+ will send the packets to the remote machine using TCP/IP. The SimpleServer application will reads or write the TCP/IP payload using USBi.
