.. _prerequisites:

Examples of hardware services
-----------------------------

Switching of a relay
++++++++++++++++++++

.. code-block:: python

    import RPi.GPIO as GPIO
    import time

    # Use BCM pin numbering
    GPIO.setmode(GPIO.BCM)

    # Define relay pin
    RELAY_PIN = 17
    RELAY_PIN = 21

    # Setup relay pin as output
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    for n in range(3):
        try:
            time.sleep(0.5)
            print("Relay ON")
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn relay on
            time.sleep(0.5)                      # Wait 5 seconds
            print("Switch on again")

            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn relay on
            time.sleep(0.5)                      # Wait 5 seconds
            print("Relay OFF")
            GPIO.output(RELAY_PIN, GPIO.HIGH)   # Turn relay off
        except:
            print("Not working")

    GPIO.cleanup()  # Reset GPIO state`
