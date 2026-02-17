.. _timeseries:

.. role:: redtext
  :class: red-text

.. role:: bluetext
  :class: blue-text

.. role:: greentext
  :class: green-text

.. role:: lightgreentext
  :class: light-green-text

Time series
-----------
The time series page shows detailed plots of time series with filter options to reduce noise, show specific date ranges
or filter out videos with certain quality criteria or other thresholds.

.. screenshot:: http://localhost:5173/time_series
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

By default, the time series view shows data from the last timestamp found in the database, and one week before that.
This usually gives a reasonable first view on the data in the database.

Displayed variables
+++++++++++++++++++
The following variables are available in the time series display. These can be switched on and off by clicking on the
variable in the legend. By default, all variables are displayed. The water level scale is on the primary y-axis,
velocities and discharge are displayed on the secondary y-axis. The meaning of the different variables is as follows:

.. list-table::
   :header-rows: 1
   :widths: 10 20 70

   * - Variable
     - Unit
     - Description
   * - :bluetext:`Water level`
     - meter (m)
     - Water level as measured by your own local device, derived from API, or (if not available) optically estimated
       from your videos, using a provided cross section for water level detection.
   * - :lightgreentext:`Surface velocity`
     - Meter per second (m/s)
     - Estimated by averaging all estimated velocities over the wetted part of the cross section, used to
       estimate discharge.
   * - :greentext:`Bulk velocity`
     - Meter per second (m/s)
     - Estimated by dividing discharge by the wetted surface area. Wetted surface area is calculated using the water
       level and the provided cross section for discharge estimation.
   * - :redtext:`Discharge`
     - Cubic meters per second (m3/s)
     - Discharge as calculated from video analyses. Within the analyses discharge is calculated by integrating
       velocity estimates over the wetted cross section, occurring during the video. To estimate the wetted cross
       section, the water level is being used.





Notes
+++++

:bluetext:`A few remarks are important:`

- if you have videos in your database, but have not yet processed these, you may not see anything in the time series
  graph. This is perfectly normal.
- once you have setup the :ref:`water level settings <water_level>` successfully, water levels will start to be collected at
  time intervals set by yourself. You may expect then that water levels will also be shown in the time series graph.
  If you retrieve water levels with a script, you may have more water level records than videos, and many may not be
  attached to a video. This is not a problem. It is better to have too many water levels than too few to ensure a
  recent water level is available to your videos.
- once also videos are, or have been processed, flow records will appear, as well as surface and bulk velocities.


