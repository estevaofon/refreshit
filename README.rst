refreshit
===========
A print to always print in the same line, refreshing the content

Setup
-----

.. code-block:: bash

    $ pip install refreshit

Code sample
-----

.. code-block:: python

    from refreshit import uprint
    from time import sleep

    uprint("Beautiful is better than ugly.")
    sleep(1)
    uprint("Explicit is better than implicit.\n")
    sleep(1)

.. code-block:: python

    from refreshit import uprint
    from time import sleep

    load = ["Loading", "Loading.", "Loading..", "Loading..."]
    for i in range(4):
        for item in load:
            uprint(item)
            sleep(0.2)
    uprint("Complete\n")
