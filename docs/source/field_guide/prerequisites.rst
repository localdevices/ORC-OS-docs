.. _prerequisites:

Hardware for using ORC-OS
-------------------------

We list here what is needed to get ORC-OS installed on a typical field device in your office.

- A small computer, such as a single board computer, running x64 or ARM64. ORC-OS is optimized for Raspberry Pi 4 or 5
  (recommended) device with 8GB of memory. We *DO NOT* support lower Raspberry Pi devices as these are not powerful
  enough and do not work with arm64 images. Please do not contact us for support on Raspberry Pi 3 or lower devices.
  See: https://www.raspberrypi.com/products/raspberry-pi-5/?variant=raspberry-pi-5-8gb

- A suitable power supply. For Raspberry Pi 5, we recommend a
  5V 5A power supply. For connections in the field to a 12V battery (e.g. combined with solar panels), you will require
  a buck step down converter (check your favorite electronics store or web store). Ensure that you find one with 12V
  input (up to 24V if your battery has a higher voltage) that **delivers 5V 5A for a stable and reliable power supply**.

- A suitable cable that goes from the buck step down converter to the Raspberry Pi. One end should be USB-C and the 
  other ideally +/-, this is also called a USB-C "open end" cable. Here it is critical that you use a cable that 
  can transport a sufficiently high current (again 5A) to ensure a stable and reliable power supply. Check the 
  specifications of the cable carefully. Typically you need a **20AWG** or lower (thicker) cable for 5A. Also, get a
  short cable (e.g. 0.5 meter) to minimize power loss. Longer cables can cause voltage drops, which can lead to 
  instability.

- Enough storage. For Raspberry Pi, an SD card (micro) of good quality (really...try to not underspend on cheap SD
  cards) of at least 32GB in size; OR
  (better) a Raspberry Pi 5 Compute Module with a carrier board, with at least 32GB eMMC flash storage. For SD-cards,
  ensure you have a microSD card reader slot on your device, or ensure you get a SD card adapter to fit it in a large
  SD card reader.
  See: https://www.raspberrypi.com/products/compute-module-5/?variant=cm5-104032

- An IP camera, that can handle events and record at a high enough bit rate. Recommended is 20 Mbps at 1080p.
  The camera should also be capable to record "events" so that you can program the camera to deliver a video on time
  intervals or at boot. This is critical as ORC-OS needs videos of short lengths at certain intervals. The events should
  be allowed to write files to an FTP or SFTP location, so that the videos can be posted directly on the Raspberry Pi.
  A directly connected camera such as a Raspberry Pi (v3) camera is also possible.
  The Raspberry Pi OS will have Raspberry Pi camera libraries pre-installed. Alternatively you may use a suitable
  IP Camera that can deliver video files via FTP or SFTP.
  See: https://www.raspberrypi.com/products/camera-module-3/

- A PoE switch (only if you use an IP camera). Normally, IP cameras are provided with network and power through one 
  single LAN network cable. A PoE switch combines a power source and network source into one cable. 

- When using an IP camera, you will also need a shared network switch, or modem, allowing IP camera and compute device
  to share the same network.

- For connectivity in the field, a 4G modem is recommended. This can be a separate modem, or a modem HAT for the 
  Raspberry Pi. Ensure that the modem is compatible with your local network and that you have a suitable SIM card with 
  data plan.

- For powering in the field with solar panels, you will need a solar charge controller, a solar panel of sufficient 
  wattage (e.g. 50W or more) and a 12V battery (e.g. 96Wh or more). The exact specifications depend on measurement
  frequency, and the expected sunlight in your location. For security, you will also need a proper fuse directly behind 
  the "+" terminal of the battery. Assuming a maximum 1A power draw from the camera and 2A (at 12V) from the Raspberry 
  Pi, a 4A fuse should be sufficient.

A few extra settings may have to be made on the Raspberry Pi 5 when using this setup.

- To enable low power use when switching off the Pi, follow the instructions on
  `this link <https://www.jeffgeerling.com/blog/2023/reducing-raspberry-pi-5s-power-consumption-140x/>`_
