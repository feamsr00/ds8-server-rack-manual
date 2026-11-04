.. _os-perf:

5.7 Perf (Performance Monitor)
==============================

.. index::
   single: Perf (Performance Monitor)

Perf draws three graphs of the rack's recent history and keeps a running tally of its memory traffic. It is program 3 in the System group; open it with **PRF**. When something has been creeping upwards, this is where you will see it creep.

5.7.1 Screen
------------


.. _figure-5-4:

.. figure:: /images/os-perf.png
   :alt: Performance Monitor with graphs for core temperature (0 to 100 C), power (0 to 500 W) and I/O (0 to 120 operations a second), and a Totals panel
   :width: 100%

   **Figure 5-4** Perf at the default sample time of 2 s. The power and I/O scales follow the rack's maximum, here 0–500 W and 0–120 operations a second.

.. _table-5-5:

.. table:: **Table 5-5** Perf screen

   +------------------+------------------------------------------------------+
   | Panel            | What it shows                                        |
   +==================+======================================================+
   | Core temperature | The last 60 samples, on a 0–100 °C scale             |
   +------------------+------------------------------------------------------+
   | Power            | The last 60 samples of the power draw, scaled to the |
   |                  | rack's maximum                                       |
   +------------------+------------------------------------------------------+
   | I/O              | The last 60 samples of memory operations per second, |
   |                  | and the current load as a share of full load         |
   +------------------+------------------------------------------------------+
   | Totals           | Reads, writes and faults since the last reset, the   |
   |                  | up time, and the UPS charge, marked "discharging"    |
   |                  | while on battery                                     |
   +------------------+------------------------------------------------------+

Each graph holds 60 samples, so at one sample a second it covers the last minute, and at ten seconds the last ten minutes. The graphs are not saved with the game.

5.7.2 Keys
----------


.. _table-5-6:

.. table:: **Table 5-6** Perf keys

   +--------+----------------------------------------------------+
   | Key    | What it does                                       |
   +========+====================================================+
   | **F1** | Resets the I/O counters                            |
   +--------+----------------------------------------------------+
   | **F2** | Selects the next sample time: 1, 2, 5 or 10 s,     |
   |        | starting at 2 s. The **SAMPLE** knob on the switch |
   |        | strip does the same                                |
   +--------+----------------------------------------------------+

5.7.3 Related data
------------------


Programs can read the same counters directly from memory cells 4109–4111 (see :ref:`12 Logic and memory reference <ch-reference>`).
