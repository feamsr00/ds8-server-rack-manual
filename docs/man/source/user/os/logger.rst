.. _os-logger:

5.11 Logger (Data Logger)
=========================

.. index::
   single: Logger (Data Logger)

Logger records device values into memory with no chip involved. It has four channels, each of which reads one value from one device at a fixed interval and writes it into a bank. It is program 5 in the Data group; open it with **LOG**, and start or stop any channel from any program with **REC1**–**REC4**.

5.11.1 Screen
-------------


.. _figure-5-8:

.. figure:: /images/os-logger.png
   :alt: Data Logger with four channels, each set to Temperature every 5 s on banks 4 to 7 and stopped, above a panel explaining how recordings are stored
   :width: 100%

   **Figure 5-8** All four channels at their defaults. The panel below repeats the storage layout and the IC10 line that reads channel 1.

The list shows each channel's device, value, interval, bank, samples taken and state. Out of the box every channel is set to Temperature, every 5 s, with no device, and stopped; channels 1–4 log into banks 4–7.

5.11.2 Keys
-----------


.. _table-5-11:

.. table:: **Table 5-11** Logger keys

   +-------------------+---------------------------------------------------+
   | Key               | What it does                                      |
   +===================+===================================================+
   | **UP** / **DN**   | Select a channel                                  |
   +-------------------+---------------------------------------------------+
   | **F1**            | Picks the device, from any device on the data     |
   |                   | network                                           |
   +-------------------+---------------------------------------------------+
   | **F2**            | Picks the value, from 18 common logic values that |
   |                   | the device can report                             |
   +-------------------+---------------------------------------------------+
   | **F3**            | Picks the interval: 1, 5, 10, 30, 60 or 300 s     |
   +-------------------+---------------------------------------------------+
   | **F4**            | Picks the bank                                    |
   +-------------------+---------------------------------------------------+
   | **F5** or **ENT** | Starts or stops the channel                       |
   +-------------------+---------------------------------------------------+

The **HOLD** switch on the switch strip pauses every channel at once, which is handy when you want a recording to stop without losing its place.

5.11.3 Recording a value
------------------------

.. index::
   single: Recording a value

**Requirements:** The device must be on the rack's data network, and the bank you choose must be served by a drive and not write-protected.

1. Select a channel with **UP** and **DN**.
2. Press **F1** until the device you want appears. Alternatively, select the device in :ref:`5.12 Network <os-network>` and press **F2** there.
3. Press **F2** until the value you want appears.
4. Press **F3** to set the interval, and **F4** to choose the bank if the default does not suit you.
5. Press **F5** to start recording.

**Result:** The channel's state changes to recording, and its sample count starts to climb.

5.11.4 How a recording is stored
--------------------------------

.. index::
   single: How a recording is stored

A recording occupies the whole of its bank, laid out like this with the default 512-cell drives:

.. _table-5-12:

.. table:: **Table 5-12** Recording layout

   +------------------+-----------------------------------------------------+
   | Cell in the bank | Holds                                               |
   +==================+=====================================================+
   | 0                | The number of samples taken so far                  |
   +------------------+-----------------------------------------------------+
   | 1                | The latest value                                    |
   +------------------+-----------------------------------------------------+
   | 2–511            | A ring buffer: sample *n* goes to cell 2 + (*n* mod |
   |                  | 510), and the oldest samples are overwritten        |
   +------------------+-----------------------------------------------------+

A sample is only counted once it has actually been written, so the bank must stay served and writable. A device that has disappeared, or a value it cannot report, adds to the rack's fault counter instead.

5.11.5 Reading a recording from IC10
------------------------------------

.. index::
   single: Reading a recording from IC10

Channel 1 on its default bank 4 starts at address 4 × 512 = 2048, so the latest sample is at 2049 and the sample count at 2048. With the rack on pin d0 of a chip elsewhere:

.. code-block:: text

	get r0 d0 2049        # latest sample
	get r1 d0 2048        # samples taken

From a processor inside the rack, use ``db`` in place of ``d0``.