- For power cycling, you have to set up a separate service that starts the Pi at set intervals
  and shuts down the pi after a few minutes.
  This is only possible on a Raspberry Pi 5, NOT on 4. On Raspberry Pi 4 you will need a separate
  power management solution.
- You may have to override the Rasperry Pi 5's 5V/5A USB-C handshake. This is a security measure that ensures you are
  using a Raspberry approved power supply. If you are using a buck converter, this will not be the case. You can 
  override this by adding ``usb_max_current_enable=1`` to the ``/boot/firmware/config.txt`` file. This allows the
  Raspberry Pi to draw the full 5A from the power supply, which is necessary for stable operation and especially 
  required when several peripherals are connected and powered from the Pi such as a 4G modem.

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

A typical hardware setup in the field
-------------------------------------

Once the software is installed, you will need a proper setup in the field. We try to provide
some guidance here how to establish a complete field setup here.

.. figure:: ../_images/_general/hardware_setup_example.png

   Impression of a typical hardware setup and the required connections
   :scale: 50 %
   :alt: hardware setup


To help you build your own camera setup we here give an overview of possible parts that we have ourselves tested with.
The figure above gives an impression what the entire build would look like.

We use industrial grade parts and assume a setup with solar power and running every 30 minutes.
We are not frequently and actively maintaining the parts list. Please let us know if anything seems out of order by
creating a Github issue on the `ORC-OS-docs GitHub repository <https://github.com/localdevices/ORC-OS-docs>`_.

.. warning::

   We do NOT give any guarantee that with these parts, your build will work. We also do not give
   any support without a project. It may be that certain parts change in time. We are never responsible for
   any issue related to your own built nor for any incompatibilities with the ORC-OS software.

