.. _vc_water_level:

Setting the water level
-----------------------

The water level is set in the cross-section tab. You here set the water level as it occurred during the survey.
The water level is needed for two reasons:

- most importantly: to notify ORC of possible offsets between the vertical datum used in your survey measurements and
  water levels as measured by a device. Remember that to process a video, the water level is needed and any local
  device reporting this may be used. The vertical level must however be translated to the level used in your survey.
  You therefore must provide the water level twice:

    1. as measured during your survey in ``Water level in GCP coordinate system [m]``
    2. as measured at the same moment, but through the water level measurement device in
       ``Water level in local gauge reference [m]``

  If you will only optically measure water level then choose a logical reference, for instance the bottom of the
  cross section. This will allow you to easily update the cross-section if you wish to do so, without creating
  offsets in the discharge - water level relationship.
- second: to visually check if your measurements seem right. After selecting the water level and a cross-section
  you will be able to visually see the wetted cross-sectional surface as well as the planar wetted surface.

.. _vc_cross_sections:

Uploading and selecting cross sections
--------------------------------------

.. note::

   It is important to understand what is meant by a "cross section". A cross section in OpenRiverCam terms, is a set
   of coordinates measured in the same coordinate system as used for all other measurements, that describes the
   bottom of the channel. There is often confusion about the vertical (Z) coordinate. This may with certain
   instrumentation be measured as the **depth** of the channel, meaning that the lowest bottom coordinate appears
   as the highest value. This is **not** correct because your cross-section dataset should instead describe the
   bottom coordinate. If for instance the ``x, y, z`` coordinate of your camera is measured as ``0, 0, 0``, then the
   bottom coordinates of your cross-section will all have a lower ``z`` value than zero. Before using a cross-section
   you **must** therefore make sure its coordinates share the same vertical reference as all other measurements
   i.e. control points and the water level.

.. plot::

   import matplotlib.pyplot as plt
   import matplotlib.image as mpimg
   import numpy as np
   plt.plot([0, 1], [1, 0])
