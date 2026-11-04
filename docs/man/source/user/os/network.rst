.. _os-network:

5.12 Network (Network Devices)
==============================

.. index::
   single: Network (Network Devices)

Network lists every device on the rack's data network and is where you give the processors their pins. It is program 4 in the Logic group; open it with **NET**.

5.12.1 Screen
-------------


.. _figure-5-9:

.. figure:: /images/os-network.png
   :alt: Network Devices listing 28 devices with name, type, reference ID and pin, and a hint about pins d0 to d5 and F1
   :width: 100%

   **Figure 5-9** 28 devices on this rack's network. The note under the list explains the pins, and says where **F1** will store an ID: at the editor cursor, 0000 here.

The header gives the number of devices the rack can see. Each row then shows a device's number, name, type and reference ID, and a Pin column: d\ *n* when the device is a processor pin, or P\ *n* when it only sits on I/O port *n*. Devices reached through a data bridge are marked as such, and with no data cable connected the list simply says so.

5.12.2 Keys
-----------


.. _table-5-13:

.. table:: **Table 5-13** Network keys

   +---------------------------------------------+-----------------------------------------------------+
   | Key                                         | What it does                                        |
   +=============================================+=====================================================+
   | **UP** / **DN**, **PG+** / **PG-**, **TAB** | Select a device                                     |
   +---------------------------------------------+-----------------------------------------------------+
   | **0**–**5**                                 | Make the selected device pin d0–d5 for every        |
   |                                             | processor                                           |
   +---------------------------------------------+-----------------------------------------------------+
   | **F1** or **ENT**                           | Stores the device's reference ID in the memory cell |
   |                                             | at the editor cursor                                |
   +---------------------------------------------+-----------------------------------------------------+
   | **F2**                                      | Puts the device on the selected logger channel (see |
   |                                             | :ref:`5.11 Logger <os-logger>`)                     |
   +---------------------------------------------+-----------------------------------------------------+
   | **F3**                                      | Moves the device to the next I/O port, 1–32         |
   +---------------------------------------------+-----------------------------------------------------+
   | **F4**                                      | Clears every I/O port                               |
   +---------------------------------------------+-----------------------------------------------------+
   | **F5**                                      | Saves the pins, I/O ports and logger devices to the |
   |                                             | drive in the selected bay; with the modifier, loads |
   |                                             | them back                                           |
   +---------------------------------------------+-----------------------------------------------------+

5.12.3 Pins and I/O ports
-------------------------

.. index::
   single: Pins and I/O ports

The rack has 32 I/O ports, each of which holds one device ID. Ports 1–8 have sockets on the patch field, and the six pin cables plug into them: out of the box, d0 is in port 1 and d5 in port 6, leaving ports 7 and 8 without a pin (see :ref:`6 Storage and data handling <ch-storage>`). Ports 9–32 have no sockets at all. Their device IDs sit in memory cells 4160–4183, ready for programs that use ``ld`` and ``sd`` with a device ID, while the IDs on ports 1–8 sit in cells 4128–4135.

A device occupies one port at a time, so giving it a new port or pin removes it from the old one. How programs use pins and ports is covered in :ref:`11 Programming (IC10) <ch-programming>`.

5.12.4 Giving a processor pin a device
--------------------------------------

.. index::
   single: Giving a processor pin a device

**Requirements:** The device must be on the rack's data network.

1. Select the device with **UP** and **DN**.
2. Press the digit of the pin you want, **0**–**5**.

**Result:** The device's ID goes onto the I/O port that the pin's cable is plugged into, and every processor in the rack now sees the device on that pin. If the pin's cable was pulled, the rack first plugs it into a free port for you and logs where it went. When all eight socketed ports are taken, the rack says so and changes nothing.

5.12.5 Storing a device ID in memory
------------------------------------

.. index::
   single: Storing a device ID in memory

**Requirements:** The editor cursor must point at a writable cell.

1. Select the device with **UP** and **DN**.
2. Press **F1**.

**Result:** The device's reference ID is written to the cell at the editor cursor, where a program can pick it up and use it with ``ld`` and ``sd``.
