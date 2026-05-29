.. _processing:

Processing options
------------------

.. note::
    
   The processing options may seem overwhelming at first, but most of the options have a default value that is based on
   our experience with processing videos from a wide range of rivers and camera setups. We therefore recommend to
   first try processing your videos with the default settings, and only change settings if you have a good reason to do 
   so. The default settings are based on the following assumptions:

   * About a 20-30 meter wide river is recorded at 15 FPS with a resolution of 1920x1080 pixels.
   * The bathymetry does not vary suddenly over short distances. This means sampling along the cross section can be done
     with a modest spacing.
   * The videos are recorded with a camera that is not moving and has a fixed focus. This means all frames including 
     the first are sharp.

The processing parameters influence how the video is processed from raw footage to discharge. We describe the parameters
briefly in small sections in the table below, with a practical guidance how to use them and when to change them.

When you have set or changed the settings, we recommend clicking on the "Save" button and then the "Run" button next to
it to try the settings. Investigate the results in the "Video" menu. If you are not satisfied, then go back to the 
settings, change them and run again.

The most prominent settings you usually have to modify slightly are:

- start and end frame (put them on a high enough value to ensure you process the entire video)
- resample frame distance (put it on a higher value to be able to detect higher velocities, or on a lower value to be 
  able to detect lower velocities)
- pixel resampling size (put it on a higher value to be able to process larger rivers, or on a lower value to be able to
  process smaller rivers)
- velocity sampling distance (put it on a lower value to be able to capture more small scale variation in velocity, on 
  small streams, or on a higher value to save processing time if you have a very large river with little small scale 
  variation in velocity).
- plotting sizes. This really depends on your personal preferences. Experiment with these values to find the best 
  settings for your videos and your personal preferences.

Details on all settings are given below.

Video settings
^^^^^^^^^^^^^^
Several parameters are available that influence how many frames are extracted from the video, and how the video
is resampled to real-distance "orthorectified" grids. These can be found under "Video settings".

.. list-table::
    :header-rows: 1
    :widths: 25 35 40

    * - Setting
      - Description (default)
      - Guidance
    * - Start and end frame
      - The first and last frame of the video to process. Default: 0, and amount of frames in the sample video. 
      - Set the first to a higher value (e.g. 15) in case the camera may be out of focus in the first frames.
        Set the last value to a higher value if you expect that your future videos will be longer. 5 seconds is a good 
        starting point. If you record at 15 FPS, this means 75 frames.
    * - Read frames in one go or in smaller chunks (default: one go)
      - Whether to read all frames in one go, or to read them in smaller chunks to save RAM.
      - Usually, this setting can be ignored. Only change it if you deal with very large areas of interest and you
        experience memory issues. E.g. drone footage at 100 meters elevation with a large width and 4K video resolution
        or hardware with very little RAM (e.g. 4GB).
    * - Resample frame distance (integer, default: 1)
      - The distance between each frame to read. E.g. if set to 2, only every second frame is utilized. 
      - The default value of 1 is based on our experience with videos of about 20-30 meters wide recorded at 15 FPS 
        with a resolution of 1920x1080 pixels and resampling the video to 0.01 meter. Basically this means 1px/frame
        translates to 0.15 meters per second velocity. If you choose this setting too high, then patterns seen in one
        frame may no longer be visible in the next frame. If you choose it too low, then you may not be able to detect
        relatively low velocities. In green text, guidance is given on how your settings (resolution and frame distance)
        will affect the expected detectable minimum flow velocity.
    * - Pixel resampling size (float, default: 0.01)
      - The resampling resolution from raw video to orthorectified. E.g. if set to 0.01, then the video is resampled to 
        0.01 meter per pixel. In the orthorectification process, a video is projected in such a way that you get a 
        planar view of the river, i.e. as if you look at the stream from directly above it, or in the way you would 
        look at it in a Geographical Information System (GIS).
      - Typical guidance: for a stream of 10-20 meters, choose 0.01 m, for 20-40 m , 0.02 m , > 40 0.03 m or (if flow
        patterns seem very large scale) even 0.05 m. For small ditches or drainage canals, you may even make this 0.001 m.
    * - Interrogation window size (integer, default 64)
      - the amount of pixels (rows x columns) used to find a patterns on the water. E.g. if set to 32, then a 32x32 
        pixel window is used to find patterns on the water.
      - The default value of 64 is based on our experience and we recommend not changing this unless there is a very 
        good reason for it. If you want more resolution in your processed velocity grid, then usually it is better
        to change the Pixel resampling size option.
    * - Produce one velocity estimate over entire frame-range? (default: yes)
      - Setting to yes (default) means all frames are jointly analyzed to produce one velocity estimate per 
        interrogation window. This reduces noise and allows for detecting lower velocities more accurately. 
        Setting this to no however means a velocity is estimated for each individual frame and can give an impression
        of the uncertainty (not shown but can be found in the downloaded timeseries CSV files). 
      - We recommend to set this to yes, as this gives the best results for most videos. Setting it to no can be useful
        if you insist having an individual uncertainty estimate for each video, or if you suspect the framerate of the
        used camera is not stable.