.. list-table::
    :header-rows: 1
    :widths: 35 65

    * - Part
      - Example specific item
    * - Raspberry Pi 5 CM (8/32GB)
      - `Raspberry Pi 5 <https://www.raspberrypi.com/products/raspberry-pi-5/>`_
    * - Compute Module board (8/32GB)
      - `Waveshare CM5-IO-Base-B <https://www.waveshare.com/cm5-io-base-b.htm?sku=30703>`_
    * - Active cooler for Raspberry Pi 5
      - `Waveshare active cooler for CM5 <https://www.waveshare.com/cm5-fan-3007-5v.htm?srsltid=AfmBOopLk_ws8IzYfTvdiKfIjJIpYJ7of6YJRmunQx7_f5n9zkALIaFL>`_
    * - Rechargeable battery for Real-Time clock and power management. For larger
        carrier boards, a CM/ML2032 is needed. For smaller boards, (e.g. the
        Waveshare CM5 IO Base-B) typically a CR/ML1220 is needed.
        The normal Raspberry Pi 5 model with SD card has a special prepared battery.
      - Please check availability locally. 3.7V LIR rechargeable batteries typically work.
    * - Weather proof IP camera (ideally >= 20Mbps, 1080p, event-capable)
      - `AXIS P1135-E Mk II <https://www.axis.com/products/axis-m1135-e-mk-ii>`_
    * - 4G modem (can also be a Raspberry Pi modem HAT like a Waveshare7600E-H)
      - `Waveshare7600E-H 4G HAT <https://www.waveshare.com/wiki/SIM7600E-H_4G_HAT?srsltid=AfmBOorAbFR9oT1jp57zfExviR1y5g-p3vRk5pf_f-1jtHWzr35EAALa>`_
    * - Relay module (ideally a Pi HAT, but if you need more peripherals, relay boards of 8 relays with Raspberry Pi 
        header are available also)
      - `RPi Relay Board <https://www.waveshare.com/wiki/RPi_Relay_Board>`_
    * - PoE adapter (12V; verify power specs). The one indicated below is very nice, as it can directly be connected 
        to the solar charge load output (12V) with a simple +/- wire, and provides all the switch options
        you will need. Just be careful NOT to use the "passive PoE LAN port" (only one) on a device that is not designed 
        for it, as this can damage your device.
      - `LINOVISION PoE switch for DC powered systems <https://eu.linovision.com/en-eu/collections/all-poe-switches/products/4-ports-mini-solar-poe-switch-optimized-for-big-ptz-camera-and-wireless-bridges?_pos=2&_fid=d8b5ba801&_ss=c>`_
    * - 12V to 5V (USB) buck converter, 5A for Raspberry Pi 5. The device indicated here is very easy to use as you 
        do not need to tweak the voltage or current. Just connect the 12V input and you get a stable 5V 5A output. We 
        recommend to put a spare one inside the housing in case it fails.
      - Sold on amazon.com e.g. `DEVMO 12V to 5V 5A Step-Down <https://www.amazon.com/DEVMO-Converter-Step-Down-Regulator-Transformer/dp/B09C4HPNJ8/ref=sr_1_11?dib=eyJ2IjoiMSJ9.RZsxLbFRLcU8Wb5O2N-5KjMcJ6uj1CoIoVbBQr4STi2nn6d88k_vvBEjd3TDfF1TUFG0_04Tchp9esoT8_nmfegVbZhdkErK-zT_2o9ZQX2eBJNbN-X9-kjJVchUWCA9eBo5tQZFStZovLdhs98BJyhv93V8ZhQyyslG4ILrTzFhK3OBGKHWr7ZUgFr1rJ9RxPkQkle4oxa4mNnuEAJevyGPTYtAqVepEHDPPPv1w8EHE_aqNBE0M0UVf_kjmDnycLmHf4u1SRdzXKlINuMrt2qboR1R5bS0C6TAlCN3q9o.zKXYl-61B5JUPgaXJbKZUSRhCvGflPU_vFfEAFQ1HIA&dib_tag=se&qid=1768307208&refinements=p_89%3ADEVMO&s=electronics&sr=1-11>`_
    * - CAT6 outdoor network cable of sufficient length to go from the PoE adapter to the camera
      - Any computer hardware shop.
    * - USB-C "open end" cable that can handle 5A current. This is for connecting the buck converter to the Raspberry 
        Pi.
      - E.g. `this link <https://www.amazon.com/11inch-Pigtail-Equipment-Installed-Replacement/dp/B0DLKPWF1G/ref=sr_1_3?crid=1I2ANFUJZR61V&dib=eyJ2IjoiMSJ9.a4Ft-il2Dw8I7G-8lhyY7R-qoSNnJknf-mRPHak9BNrjZlcDMcM3oFtowb88AnhET1Sk4KceVfl1CFUFcHY4tAap2TuQDV7k9iDgYGSEO4VNES4wLqB-mPPJO-iHHAGEplTqud5WWDplv5CiQD849ItUpD-Tp33KlKYP-3Tb1NlgnrbaDJgnL7bhd6tNIDBxDtQC7c7hW3bJEQonujhv78WHmYafl_kShSBQHi0SGMM.rrJXGCxylumBzGiEWZ2Jw5cnIt3PMwM-9ez7y7sH1SA&dib_tag=se&keywords=USB-C%2Bbare%2Bwire%2B20%2BAVG%2B5A&qid=1775045092&sprefix=usb-c%2Bbare%2Bwire%2B20%2Bavg%2B5a%2Caps%2C178&sr=8-3&th=1>`_
    * - A very short (e.g. 0.5 meter) CAT6 network cable. This is for connecting the Raspberry Pi to the switch.
      - Any computer hardware shop.
    * - Solar panel (>= 50W)
      - Any electronics/solar shop.
    * - MQTT Solar charge controller
      - Any electronics/solar shop.
    * - 12V battery (>= 96Wh)
      - Any electronics/solar shop. Consider a compact LiFePO battery for better environmental performance.
    * - +/- terminal connectors compatible with the 12V battery.
      - Any electronics shop.
    * - A fuse (e.g. 4A) for safety, to be placed directly behind the "+" terminal of the battery. We used a fuse holder
        with a blade fuse, as it makes things so simple to replace but there are many options for this. Also here,
        recommended to put a few spare fuses inside the housing in case of failure.
      - Any electronics shop.  
    * - a IP66 enclosure. Look for one that has optional cable outlets so that you can bring +/- of solar panel into
        the device and a network cable out. At least two cables will need to pass through.
        Ideally get one or two DIN rail pieces in the box for proper and neat device and cable management.
      - Sold on amazon.com, but look carefully for one, large enough, and with the proper cable options.
    * - watertight cable enclosures
      - Sold on amazon.com e.g. `3.5-10mm waterproof IP68 electrical cable connectors <https://www.amazon.com/Junction-Waterproof-Electrical-Connector-3-5-10mm/dp/B083HRLQG3/ref=sr_1_8?crid=HEXI3WRNBK05&dib=eyJ2IjoiMSJ9.1OgXdhDDhFyRtnLGA9HrHG7yCSQf3A_MBkggyG9Ps9lv6DH14X6Rou6pRoXwdBd1S_5NyPLheFDoA9PCpXOyiUILaiG--e_MmnNDt_nRV508q1TGmHOfWa69i_woKkwZbBnw8zu5mEHXyfcVZDekmMhnBlnwYLVj2GDWc1F9--lTXAsviXI18nyE8OYQO4nzxGLvk1Rr7_nx5Ba2JUU1zJ0e-74Z0N8y_0vqtyURkI6J3jQq8LzkBMO5wZjLV_61di_vjqmocnXhGFOHzkUkbA2nUlQS2Bm8-Yt_owMLAcs.paFNW_AIQxvCP420cI06YyJN6FrAUH3UcIP2MYbzs54&dib_tag=se&keywords=cable%2Bconnectors%2Boutdoor&qid=1768311613&sprefix=cable%2Bconnectors%2Boutdoo%2Caps%2C190&sr=8-8&th=1>`_
    * - passthrough cable connectors for watertight connection where cables enter/exit the enclosure.
      - Sold on amazon.com e.g. `QILIPSU NPT Cable Gland Waterproof IP68 <https://www.amazon.com/QILIPSU-Waterproof-Adjustable-Locknut-Diameter/dp/B07ZRH3V59/ref=sr_1_9?crid=HEXI3WRNBK05&dib=eyJ2IjoiMSJ9.1OgXdhDDhFyRtnLGA9HrHG7yCSQf3A_MBkggyG9Ps9lv6DH14X6Rou6pRoXwdBd1S_5NyPLheFDoA9PCpXOyiUILaiG--e_MmnNDt_nRV508q1TGmHOfWa69i_woKkwZbBnw8zu5mEHXyfcVZDekmMhnBlnwYLVj2GDWc1F9--lTXAsviXI18nyE8OYQO4nzxGLvk1Rr7_nx5Ba2JUU1zJ0e-74Z0N8y_0vqtyURkI6J3jQq8LzkBMO5wZjLV_61di_vjqmocnXhGFOHzkUkbA2nUlQS2Bm8-Yt_owMLAcs.paFNW_AIQxvCP420cI06YyJN6FrAUH3UcIP2MYbzs54&dib_tag=se&keywords=cable%2Bconnectors%2Boutdoor&qid=1768311613&sprefix=cable%2Bconnectors%2Boutdoo%2Caps%2C190&sr=8-9&th=1>`_

