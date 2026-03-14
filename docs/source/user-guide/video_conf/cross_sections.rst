.. _vc_water_level:

Water level and cross-sections
------------------------------

.. note::

   Water levels and cross-sections are needed to determine the wetted area of the channel, which in turn is needed to
   determine discharge. During your survey, you should measure the water level and cross-section in the same coordinate 
   reference system as used for the camera pose and the ground control points so that the camera "understands" how
   it is aimed towards the water and cross section.

Entering water levels
^^^^^^^^^^^^^^^^^^^^^

The water level is set in the cross-section tab. You here set the water level as it occurred during the survey.
The water level is needed for two reasons:

- most importantly: to notify ORC of possible offsets between the vertical datum used in your survey measurements and
  water levels as measured by a device. Remember that to process any video, the water level during that video is needed
  and any local device reporting this may be used. The vertical level must however be translated to the level used in 
  your survey. You therefore must provide the water level in two different ways:

    1. as measured during your survey in ``Water level in GCP coordinate system [m]``. This water level is indicated 
       with the black arrow on the left-hand side of the image shown below. 
    2. as measured at the same moment, but through the water level measurement device in
       ``Water level in local gauge reference [m]``. This is illustrated with the green arrow on the right-hand side of 
       the image shown below. The image suggests a staff gauge is the local reference, but this can also be a 
       pressure sensor or any other device that can be used to measure water level. The only requirement is that you
       can translate the water level as measured by this device to the water level in the GCP coordinate system. 
       This is done by providing both water levels as described above.
   
  .. figure:: ../../_images/_video_conf/water_level.png
     :align: center
     :alt: water level schematic

     Schematic overview of water level measurements. Black arrow - Water level measured in GCP coordinate system. 
     Green arrow - Water level measured in local gauge reference. Source: adapted from ChatGPT.

  If you will only optically measure water level then choose a logical reference, for instance the bottom of the
  cross section. This will allow you to easily update the cross-section if you wish to do so, without creating
  offsets in the discharge - water level relationship.
- second: to visually check if your measurements seem right. After selecting the water level and a cross-section
  you will be able to visually see the wetted cross-sectional surface as well as the planar wetted surface.

Fill in the two water levels in the cross-section tab as shown below. The color coding is the same as in the figure 
above.

.. figure:: ../../_images/_screenshots/video_config_water_level.png
   :align: center
   :alt: water level settings

   Water level settings in the cross-section tab. 
   Black rectangle - Water level measured in GCP coordinate system.
   Green rectangle - Water level measured in local gauge reference.


.. _vc_cross_sections:

Uploading and selecting cross sections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. important::

   It is important to understand what is meant by a "cross section". A cross section in OpenRiverCam terms, is a set
   of coordinates measured in the same coordinate system as used for all other measurements, that describes the
   bottom of the channel. There is often confusion about the vertical (Z) coordinate. This may with certain
   instrumentation (e.g. echo sounders)be measured as the **depth** of the channel, meaning that the lowest bottom 
   coordinate appears
   as the highest value. This is **not** correct because your cross-section dataset should instead describe the
   bottom *coordinate*. If for instance the ``X, Y, Z`` coordinate of your camera is measured as ``0, 0, 0``, then the
   bottom coordinates of your cross-section will all have a lower ``Z`` value than zero with the lowest point in the
   channel having the lowest ``Z`` value. Before using a cross-section you **must** therefore make sure its 
   coordinates share the same vertical reference as all other measurements i.e. control points and the water level.

The cross-section is needed to determine the wetted area of the channel, which is needed to determine discharge. You 
can upload one or more cross-sections and use these for multiple video configurations. For instance: you may decide to 
resurvey after the camera has moved or its direction has been changed. If GCPs remain in the same coordinate reference 
system and the cross-section has not changed, you may use an existing cross-section. 

You can also decide to upload multiple cross-sections for the same video configuration, for instance if you have 
surveyed multiple cross-sections during the survey, e.g. one that describes the cross-sectional wetted perimeter and 
one that describes the shape along a clear channel form, which works better for optical estimation of water levels.
This may (ideally) for instance be a vertical structure such as a concrete embankment, a bridge pier or a staff gauge,
close enough to the camera to be clearly visible. See our tip below for how to make a "cross section" that uses
points along known vertical objects like placed staff gauges.

To upload a cross-section, go to the ``Cross sections`` tab and click on the "Upload cross-section" button. This will 
open a file dialog. Select the file containing the cross-section coordinates. The file must be a CSV file obeying
to the following **strict** rules. Make sure the file is properly formatted before uploading:

* It must have three columns strictly named "X", "Y" and "Z" for the horizontal (x, y) coordinates and vertical (z)
  coordinates respectively.
* X, Y and Z coordinates **MUST** be in a meter unit projection. If your measurements are in another unit, you must
  convert them to meters before uploading. If your measurements are in a geographic coordinate system (e.g. WGS84 lat-lon), 
  you must first project them to a meter unit projection before uploading. In this process, make sure that also your
  GCPs and water level measurements are in the same meter unit projection.
* X and Y should follow the horizontal directions left-right (positive-X), and backward-forward (positive-Y), e.g. 
  west-east and south-north respectively. Positive-Z is in upward direction always! GPS and the Disto P2P systems
  always follow this convention. Note that x-y can be any perpendicular directions you wish as long as they follow the 
  horizontal plane.
* The points must be ordered from left to right or right to left bank. If the points are not ordered, you will not 
  receive an error, but results will become very very unpredictable! Order your points (e.g. in excel) before uploading
  or (easier) just make sure you go in one direction only while surveying.
* You can supply a file with more columns, containing for instance ID, notes, names of each point etc. taken during the
  survey, or any other information you may wish to save. It should be noted however, that these details will not be 
  stored in the database. Save your files as a backup!

You may also decide to "Straighten cross section". If you enable this option before selecting "Upload", the points.

.. note::

   Cross sections in GeoJSON format are also supported. In this case, also the geographical coordinate reference system
   will be stored alongside the coordinates. You **MUST** however then also upload your GCPs in GeoJSON format to
   ensure that the same coordinate reference system is used for all measurements.   

.. tip::

  How about measuring water levels optically from staff gauges? Optical water level estimation can be done by defining
  a "cross section" which is merely a smart horizontal and vertical interconnection of points on known vertical 
  structures. For instance you may have installed a camera on a mast looking at two staff gauges or (better) white
  colored plates. You can measure the X-, Y-coordinates of the lowest staff 
  gauge, measure the Z-coordinate of the lowest point and highest point of the staff gauge. Then measure the X-, 
  Y-coordinates of the second staff gauge and also the lowest (Z) point and highest point. Then in Excel create a set of 
  cross section points that connects the two with each other. For the other side (not used in practice) you may then 
  create some arbitrary points towards the farthest bank. The 2-D schematic shown in the figure below demonstrates
  this idea. Just make sure that both (or all if you have more than 2) staff gauges have some overlap in the vertical,
  and that you finish the cross section by adding some arbitrary far-shore points so that you can select the nearest
  bank to detect the water level on.

  You should with this approach consider that the rectangular area should have a relatively small width, in the order
  of the width of your staff gauge, change the 3 meter default value to e.g. 0.3.
  
  .. plot:: ./_scripts/plot_camera_staff_gauge.py
    :alt: Schematic of cross section for optical water level estimation

    Schematic representation of a "cross section" that can be used to detect water levels, which is not a real 
    cross section, but more a connection of known vertical orientation points.
    
