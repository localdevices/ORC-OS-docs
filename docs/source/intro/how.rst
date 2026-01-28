.. _how:

How does it work in 6 bullets?
------------------------------
- A camera is setup, such that it can see an entire cross section from left to right bank.
- A few measurement are collected:

  - a bottom cross-section, measured in 3D coordinates, in view of the camera, and;
  - a few "control points" measurements, also in 3D coordinates in the same reference system. The software uses these
    to estimate the 3D angles and position of the camera with respect to the measured cross section.

- These measurements are fed into the software using a user-friendly interface
- The software is set to record and analyze videos at set intervals.
- Each video is automatically analyzed for movements of patterns around the cross-section. Thanks to the measurements,
  pixels per second can be converted in meters per second.
- Data is sent automatically to a central `LiveOpenRiverCam`_ server for further use in
  decision support or other operational processes.

.. _feats:

Features
--------

- Set up fully automated processing of videos into water levels and discharges, leveraging the power of
  `PyOpenRiverCam`_
- Set up your own automated water level feeds from external (e.g. web-reporting) or connected devices.
- Download your data, directly from the device via the web interface.
- Sync your data Live(!) to a `LiveOpenRiverCam`_ server setup for operational real-time
  use of data in Decision Support Systems or forecast systems.
- Monitor currently ongoing tasks and logs.
- Investigate your time series and results with powerful figures and graphs.
- Secure access to your device via a hashed password.
- Stay up-to-date with the latest developments of OpenRiverCam OS through Over-The-Air updates.

.. _PyOpenRiverCam: https://github.com/localdevices/LiveORC
.. _LiveOpenRiverCam: https://github.com/localdevices/LiveORC