.. note::
   
   Unstable frame rates may occur if you have a cheap camera, or a camera read directly from a web stream like RTSP 
   or WebRTC, causing framedrops. In such cases, it may be useful to set the "Produce one velocity estimate over entire 
   frame-range?" setting to no. This will give you more reliable velocimetry results.

.. _optical_water_level:

Optical water level
^^^^^^^^^^^^^^^^^^^
If you decide to estimate the water level from the video then several additional settings are available that 
determine how the video with the cross section supplied under the "Cross sections" tab are used to estimate the 
water level. It may require some iterations under different water level conditions to get the most optimal settings 
here. We however recommend starting with the defaults.

.. list-table::
    :header-rows: 1
    :widths: 25 35 40

    * - Setting
      - Description (default)
      - Guidance
    * - Minimum and maximum water level (default: from optical cross section)
      - by default, this is set to the minimum and maximum level found in the cross section selected for
        optical water level estimation. 
      - In most cases not needed to change this. If you deem very low or high levels unrealistic, or think these may 
        introduce wrong detection of water levels, you may change this value. You will see the changes reflected in 
        the "Side view" panel.
    * - Land in/outward distance to measure intensity differences (default 0.5m)
      - To detect water levels, ORC will sample a horizontally oriented rectangle of pixels left and right of possible
        locations in the cross section where the water line is located. This measure determines the distance from 
        crossing land inwards or outwards.
      - Usually it is not needed or recommended to change this, unless your camera's angle is very oblique, you may
        then consider to make this value larger.
    * - Size of element to measure water level on (default 3 meters)
      - Similar to the previous, but then the length of the rectangle along the shoreline. 
      - Usually not needed or recommended to change. If you have a very clear uniform cross section, like a long 
        concrete wall to measure water level against, you can choose a larger value here to make detection more robust.
        If the channel is more natural, choose a lower value. If you measure over an object, then use the width of that
        object.
    * - Best visible bank for detection (radio button, default: Far bank)
      - Water level is only detected from the bottom to either the left or right shoreline. You choose which one by
        indicating if you want to detect it on the bank furthest away, or closest to the camera.
      - Usually the far bank is easier visible over the entire bottom to top range. If you have a cross section with 
        the nearest shore being entirely visible over a length similar to the "Size of element" setting, you may
        however decide to use the nearer shore for better results.
    * - Stream characteristics
      - Man-made is selected as default because the optical level detection methods work best on man-made channels.
      - Different preprocessing combinations are used here to extract a good land/water segmentation from your videos.
        For instance, the "Man-made" option first attempts to resolve water levels from the range of intensities 
        measured over the entire video where the assumption is that moving water will show much more variation than
        non-moving banks made out of a man-made material. If this yields a too low signal-to-noise ration (see below) 
        then it will fall back to greyscale. Other bank types may be chosen, but in general man-made conditions work
        well, and natural do not work well. In natural channels consider installing a level gauge sensor, or install 
        a clear stable object close to the camera. See additional note below for more information.
    * - Signal-to-noise ratio for measuring levels (default: 3.0)
      - the ratio of the optimal score identifying the water level in the cross section and the mean of the scores
        over the entire cross section. If this ratio is too low, then the water level detection is not reliable and the 
        water level is not set.
      - For well-defined banks, e.g. a concrete wall or wide enough staff gauge plate, the default value of 3.0 works
        well. For more natural banks, you may want to lower this value to e.g. 2.0, but be aware that this may
        introduce more chance of wrong detection. In general, if you have a natural bank, we recommend
        installing a clear stable object close to the camera to improve water level detection, or install a level gauge 
        sensor and set up automated readings following :ref:`water level settings <water_level>`. You may also paint 
        a clear stable object, like a white broad patch over the vertical.

