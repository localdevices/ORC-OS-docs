.. _services:

Background services
-------------------

Background services are processes that run in the background as entirely
independent processes from the web server. They can be used to run any kind of
additional process encapsulated in a script that you like. Examples include:
* Running a script, that monitors the state of your battery and reports
  this in the ``misc`` field of the time series table.
* Running a script that continuously monitors the database and if a new record
  appears, send it to a separate connected logger or an API of a third-party
  service.
* Handling power management, so that the device turns on and off at certain 
  times of the day**

A service can be created in the web interface as developer and this process
is described in the section on 
:ref:`creating background services <devel_services>`.

Once it is created, you as a user, can modify its parameters, and enable, 
disable, start, stop or restart the service. You can also read about the 
service in the README section and see the logs of the script.

Each service has its own page in the web interface, where you can do all of the 
above. All of the services will be found under the "Settings" menu under 
"Background services". Just click on the one you wish to manage and you will
be taken to the appropriate page.

Starting, stopping, enabling and disabling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We here briefly explain what this means.

* Start: if the service does not run, you can start it. The script, connected
  to the service will start once, run, and if it is non-persistant, stop again.
  You can see this with the indicator under "Service status". 
* Stop: if the service is still running, you can stop it. This will stop the 
  script immediately. You can see this with the indicator under "Service 
  status".
* Enable: If the service is not enabled, you can enable it. This means that the
  service will automatically start once the device is restarted. You can see
  this with the indicator under "Service enabled". Clicking on "Enable" will not
  also automatically start the service in the current session. 
  You will have to click on "Start" for this.
* Disable: If the service is enabled, you can disable it. This means that the
  service will no longer start once the device is restarted.
* Restart: If the service is running, you can restart it. This will stop the 
  script immediately and start it again. This is required when you have updated 
  the parameters (see below).

Parameters
^^^^^^^^^^
The parameters of a service are stored as environment variables. You can change
the value of these environment variables in the web interface. Once you have
changed them, click on "Update parameters" to save these to environment 
variables. Only after that will a restart change the parameters in the script.

Example
^^^^^^^

As an example, you may want to connect 3rd party devices to your ORC-OS device,
for instance an additional sensor, a IP camera that provides videos, or a 
separate logger. All of these will consume power, so you may only want to turn
these on a certain intervals and in each interval for a brief period. For this,
we have designed a "Relay management service". You can get this service running
on your device by referring to the section on 
:ref:`creating background services <devel_services>` where the entire service
and script is provided. After this service is added you should see it appear 
in the Settings menu, and its management page should look like the page shown
below.

INSERT SCREENSHOT HERE.

You will see that a README is provided in Markdown language, which gives
explanations how to connect a relay board, and how to configure the service.
All the configuration should be easy once you have read the README. 
Once you have set up some example parameters, also open and close the "Logs"
a few times. You will see that the logs produce messages that may hint on 
possible problems, or that may confirm that the parameter do what you expect.
We highly recommend to set this up and play with the settings before going
into the field with your device.