You will need basic tools such as:

* a wire stripper
* a small cutter
* small screw drivers (phillips and flat head, for terminals and relay connections)
* crimping pliers
* 12V electric wire (wire used for speakers usually is great for 12V projects, but never use this for 220V applications!).
* a multimeter to check voltages and connections
* terminal and cable connectors for the 12V battery and charge controller connections
* isolation tape for safety to cover exposed wires and connections

Assemblage
----------

Below a rough guide to assemblage is provided:

Getting the Raspberry Pi and relay module running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Assuming you have a Pi 5 Compute Module with a carrier board, put the Raspberry Pi 5 CM on the carrier board, and 
   install the active cooler.
2. Install ORC-OS as indicated on the `README <https://github.com/localdevices/ORC-OS/blob/main/README.md>`_ of ORC-OS.
   We recommend getting our ready-to-flash images as this will give you a huge head start with everything pre-installed 
   including services for power management, relay management and remote connectivity.
3. Fix the modem HAT on the Pi and insert a SIM-card. Make sure the SIM card does not have a PIN-code. This will save
   you a lot of trouble. Test the connection whilst in your office. Use stacking header to get enough space between 
   the 
4. Fix the Relay HAT on top of the modem HAT (or vice versa, whatever is easiest for you). 
5. Switch on the Pi with a normal 5V/5A power supply and connect a laptop or computer via a LAN cable.
6. Log into the web interface of ORC-OS by going to http://orcos.local
7. Program one of the relays on the HAT to switch on for 30 seconds during boot. This can be done by creating an 
   additional :ref:`service <devel_services>`. We provide relay switching as a full exmaple in the manual. 
   With Rainbow Sensing's ready-to-flash image, you will receive a ready 
   to use relay service menu in the web front end. This makes programming the relay very easy. Just select the relay pin
   (first relay is on 26), select a frequency of e.g. 300 seconds, and a duration of 30 seconds. Test it by clicking
   on "Start".

