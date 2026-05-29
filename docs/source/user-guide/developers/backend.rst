.. _devel_database:

Console and virtual environment
===============================

.. note::

  The operations mentioned in this section require knowledge of the linux command
  line interface and python virtual environments. If you are not familiar with 
  these, we recommend to read up on these topics first, for example through the 
  `Raspberry Pi documentation`_ and `Python virtual environments documentation`_.

Accessing the back-end
----------------------

For direct access to the files and database and command-line interface,
you will require a terminal console and a virtual python environment to 
interact with the software. You must be connected to the device, either through
a local network connection, a direct connection or via a remote connectivity
option. In most cases, you have three options to access the back-end: 

1. Terminal access via Secure Shell (SSH).
2. Access to a desktop environment via a remote desktop protocol (RDP) client.
   Assuming you are using Raspberry Pi here, you will need the
   `RealVNC client`_ for your computer's platform to access the desktop 
   environment of the Raspberry Pi.
3. Direct access to the Raspberry Pi by connecting a monitor, keyboard and 
   mouse.

If you have acquired a Rainbow Sensing ready-to-flash image, you will have 
received a username and password for accessing via SSH and VNC. If you have 
deployed ORC-OS yourself, please use your own defined username and password.

Within the desktop environment, you may open a console by looking for an icon
that looks like a terminal :octicon:`terminal;1em`. 

.. note::

    For further instructions on SSH and VNC access to a Raspberry Pi, please read
    on how to gain access, we refer to `Raspberry Pi documentation`_.

Location of files and database
------------------------------
By default, the ORC-OS software is installed in the home directory of the main
user (e.g. ``pi``) in a hidden folder called ``.ORC-OS``. This makes the full path
accessible as follows:

.. code-block:: bash

    cd $HOME/.ORC-OS

or:

.. code-block:: bash

    cd ~/.ORC-OS

Within this folder, you will find several default locations for database, 
incoming videos (when you import and run videos automatically) and stored
files per video after importing and running. This is organized as follows:

.. code-block:: text

    ~/.ORC-OS/
    ├── orc-os.db
    ├── tmp/
    ├── uploads/
    │   └── incoming/  # folder where incoming videos are expected
    │   └── videos/
    │   │   └── <YYYYMMDD>/
    │   │       ├── <id>
    │   │           ├── <video_filename>.<ext>  # original video file
    │   │           ├── <video_filename>_thumb.jpg  # thumbnail
    │   │           ├── cross_section.geojson  # parsed cross section
    │   │           ├── pyorc.log  # log file for processing of this video
    │   │           └── output/  # folder with processed outputs, netcdf files
    │   │               └── ...
    │   └── logs/  # folder with rotating log files, max 10 files, max 10MB per file
    │       ├── orc-os.log  # current log file
    │       ├── orc-os.log.1  # previous log file
    │       ├── ...
    │       └── orc-os.log.<nr>  # all previous log files
    └── ...

The database file is called ``orc-os.db`` and is located in the main folder.
This file is a standard sqlite3 database file, and you can access it with any 
sqlite3 client.

The ``uploads`` folder contains the incoming videos (not organized)
and the processed videos (organized per day and per video record, using the 
video record id). If you wish to find a specific video, then you must look for
the day of the video and its id in the table `video` in the database, and then 
look for the corresponding folder ``uploads/videos/<YYYYMMDD>/<id>``. In this
folder, you will find the original video file, the thumbnail, the parsed cross
section (and cross section for water level estimation if relevant) and a log
file for the processing of this video. If you have run the video processing,
you will also find a folder with processed outputs, including netcdf files for 
2D gridded surface velocities and 1D cross-section velocities and discharge.

Environment variables
---------------------
The web server can be run with user specific environment variables, for example
to change the location of certain folders. These are described below.

.. list-table::
    :header-rows: 1
    :widths: 25 35 40

    * - Environment variable
      - Description (default)
      - Default value
    * - ``ORC_SECRET_KEY``
      - The secret key for the web server, used for session management and
        security. It is recommended to set this to a random string for 
        production use. Take care that you always use the same string 
        afterwards, otherwise you will not be able to validate your password
      - ``ORC_DEFAULT_KEY``
    * - ``ORC_HOME``
      - The location of the main ORC-OS folder. This is where the database and
        uploaded videos are stored by default. You may change this for instance
        if you want to store the database and videos on an additional mounted
        drive like an SSD drive.
      - ``$HOME/.ORC-OS``
    * - ``ORC_UPLOAD_DIRECTORY``
      - The location where incoming videos are expected and where processed videos are stored.
      - ``$ORC_HOME/uploads``
    * - ``ORC_INCOMING_DIRECTORY``
      - The location where incoming videos are expected.
      - ``$ORC_UPLOAD_DIRECTORY/incoming``
    * - ``ORC_SERVICE_DIRECTORY``
      - The location where background service files and scripts are stored.
      - ``$ORC_HOME/services``  
    * - ``ORC_DEV_MODE``
      - Whether to start the web server in developers mode, which allows you to
        access additional features on the front-end. This is usually only needed
        temporarily to set up or change a background service. Set to ``1``
        (true) to activate developers mode, and to ``0`` (false) to deactivate
        it.
      - ``0`` (false)

In bash, you can set these environment variables by running the following command,
adapting the values to your needs:

.. code-block:: bash
    
    export ORC_SECRET_KEY="my_random_secret_key"

If you start the web server after this, the ``ORC_SECRET_KEY`` will be set to 
the value you have defined.

.. warning::

    If you first install ORC-OS entirely, then change the ``ORC_HOME`` 
    environment variable and then start the web server, you may loose access
    to your database and videos. This is because the web server will look for 
    the database and videos in the location specified by the ``ORC_HOME``.
    Make sure you move the relevant files and folders under the new location 
    specified by ``ORC_HOME``. If you have not done any processing yet, you
    may also simply start with a fresh empty database. Instructions are 
    provided in the section about the 
    :ref:`command-line interface <devel_cli>`.


Virtual environment
-------------------
Raspberry Pi OS comes with a pre-installed version of Python, and normally you
would then install the ORC-OS software in a virtual environment to avoid 
conflicts with the pre-installed Python and other software. See also our 
installation instructions for more details.

We here assume that you have made a virtual environment for ORC-OS under 
the path `$HOME/venv/orcos`. To activate this virtual environment, you can run 
the following command (adapt your exact path if necessary):

.. code-block:: bash

    source $HOME/venv/orcos/bin/activate

You should see the name of your virtual environment in parentheses at the 
beginning of your terminal prompt, indicating that it is active. For example:

.. code-block:: bash

    (orcos) pi@openrivercam:~ $

Now we are able to access python commands and scripts, that use pre-installed
packages in the virtual environment. In the next sections we will treat:

* starting and stopping the web server and starting it up in developers mode 
* using the command line interface

For both of these, you will need to have the virtual environment activated as 
described above.

.. _installation instructions: https://github.com/localdevices/ORC-OS/blob/main/README.md
.. _Raspberry Pi documentation: https://www.raspberrypi.com/documentation/computers/remote-access.html
.. _Python virtual environments documentation: https://docs.python.org/3/library/venv.html
.. _RealVNC client: https://www.realvnc.com/en/l/download/

