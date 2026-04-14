.. _parts_general:

General required parts
----------------------


.. note::

  Before assembling any full station, you may want to start just setting up the 
  software on a device in your office. This is a great way to get familiar with
  the software and to test it with some sample videos before considering any 
  full field setup. Just get a suitable computer (e.g. a Raspberry Pi 5) and 
  install ORC-OS on it, following our instructions.

We list here what is needed to get ORC-OS installed and start experimenting. We 
do not yet provide a specific parts list, nor do we demonstrate how to put these
together. This section is just to explain which part is needed and why so that you
understand the hardware concepts.

- A small computer, such as a single board computer, running x64 or ARM64. 
  ORC-OS is optimized for Raspberry Pi 4 or 5 (recommended) device with 8GB of 
  memory. We *DO NOT* support lower Raspberry Pi devices as these are not 
  powerful enough and do not work with arm64 images. See: 
  https://www.raspberrypi.com/products/raspberry-pi-5/?variant=raspberry-pi-5-8gb
  This single board computer will run the ORC-OS dashboard and will perform all
  video processing and data management. It may also be responsible for 
  controlling power and interrupt power supply to the camera in case you need
  low energy consumption.

- A suitable power supply. Here it depends on your situation what you need. 
  In general, a Raspberry Pi 5, and most carrier board under a Raspberry Pi 5
  Compute Module, require 5 Volts! So whatever you do, always ensure that the
  power supply connected to your Raspberry Pi delivers 5V. In general you also
  must ensure that the entire route from battery to the Raspberry Pi can deliver
  5A of current, to ensure a stable and reliable power supply. This is not 
  trivial as discussed below.

  1. If your site is equipped with normal wall sockets with 220 (or 115) Volt,
     get a standard Raspberry Pi 5, 5V 5A power supply. Done!
  2. If you do not have a wall socket but need a 12V or 24V battery (e.g. combined with solar panels), you will require
     a buck step down converter (check your favorite electronics store or web store). 
     This device is capable to transform an input voltage and current into 
     another voltage and current on the output. There are many different sorts.
     As a 12V battery is a so-called DC power source, you need a buck converter 
     that can take DC (NOT AC) input. It also should be able to take the voltage
     of your battery (e.g. 12V or 24V) and step it down to 5V. Finally, it 
     should be able to **deliver 5V 5A for a stable and reliable power supply**.
     Many smaller converters only provide 3A! This is not sufficient for Raspberry Pi 5, especially when you connect peripherals 
     such as a 4G modem. In the 12V case, you will also need a suitable cable that goes from the buck step down converter to the 
     Raspberry Pi. One end should be USB-C and the other ideally +/-, this is also called a USB-C "open end" cable. 
     Similar to the buck converter, here it is critical that you use a cable that 
     can transport a sufficiently high current (again 5A) to ensure a stable and reliable power supply. Check the 
     specifications of the cable carefully. Typically you need a **20AWG** or lower (thicker) cable for 5A. Also, get a
     short cable (e.g. 0.5 meter) to minimize power loss. Longer cables can cause voltage drops, which can lead to 
     instability. Also long cables are more difficult to manage inside a small enclosure.

  .. note::

    The **AWG** (American Wire Gauge) is a standard for wire thickness. The lower 
    the AWG number, the thicker the wire and the more current it can safely 
    carry. For example, a 18 AWG wire can carry up to 10A of current, while a 
    20 AWG wire can typically carry up to 5A of current and a 22 AWG wire can
    only carry up to 3A. Using a wire that is too thin for your current needs
    can in the most severe situations lead to overheating and potential fire 
    hazards, so it's important to choose the right gauge for your application.
    In most cases, a too low current carrying capacity will lead to voltage 
    drops and instability of your power supply towards the Raspberry Pi.

- Enough storage. For Raspberry Pi, an SD card (micro) of good quality (really...try to not underspend on cheap SD
  cards) of at least 32GB in size; OR
  (better) get a Raspberry Pi 5 Compute Module with a carrier board, with at least 32GB eMMC flash storage. For SD-cards,
  ensure you have a microSD card reader slot on your normal working PC or laptop,
  or ensure you get a SD card adapter to fit it in a large SD card reader.
  You need your workstation to setup the OS.
  See: https://www.raspberrypi.com/products/compute-module-5/?variant=cm5-104032

- An IP camera, that can handle events and record at a high enough bit rate. Recommended is 20 Mbps at 1080p.
  We recommend a camera that receives network and power through a single cable,
  using a PoE switch (see below). The camera should also be capable to record "events" so that you can program the camera to deliver a video on time
  intervals or at boot. This is important as ORC-OS needs videos of short lengths at certain intervals. The events should
  be allowed to write files to an FTP or SFTP location, so that the videos can be posted directly on the Raspberry Pi.
  A directly connected camera such as a Raspberry Pi (v3) camera is also possible.
  Our ready-to-flash OS image has Raspberry Pi camera libraries pre-installed. Alternatively you may use a suitable
  IP Camera that can deliver video files via FTP or SFTP.
  See: https://www.raspberrypi.com/products/camera-module-3/

- A PoE switch (only if you use an IP camera). Normally, IP cameras are provided with network and power through one 
  single LAN network cable. A PoE switch combines a power source and network source into one network cable
  which then carries both network signal and power. This is very convenient as it reduces the number of cables
  outside of your equipment enclosure and simplifies installation. If you use a 
  PoE switch, ensure that it can provide enough power for your camera (e.g. 20W or more).
  Check the camera documentation for the exact power requirements. 
- When using an IP camera, you will also need a shared network switch, or modem, allowing IP camera and compute device
  to share the same network.

- A small cell battery to run the Real-Time Clock (RTC) on the Raspberry Pi. The Rpi-5
  has a built-in RTC, which allows it to keep track of time even when powered 
  off. We use this in ORC-OS to schedule power on and off intervals. In practice
  this saves a huge amount of energy, as the Raspberry Pi consumes almost no
  energy when switched off.

- For connectivity in the field, a 4G modem is recommended. This can be a separate modem, or a modem HAT for the 
  Raspberry Pi. Ensure that the modem is compatible with your local network and that you have a suitable SIM card with 
  data plan to run it.

- For powering in the field with solar panels, you will need a solar charge controller, a solar panel of sufficient 
  wattage (e.g. 50W or more) and a 12V battery (e.g. 96Wh or more). The exact specifications depend on measurement
  frequency, and the expected sunlight in your location. For security, you will also need a proper fuse directly behind 
  the "+" terminal of the battery. Assuming a maximum 1A power draw from the camera and 2A (at 12V) from the Raspberry 
  Pi, a 5A fuse should be sufficient.

.. note:: 
  
  The cool thing of ORC-OS is that you can setup power management and control of power of the camera through extra 
  additional services, that can be created, deployed and managed entirely on the front end interface. Are you using
  a bespoke power management solution? No problem, build your own script to control that and create a service in our
  web interface for it, which controls the parameters of your script. For more information, please check out 
  :ref:`our guide on creating services <devel_services>`.

.. tip::

  An even cooler thing: if you get Rainbow Sensing's very cheap ready-to-flash ORC-OS image with support package, you 
  will receive 
  a ready to use relay service menu, a power management service menu and a remote connectivity menu in the web front 
  end, making programming of relays and power management (regular interval on/off) and remote connectivity very easy 
  to setup. Each service has its own README section with instructions how to use it, and even how to connect a relay 
  extension. The support includes a username and password for remote connectivity, getting you up and running 
  instantly.