Cool! You have a relay working on your Raspberry Pi 5. This relay can be used to switch on the PoE adapter for the 
camera, but for now we will keep it off and directly connect the camera to the PoE adapter for testing. The modem
is also already installed, let's not worry about that now.

Hooking up the power supply
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning::

    When working with electricity, always be careful and take the necessary safety measures. If you are not sure about
    anything, please consult an expert or do more research before proceeding. In general, 12V is not necessarily very 
    dangerous but you should never short cut the + and - terminal of the battery as this may cause sparks, very high
    current in your wires, and even fire. Always use a fuse (attached as close as possible to the "+" terminal)
    for safety, and ensure you have the proper tools and equipment to work with electricity safely. A multimeter is
    highly recommended to check voltages everywhere in the system before connecting anything.

1. Prepare some wires to connect the battery to the charge controller. Typically you need a terminal connector, some 
   cable connectors, a crimp tool, a wire stripper, isolation tape and some 12V capable double wire, preferrably colour 
   coded (red for + and black for -) of about 0.75 to 1 mm2. Do not mix up the colors. If you confuse them and connect 
   "+" to "-" you may damage equipment. Wire as follows: Take the fuse holder, cut it about half way, strip it on both 
   ends, connect a terminal connector on one end and a cable connector on the other end. Take a piece of electric wire,
   split it over a small part so that you can connect the fuse holder on the red part, and another terminal connector
   on the black ("-") part. Strip the other ends and connect the "-" to the charge controller's "-" of the battery
   terminal, and the "+" to the "+" terminal of the charge controller. Now also connect the terminal connectors
   to the battery, again ensuring the correct polarity. The fuse should be directly behind the "+" terminal of the 
   battery. The black part of the wire should go on the "-". Now the battery and charge controller are securely 
   connected. Assuming the battery has some power, check the voltage on the charge controller with a multimeter.

   <PHOTO of wiring with fuse and connectors inside box>

2. If you want and there is enough sun, you can now also connect the solar panel to the charge controller. This is done
   in a similar way as the battery, but now you the wires to the "solar panel" terminal of the charge controller. 
   Again, ensure correct polarity and check with a multimeter if you get power on the charge controller when connecting 
   the solar panel. Of course you only get a voltage if the panel is in the sun. A typical panel rated for 12V in the 
   sun can easily deliver 13 or 14 volts or much lower when in the shade. This is normal, as the voltage depends on the 
   amount of sunlight and the 
   charge controller regulates the voltage to the battery. If you do not have a solar panel or it is not sunny, you 
   can also connect a 12V power supply to the charge controller. Just strip the end on the power supploy side, plug it 
   into the wall and connect the wires to the "solar panel" terminal of the charge controller. Again, ensure correct
   polarity and check with a multimeter if you get power on the charge controller.

.. container:: figure-text-pair

   .. container:: column

      .. figure:: ../_images/_hardware/solar_voltage_shade.jpg
         :width: 100%

         Voltage reading when solar panel is kept in the shade.

   .. container:: column

      .. figure:: ../_images/_hardware/solar_voltage.jpg
         :width: 100%

         Voltage reading when solar panel is in direct sunlight.

3. Charge your 12V battery to a satisfactory amount for testing. You can do this safely by connecting the battery to 
   the charge controller and connecting the charge controller to the solar panel, or by using a separate 12V charger. 
   Connect the battery to the charge controller and test with a multimeter if you can get power from the load terminal 
   (12V) of the charge controller. This is where you will connect the PoE adapter and 12V --> 5V buck converter later 
   on.

