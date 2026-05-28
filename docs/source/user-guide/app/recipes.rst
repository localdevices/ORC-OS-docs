.. _recipes:

Recipes
-------


.. screenshot:: http://localhost:5173/recipe
  :browser: chromium
  :viewport-width: 1280
  :viewport-height: 960
  :color-scheme: dark
  :status-code: 200,302

This page is only meant to administrate recipe records. You can here remove recipes that are not used if you wish.
They are not large to store, so it is usually not needed to delete them. You can also conveniently store the recipes
as YAML files after which they can be used in |PyOpenRiverCam| on the command line interface. This can be useful for batch
reprocessing with identical processing settings. Recipe names are typically identical to names of video configs so
that you can easily find the right recipe back.

.. _PyOpenRiverCam: https://github.com/localdevices/LiveORC
