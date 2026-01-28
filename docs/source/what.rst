.. _what:

.. container:: figure-text-pair

   .. container:: column

        .. figure:: _images/_general/ngwerere_20260103.jpg

           Example output in Lusaka along Ngwerere river. About 6 m/s surface velocities were measured on 3 January 2026
           2:15 PM local time.

   .. container:: column

      A relatively simple camera system can be utilized to measure accurately in **m3/s** how much water flows
      through a stream. Look at this example, where a staggering 5 meter per second (!) velocity was observed in a storm
      drain in Lusaka. There is **no other method** in the world that can measure such extreme flows.

      OpenRiverCam OS (ORC-OS) is an entirely open-source dashboard to organize automated measurements of water levels and river flows
      using camera videos. It is currently only supporting usage on single measurement sites, and is meant to be deployed on
      a device that can run ORC-OS. It should be a linux-based device. It is optimized for use on Raspberry Pi 5 devices and
      can utilize connected Raspberry Pi cameras natively!

.. note::

   In the near future we will also allow connecting the dashboard to `LiveOpenRiverCam`_,
   the open-source server-side API. This will allow for browsing and interacting with all data from measurement sites
   that report live to this server. If you store the original videos on LiveORC, you will also be able to process or
   reprocess videos on the server-side.

.. _LiveOpenRiverCam: https://github.com/localdevices/LiveORC