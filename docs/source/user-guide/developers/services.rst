.. _devel_services:

Creating background services
============================


Background services are processes that run in the background as entirely
independent processes from the web server. They can be used to run any kind of
additional process that you like. Examples include:

* Running a script, that monitors the state of your battery and reports
  this in the ``misc`` field of the time series table.
* Running a script that continuously monitors the database and if a new record
  appears, send it to a separate connected logger or an API of a third-party
  service.
* Handling power management, so that the device turns on and off at certain 
  times of the day**

.. tip::

    Creating a new service requires the web server to be in development mode. 
    The ready-to-flash images from Rainbow Sensing can be started in development
    mode by simply pressing the on-board power button briefly. This will start
    the web server in development mode, and even start a WiFi Hotspot so that
    you can easily connect to your device. No need to log into the back-end!

A service consists of a set of parameters, stored as environment variables, 
and a Bash or Python script, which is run once the service is started. 
Other things that help define the service are a short name, a description, and a 
README (which can contain Markdown language). Each parameter in turn also has
additional properties, including the environment variable it is linked to, 
the type (boolean, integer, float or string), whether it is mandatory or not, 
and a default value. The parameters allow for user-side configuration of the
service.

A new service can be created from the web interface but only when the web server
is running in development mode. The ready-to-flash images require a simple button
press to switch to development mode. If you have built your own device
follow these instructions:

To run the web server in development mode, set 
the ``ORC_DEV_MODE`` environment variable to ``1`` (true). Then run the 
web service interactively. Usually you do this with uvicorn, as follows:

.. code-block:: bash

    # set the DEV MODE environment variable to 1 (true)
    export ORC_DEV_MODE=1
    uvicorn orc_api.main:app --host 0.0.0.0 --port 5000 --workers 1

The port number is important because the web front-end is usually configured to 
look for the web server on port 5000. If you have chosen a different port
in your nginx configuration, then change the port to this port instead.

Create a new service
--------------------

Once the webserver is in development mode, navigate to Settings --> 
Manage Services.

.. screenshot:: http://localhost:5173/services
  :browser: chromium
  :viewport-width: 1920
  :viewport-height: 1080
  :color-scheme: dark
  :status-code: 200,302

  The Manage Services page, where you can create, edit, delete and deploy 
  background services.

Here you can create a new service, or edit or delete an existing one. When
you create a new service, you will be asked for a short name (only small letters
and dashes, no other special characters, spaces or capital are allowed), a
long name, Service type (run once or at intervals), a description and a README.

.. figure:: ../../_images/_screenshots/services_create.png
    :align: center
    :width: 100%
    
    The form to create a new background service.

A created service can be edited with the "Edit" button.

Once created, you can add parameters, change their value, deploy the service,
and start and stop it. This is explained in more detail below.

Adding parameters
-----------------
To manage a service, click on the "Manage" button of the service you wish
to manage. This will reveal the following page:

.. screenshot:: http://localhost:5173/services/3
  :browser: chromium
  :viewport-width: 1920
  :viewport-height: 1080
  :color-scheme: dark
  :status-code: 200,302

Parameters are added by clicking the "Add parameter" button. A form will be 
brought up where can fill in the details.

.. figure:: ../../_images/_screenshots/parameter_create.png
    :align: center
    :width: 100%
    
    The form to add a parameter to a background service.

The short name must be capitalized
and can only contain "_" as a special character. This is because the
short name will be used as the name of the environment variable that is linked
to this parameter. The long name can be anything you want. 
The type can be boolean, integer, float or string. The default value must be of
the type you have specified. You may also specify whether the parameter is 
mandatory or not by selecting or deselecting "Nullable". 
The description may be important for users, explain here carefully what the
parameter does and how it should be used.

Once saved, the parameter will appear in the list of parameters and you may 
change its behaviour by clicking "Edit". You can also change the value of the 
parameter for this service by entering it in the designated field. The parameter
values will be stored as a list of environment variables when you click on 
"Update parameters". Once you have done this, each time you revisit this page,
the fields will be filled with the values you have defined. If you change the
parameter values and click "Update parameters" again, the new values will be 
stored and will overwrite the previous values. Changing the parameters can
also be done by the user when not in developers mode. This allows you to 
quickly change parameters if this is needed while the device is in operation.

Deploying the service
---------------------
At this stage the service contours are defined, but the service is not yet 
deployed: a script must be run as part of the service, and this script must
be encapsulated in a so-called "service file". To do this, click on "Deploy".
This will bring you to the deployment page, where you can upload a script.
A service file will be generated automatically and once this is done, you will
be able to start, stop, enable disable and restart the service. Again, this
can be done even if not in developers mode, so that you can quickly update
parameters and then restart the service. You may also want to interrupt a 
service that is running. This is for instance very important if you want to
have a longer look at the device and a service is running that power cycles
the device. If you interrupt this, you will have more time to check the device.
Once you are done you can restart the service again. The meaning of the buttons
is described in the general description of the :ref:`services pages <services>`
for normal users.

We have prepared a full example of a service for managing power to external devices
via relays. To get a better understanding, please implement this service yourself
by following the instructions in the next section.