.. warning:: 
   
   Before connecting anything to the load terminal, make sure you switch off the load with the power button on the 
   charge controller. This button is usually indicated with a "lightning" or a "lightbulb" symbol. If you do not switch
   off the load, you may easily cause a short circuit when connecting as wires may still be exposed.

4. Now it is time to connect your Raspberry Pi setup. Raspberry Pi cannot work with 12V. In fact the Pi will blow up if
   you would supply that. First connect the buck converter to the charge controller load terminal (12V) with a simple 
   piece of +/- (red/black) wire. Again, ensure correct polarity! The buck converter will convert the 12V to a stable 
   5V 5A output that is suitable for the Raspberry Pi. Once connected, there should be a red light on the buck 
   converter indicating it is powered. Check the voltage on the other side first and see if it is about 5V. If the wires
   are a little openly exposed, then use isolation tape to cover the exposed parts to prevent short circuits. Do this
   on both sides. 

.. container:: figure-text-pair

   .. container:: column

      .. figure:: ../_images/_hardware/buck_converter_voltage_in.jpg
         :width: 100%

         Voltage reading on the input of the buck converter, which should be about 12V. It can be higher when the 
         battery is fully charged.

   .. container:: column

      .. figure:: ../_images/_hardware/buck_converter_voltage_out.jpg
         :width: 100%

         Voltage reading on the output of the buck converter, which should be about 5V. It can be a little bit higher,
         but not substantially as this may damage the Raspberry Pi. If you have a variable buck converter, you can 
         adjust the output voltage with the potentiometer on the converter. Always really make sure the voltage is 
         correct before connecting the Raspberry Pi.

5. Now connect the output of the buck converter to the Raspberry Pi via the USB-C open end cable. Test if you can power
   on the Raspberry Pi with this setup. The green light should go on and your programmed relay should switch on with
   a click sound.

Connecting peripherals
^^^^^^^^^^^^^^^^^^^^^^

The relay is working fine, but it is not really powering anything yet. Let's connect the PoE adapter to the relay, 
so that it can switch on and off the camera. The PoE adapter requires 12V so we can quite easily connect it to the 
charge controller load terminal (12V) with a simple piece of +/- (red/black) wire. Again, ensure correct polarity! 
The relay will be in between the PoE adapter and the charge controller, so that it can switch on/off the power to the 
PoE adapter. Probably you have to take out the buck converter from the charge controller, then bundle the two wires
and connect them together to the charge controller load terminal, and then connect the buck converter and the PoE.


.. warning:: Before disconnecting, make sure you switch off the load with the power button on the charge controller.
  
1. Connect the PoE adapter to the load terminal of the charge controller. For now we do not use the relay, as we want
   to first test if the PoE adapter works and can power the camera. Again think about the polarity. The PoE adapter
   uses 12V as input, so no buck converter is needed for the PoE adapter in our case.

.. warning:: 

   You may have acquired a different PoE adapter than the one we indicated in the parts list. Make sure that you get
   one that can handle 12V or ensure that the voltage is converted with a buck step-up or step-down converter to the
   right voltage first. If the PoE adapter has a 220 to 12V adapter you can cut off the and strip the +/- wires on the
   12V side and connect these to the charge controller load terminal. Always check the PoE manual and check carefully 
   the required voltages before connecting any equipment.

2. Connect the IP camera to the PoE adapter with the long CAT6 network cable. If you have a separate 
   switch, you can also connect the camera to the PoE adapter, and the PoE adapter to the switch (not the other way
   around).

3. Also connect the Raspberry Pi with a LAN cable to the PoE Switch, so that it shares the same network as the IP 
   camera. Connect your own computer to the switch as well (NOT on a passive PoE port!!). Test if you can access the
   Raspberry Pi through the network for instance by logging into the ORC-OS interface. That usually is possible on 
   ``http://orcos`` or ``http://orcos.local`` or replace ``orcos`` for the hostname you created while installing.

4. Also test if the camera's web interface is accessible. The camera usually has a web interface that you can connect to
   via a hostname or IP address. Check the manual of your camera to find out how to access it. If you can access the 
   web interface, you can also test if you can see the live stream from the camera. If this works, then the camera is
   properly powered and connected to the network.

