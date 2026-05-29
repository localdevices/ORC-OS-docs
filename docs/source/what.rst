.. container:: figure-text-pair wide-text


   .. container:: column

      A relatively simple camera system can be utilized to measure accurately in **m3/s** how much water flows
      through a stream. Look at this example, where a staggering 5 meter per second (!) velocity was observed in a storm
      drain in Lusaka. There is **no other method** in the world that can measure such extreme flows.

      OpenRiverCam OS (ORC-OS) is an entirely open-source dashboard to organize automated measurements of water levels and river flows
      using camera videos. It is currently supporting usage directly on measurement sites, and is meant to be deployed on
      a linux-based Single-Board-Computer (SBC). It is optimized for use on Raspberry Pi 5 devices and
      can utilize connected Raspberry Pi cameras natively, or IP cameras connected via a network cable.

   .. container:: column

      .. figure:: _images/_general/ngwerere_20260103.jpg
          :width: 300px

.. tip::

    We provide read-to-use images for Raspberry Pi 5 with support, as well as other products
    and services to get you started. Check our https://openrivercam.org for more information.

Navigation
==========

For quick references to the most important parts you need to get a running station,
please check the following major sections of the documentation. They are ordered
the way you will need them when setting up your station.

The menu bar on top helps you navigate through all detailed sections.

.. grid:: 2
    :gutter: 1

    .. grid-item-card::
        :text-align: center
        :link: hardware
        :link-type: ref

        :octicon:`cpu;5em;sd-text-icon blue-icon`
        +++
        **Hardware guidance**

        Do you want to know how to get a station assembled? Start here with guidance on parts and a full assembly example.

    .. grid-item-card::
        :text-align: center
        :link: field_guide
        :link-type: ref

        :octicon:`device-camera;5em;sd-text-icon blue-icon`
        +++
        **Field survey**

        Where should you put your station? And how should you aim and survey it? Check this section for more information.

    .. grid-item-card::
        :text-align: center
        :link: sample_video
        :link-type: ref

        :octicon:`gear;5em;sd-text-icon blue-icon`
        +++
        **Configure your station**

        Once setup and aimed, it is time to configure your station. The video configuration section helps you with the entire process, including examples.

    .. grid-item-card::
        :text-align: center
        :link: user-guide
        :link-type: ref

        :octicon:`book;5em;sd-text-icon blue-icon`
        +++
        **User guide**

        Our full ORC-OS software guide leads you through all features of the web front end, configuration of bespoke services and operationalization of data flows.

.. note::

   In the near future, cloud processing will also become possible through `LiveOpenRiverCam`_,
   the open-source server-side API. With this, only an IP-camera with power and an internet connection
   will be needed on site.

.. _LiveOpenRiverCam: https://github.com/localdevices/LiveORC