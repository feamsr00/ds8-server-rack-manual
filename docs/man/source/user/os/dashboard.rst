.. _os-dashboard:

5.14 Dashboard (Base Dashboard)
===============================

.. index::
   single: Dashboard (Base Dashboard)

Dashboard shows every device on the data network at a glance, together with everything currently in alarm. It is program 12 in the Automation group; open it with **HOME**, then **1**. It is the closest thing the rack has to a control-room wall.

5.14.1 Screen
-------------


.. _figure-5-11:

.. figure:: /images/os-dashboard.png
   :alt: Base Dashboard: 28 devices, 0 rules, 0 tasks, a device list with doors and wall lights, and Alarms none
   :width: 100%

   **Figure 5-11** 28 devices, no rules or library tasks yet, and nothing in alarm.

The header line counts the devices, the rules (and how many of them are active) and the library tasks running. The device list shows each device's name, type and main value: its pressure, temperature, charge, power, oxygen or on/off state, whichever suits the device. Below it, the Alarms panel lists every rule set to "Raise alarm" and every room-alarm or leak-alarm library task that is currently active. When there are none, it says that all is quiet.

5.14.2 Keys
-----------


.. _table-5-16:

.. table:: **Table 5-16** Dashboard keys

   +---------------------------------------------+------------------------------------+
   | Key                                         | What it does                       |
   +=============================================+====================================+
   | **UP** / **DN**, **PG+** / **PG-**, **TAB** | Scroll the device list             |
   +---------------------------------------------+------------------------------------+
   | **F1**                                      | Opens :ref:`5.15 Rules <os-rules>` |
   +---------------------------------------------+------------------------------------+
   | **F2**                                      | Opens the running tasks in         |
   |                                             | :ref:`5.17 Library <os-library>`   |
   +---------------------------------------------+------------------------------------+