Discharge estimation
^^^^^^^^^^^^^^^^^^^^
Two settings can be managed to extract discharge from the video. These are found under "Discharge estimation".

.. list-table::
    :header-rows: 1
    :widths: 25 35 40

    * - Setting
      - Description (default)
      - Guidance
    * - Velocity sampling distance (default: 0.5 m)
      - The distance between points in the cross section where velocity is sampled to estimate discharge. E.g. if set 
        to 0.5, then velocity is sampled every 0.5 meter along the cross section.
      - For small streams, you probably want to reduce this value. Also if you have streams with a lot of small scale
        variation in velocity, you may want to reduce this value. This may for instance be the case with reasonably 
        wide artificial storm drains, with small conveyance channels in the middle, which convey water during dry
        periods. If you still wish to capture velocities in the smaller conveyance channel, a reduction to e.g. 0.1 or
        0.2 may be required. For large streams, you may want to increase this value to save some processing time.

Plotting
^^^^^^^^
For each video, an augmented reality plot will be made. This plot can also be sent along with the time series record
to :ref:`LiveORC <liveorc>` if this is selected in the :ref:`Daemon settings <daemon_settings>`. A number of settings
are available to make your plot look the way you want it to look. These can be found under "Plotting".

.. list-table::
    :header-rows: 1
    :widths: 25 35 40

    * - Setting
      - Description (default)
      - Guidance
    * - Grid arrow scale (default: 1.0)
      - The scale of the arrows in the velocity grid. E.g. if set to 2.0, the arrows will be twice as long as the
        default.
      - The default creates a quiver arrow, that is scaled according to the real distance viewed in the objective.
        If your stream is really small, but the velocities are still quite large, you may find the arrows too large
        and you may want to reduce this value. If your stream is really large, but the velocities are still quite small, 
        you may want to increase this value. Bear in mind that slow flowing rivers, can become fast during high flows!
        Experimenting with this value may make sense.
    * - Cross section arrow scale (default: 1.0)
      - The scale of the arrows of the sampled velocities along the cross section. E.g. if set to 2.0, the arrows will
        be twice as long as the default.
      - Similar to the previous, but then for the cross section plot. The same guidance applies here as for the grid
        arrow scale. A value of 1.0 is twice as long as the grid arrow scale.
    * - Grid arrow width (default: 1.0)
      - A width measure of the arrows in the velocity grid. E.g. if set to 0.5, the arrow line will be half as thick
        as the default.
      - The default usually looks nice, but if you think the plot is somewhat cluttered, you may want to reduce this 
        value. If you think the arrows are too thin, you may want to increase this value. Go ahead and experiment!
    * - Cross section arrow width (default: 1.0)
      - A width measure of the arrows of the sampled velocities along the cross section. E.g. if set to 0.5, the arrow
        line will be half as thick as the default.
      - Similar to the previous, but then for the sampled cross section velocities. The same guidance applies here as
        for the grid arrow width.

.. tip::

   In general, we recommend to iteratively change the processing settings with one or a few sample videos, ideally 
   spanning low and high flow conditions. This will help you get an impression what the different settings do, and what
   the optimal settings are. The most critical ones for velocity estimation are the "Resample frame distance" and 
   "Pixel resampling size" settings as these influence largely the lower velocity values that you can still
   reliably estimate. Perhaps counterintuitively, lowering the resample frame distance typically leads to a higher
   sensitivity to also measure low flows. If your camera records at 60 (30) FPS, and your stream velocities are within a 
   normal natural stream limits (e.g. 0.1 to 3 to 4 meter per second), then consider putting this value at 4 (2) as this
   can lead to more accurate detection of low flows. To save storage, you may also simply put your camera FPS to 15.

