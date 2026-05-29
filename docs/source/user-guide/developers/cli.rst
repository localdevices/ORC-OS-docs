.. _devel_cli:

Command-line interface
======================

A simple yet effective command-line interface (CLI) is available for ORC-OS. 
It can conveniently be used to list, create or delete available records,
reset your password (in case you DID forget it 😉), update your database
in case automated updates did not fully update your database, and import, export
or delete background services using json files. To get an overview of the CLI
sections, simply run:

.. code-block:: bash

    $ orc --help

.. program-output:: orc --help

Password reset
--------------
Simply type the following command to reset your password:

.. code-block:: bash

    $ orc password_reset

This deletes the password and once you attempt logging in, you will see the
initial screen to set your password. This action will not delete any records
so all of your previous work will be preserved.

Database actions
----------------

Database actions are under the ``db`` sub-command. For an overview run:

.. code-block:: bash

    $ orc db --help

This will give:

.. program-output:: orc db --help

Most of the commands speak for themselves. Please note that ``downgrade`` is 
not guaranteed to work. In order to migrate to the most recent version following
the currently installed version of ORC-OS, you should simply run:

.. code-block:: bash

    $ orc db migrate

You may supply a specific version also, e.g. to perform stepwise migrations.
This can be done by adding the ``--revision`` option followed by the version.
To know which versions are available, you run:

.. code-block:: bash

    $ orc db history

The output should give something like this:

.. program-output:: orc db history

The top ``<head>`` is the most recent version, and the bottom ``<base>`` is the 
oldest version.

Creating, listing and deleting videos
-------------------------------------

These actions are all under the ``video`` sub-command. For an overview run:

.. code-block:: bash

    $ orc video --help

This will give:

.. program-output:: orc video --help

The ``add``, ``delete`` and ``list`` commands are pretty self-explanatory. 
The ``add-config`` adds a video configuration to the database. 

.. code-block:: bash

    $ orc video add-config --help

.. program-output:: orc video add-config --help
    
This command expects a video configuration to be supplied by:

* a JSON file with the camera configuration details
* a JSON or YAML file with the recipe
* one or two CSV or GeoJSON formatted cross section files for discharge 
  (mandatory) and optical water level estimation (optional).

The files typically come from exports from the web interface, or from 
`pyorc`_ projects. Finally the record ID of a sample video should be provided
so that the video configuration is attributed to a certain video record.
This is important for the web interface to know which video configuration 
belongs to which video.

.. _pyorc: https://github.com/localdevices/pyorc

.. note::

    Future updates will have a special ``video-config`` sub-command.
    We are also planning a command ``orc video run`` to run the video 
    processing from the CLI, for testing or large reanalysis purposes.

Importing, exporting, listing and deleting services
---------------------------------------------------

To understand better what background services are and how to create them
from scratch in the web interface, please read the section on 
:ref:`background services <devel_services>`. 

The actions for services are all under the ``service`` sub-command. For an 
overview run:

.. code-block:: bash

    $ orc service --help

This will give:

.. program-output:: orc service --help

The ``import`` and ``export`` commands are used to import or export background
services using JSON files. Usually this is used to first export a service
that runs on an existing device, which you might want to replicate on another
device, without having to go through the web interface to set up the service 
from scratch. If your service is already entire deployed, including a set of
parameter as environment variables, and a running Bash or Python script,
then during export, the entire script and set enrionment variables will be 
exported in the JSON file so that the entire service is preserved in one single
file. When you import this JSON file on another device, the service will be
created without deploying the script and environment variables. 
If you add the ``--deploy`` argument, the service will be 
deployed with the same script and environment variables. If you do not supply
this, then only the skeleton will be setup, but no script will be added,
and environment variables will go to default or null.

You may also re-import the service if you have made modifications. Existing
services with the same short name will then be overwritten.

For security reasons, the background service will not be started or enabled
automatically. You can start it from the web interface by one single click.

The ``list`` and ``delete`` commands are used to show all existing services
or to delete a service by its ID. To find the ID, first list existing services
and note down the ID of the service you wish to delete.

