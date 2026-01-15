.. _whom:

What and for whom is ORC-OS?
----------------------------

.. container:: figure-text-pair

   .. container:: column

        .. figure:: ../../_images/_general/ngwerere_20260103.jpg

           Example output in Lusaka along Ngwerere river. About 6 m/s surface velocities were measured on 3 January 2026
           2:15 PM local time.

   .. container:: column

      A relatively simple camera system can be utilized to measure accurately in m3/s how much water flows
      through a stream. Look at this example, where a staggering 5 meter per second velocity was observed in a storm
      drain in Lusaka. There is no other method in the world that can measure such extreme flows.

      OpenRiverCam OS (ORC-OS) is an entirely open-source dashboard to organize automated measurements of water levels and river flows
      using camera videos. It is currently only supporting usage on single measurement sites, and is meant to be deployed on
      a device that can run ORC-OS. It should be a linux-based device. It is optimized for use on Raspberry Pi 5 devices and
      can utilize connected Raspberry Pi cameras natively!

.. note::

   In the near future we will also allow connecting the dashboard to [LiveORC](https://github.com/localdevices/LiveORC),
   the open-source server-side API. This will allow for browsing and interacting with all data from measurement sites
   that report live to this server. If you store the original videos on LiveORC, you will also be able to process or
   reprocess videos on the server-side.

How does it work in 6 bullets?
++++++++++++++++++++++++++++++
- A camera is setup, such that it can see an entire cross section from left to right bank.
- A few measurement are collected:

  - a bottom cross-section, measured in 3D coordinates, in view of the camera, and;
  - a few "control points" measurements, also in 3D coordinates in the same reference system. The software uses these
    to estimate the 3D angles and position of the camera with respect to the measured cross section.

- These measurements are fed into the software using a user-friendly interface
- The software is set to record and analyze videos at set intervals.
- Each video is analyzed for movements of patterns around the cross-section. Thanks to the measurements, pixels per
  second can be converted in meters per second.
- Data is sent automatically to a central [LiveORC](https://github.com/localdevices/LiveORC) server for further use in
  decision support or other operational processes.

Features
++++++++

- Set up fully automated processing of videos into water levels and discharges, leveraging the power of
  [PyOpenRiverCam](https://github.com/localdevices/pyorc)
- Set up your own automated water level feeds from external (e.g. web-reporting) or connected devices.
- Download your data, directly from the device via the web interface.
- Sync your data Live(!) to a [LiveORC](https://github.com/localdevices/LiveORC) server setup for operational real-time
  use of data in Decision Support Systems or forecast systems.
- Monitor currently ongoing tasks and logs.
- Investigate your time series and results with powerful figures and graphs.
- Secure access to your device via a hashed password.
- Stay up-to-date with the latest developments of OpenRiverCam OS through Over-The-Air updates.

For whom
++++++++
ORC-OS is meant for professional organizations that want to set up their own image-based discharge measurement sites
withcameras.