5. Once verified, you can wire in the relays! Again, switch off the load on the charge controller first! Then remove 
   the + wire from the PoE adapter, and connect it to the normally open (NO) terminal of the relay. This is because
   without any signal, you want this relay to be open so that it does not supply power. Then connect a new red wire from
   the common (COM) terminal (middle of the relay) to the PoE adapter. Check below to see what the wiring should look
   like.

.. figure:: ../_images/_hardware/relay_poe_wiring.jpg
   :alt: relay wiring

   Wiring of the relay in between the charge controller and the PoE adapter. The relay is used to switch on/off the
   power to the PoE adapter, which in turn powers the camera. The relay is controlled by the Raspberry Pi, which can
   be programmed to switch on/off the relay at certain intervals or at boot.

Setting up the camera and ORC-OS for receiving videos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Go to the Settings - Daemon settings. Fill out the expected file name convention for receiving videos from your
   IP-camera (check the manual of the IP camera, you expect something like ``video_20260103_141500.mp4`` for a video
   taken on 3 January 2026, 2:15 PM. This would yield a naming convention ``video_{%Y%m%d_%H%M%S}.mp4``. Click on 
   "Submit".
2. Now click on <EXAMPLES> to see how to get such video files transferred from the IP camera to the raspberry pi.
   You want to note the SFTP details and the specific folder the files should go to.
3. Now login to the IP camera web interface (check the IP camera's manual, this is different for all camera models).
4. Program an "event" that records a 5-sec video when the camera switches on. Use SFTP to transfer the video file
   directly to the Raspberry Pi using the details taken from ORC-OS. If a single event at boot is not possible, you
   can also program the camera to record 5-seconds at set intervals, such as every 30 minutes. In practice it will
   then only record at boot, as your cycle is shorter than 30 minutes. Ensure the bit rate is high! Ideally 20Mbps
   (Megabit per second). This is to ensure that the details visible on the water surface are not lost through 
   compression.
5. Test the event and check if the files indeed end up in the right folder. Currently these are not yet processed.

Install for field use
^^^^^^^^^^^^^^^^^^^^^

1. Install all components in the IP66 enclosure. Prepare the wiring of the solar panels with a long enough wire. 
   controller, then the panel). Pass the cables and fix these watertight with passthrough cable connectors.
2. If possible, keep the battery inside the housing with short wires, and keep it a little away from the electronics. 
   Clamp it with wall irons or something else that keeps it from the bottom of the casing. The battery may become warm 
   during operations.
3. Install the device, with the camera aimed at the wqater surface. Carefully read our 
   :ref:`Survey guide <field_survey>` to properly position and aim the device. 
4. During setup, pass the long network cable through the enclosure with passthrough cable connectors, and reconnect 
   everything afterwards. Try to keep as much of the wiring inside of the box, wind it up neatly and fix it with cable 
   ties. If cable is outside, always tie it up neatly at a high position. Under no circumstance should you leave it on 
   the ground as it is then more exposed to water, wildlife, trampling and other risks.
5. Start configuring ORC-OS! See our extensive :ref:`User guide <user-guide>`. Don't forget to set up remote management
   if you want to be able to access the device remotely. Also setup the connection with your own 
   :ref:`LiveORC server <liveorc>` to 
   synchronize and centralize all your processed data and videos. If you have a support contract with Rainbow Sensing, 
   you will receive remote connectivity for your devices within the support package.
6. Once configured, enable all required services in the service options, such as power management and relay management.
   Choose parameters such as durations and boot cycles according to your needs.
7. Wait for a few cycles to see if everything works as expected.
8. Go home and let the device collect your data! Just make sure you have a sufficiently large data package on your SIM 
   card.

.. note::

   If you decide to get a service contract for support from Rainbow Sensing, you will receive remote connectivity for
   your devices within the support package if your device is compatible. Remote support works through a pangolin server
   and accounts and offers you a https access to services via a proxy server, with highly granular access. This is very
   similar to services such as remoteit and cloudflare, but own-hosted. Contact us at info@rainbowsensing.com for
   further information.
