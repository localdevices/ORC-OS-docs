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

Optical water level
^^^^^^^^^^^^^^^^^^^
If you decide to use the video to estimate the water level then several additional settings are available that 
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
    * - Size of element to measure water level on (3 meters)
      - Similar to the previous, but then the length of the rectangle along the shoreline. 
      - Usually not needed or recommended to change. If you have a very clear uniform cross section, like a long 
        concrete wall to measure water level against, you can choose a larger value here to make detection more robust.
    * - Best visible bank for detection (radio button, default: Far bank)
      - Water level is only detected from the bottom to either the left or right shoreline. You choose which one by
        indicating if you want to detect it on the bank furthest away, or closest to the camera.
      - Usually the far bank is easier visible over the entire bottom to top range. If you have a cross section with 
        the nearest shore being entirely visible over a length similar to the "Size of element" setting, you may
        however decide to use the nearer shore for better results.
    * - Stream characteristics
      - Different preprocessing combinations are used here to extract a good land/water segmentation from your videos.
        For instance, the "Man-made" option first attempts to resolve water levels from the range of intensities 
        measured over the entire video where the assumption is that moving water will show much more variation than
        non-moving banks made out of a man-made material. If this yields a too low signal-to-noise ration (see below) 
        then it will fall back to greyscale. Other bank types may be chosen, but in general man-made conditions work
        well, and natural do not work well. In natural channels consider installing a level gauge sensor, or install 
        a clear stable object close to the camera. See additional note below for more information.
    * - Signal-to-noise ration for measuring levels






