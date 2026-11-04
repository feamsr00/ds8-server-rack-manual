.. _os-rules:

5.15 Rules (Automation Rules)
=============================

.. index::
   single: Rules (Automation Rules)

Rules let the rack react to the base by itself. A rule reads one value from one device and, when its condition is met, does one thing: sets a device, sets every device of a kind, recalls a scene or raises an alarm. The rack holds up to 32 rules, and they run inside it with no chip at all. It is program 8 in the Automation group; open it with **HOME**, then **2**. When rules run is explained in :ref:`5 DS-8 OS <ch-os>`.

5.15.1 Screen
-------------


.. _figure-5-12:

.. figure:: /images/os-rules.png
   :alt: Automation Rules with no rules yet, showing the example IF Gas Sensor Pressure < 90 THEN Active Vent On = 1
   :width: 100%

   **Figure 5-12** An empty rule list. The screen's own example is the same rule worked through in :ref:`5.15.5 <sec-5-15-5>`.

Each rule appears as one row, showing its condition, its action and its state. The hint line counts the rules in use out of 32.

5.15.2 Keys
-----------


.. _table-5-17:

.. table:: **Table 5-17** Rules keys

   +------------------------------+----------------------------------------------------+
   | Key                          | What it does                                       |
   +==============================+====================================================+
   | **UP** / **DN**              | Select a rule                                      |
   +------------------------------+----------------------------------------------------+
   | **<** / **>**                | Move between the rule's fields                     |
   +------------------------------+----------------------------------------------------+
   | **INC** / **DEC** or **ENT** | Change the selected field; type digits and press   |
   |                              | **ENT** for a number                               |
   +------------------------------+----------------------------------------------------+
   | **F1**                       | Switches the rule on or off                        |
   +------------------------------+----------------------------------------------------+
   | **F2**                       | Adds a new rule                                    |
   +------------------------------+----------------------------------------------------+
   | **F3**                       | Copies the rule                                    |
   +------------------------------+----------------------------------------------------+
   | **F4**                       | Deletes the rule                                   |
   +------------------------------+----------------------------------------------------+
   | **F5**                       | Saves every rule, scene and library task to the    |
   |                              | selected drive; with the modifier, loads them back |
   |                              | (see                                               |
   |                              | :ref:`6 Storage and data handling <ch-storage>`)   |
   +------------------------------+----------------------------------------------------+

5.15.3 Fields
-------------


.. _table-5-18:

.. table:: **Table 5-18** Rule fields

   +--------------------+------------------------------------------------------+
   | Field              | Choices                                              |
   +====================+======================================================+
   | IF device          | Any device on the network; only values the device    |
   |                    | can report are offered                               |
   +--------------------+------------------------------------------------------+
   | Value              | One of 18 common logic values                        |
   +--------------------+------------------------------------------------------+
   | Compare            | >, <, >=, <=, =, !=, or always (which copies without |
   |                    | a condition)                                         |
   +--------------------+------------------------------------------------------+
   | Limit              | A number                                             |
   +--------------------+------------------------------------------------------+
   | Band               | Hysteresis: how far back the value must go before    |
   |                    | the rule lets go. For = and != it is the tolerance   |
   +--------------------+------------------------------------------------------+
   | Delay              | 0, 1, 2, 5, 10, 30, 60 or 300 s that the condition   |
   |                    | must hold before the rule acts                       |
   +--------------------+------------------------------------------------------+
   | THEN               | Set device; Set all alike (every device of the same  |
   |                    | type on the network); Recall scene; Raise alarm      |
   +--------------------+------------------------------------------------------+
   | Target and setting | The device, and one of 8 settings; only settings the |
   |                    | device accepts are offered                           |
   +--------------------+------------------------------------------------------+
   | To                 | A fixed number; the IF reading times a factor; or    |
   |                    | another device's value times a factor                |
   +--------------------+------------------------------------------------------+
   | ELSE               | Set the target back to a value when the condition    |
   |                    | ends, or leave it as it is                           |
   +--------------------+------------------------------------------------------+

5.15.4 How rules behave
-----------------------

.. index::
   single: How rules behave

Rules are designed to be quiet neighbours. They act on change rather than rewriting their target every tick, and they check that their change actually stuck.

- **They act on change.** A rule fires when its condition becomes true, and again, through its ELSE, when the condition becomes false.
- **Live values follow.** When To takes the IF reading or another device's value, the rule keeps rewriting the target for as long as it is active, whenever that value changes.
- **They check their work.** After a write, the rule reads the target back three times, 2 s apart, and writes again if something has changed it back. A write that fails is retried every half second.
- **Recall scene** uses the number in To as the scene number, 1–8 (see :ref:`5.16 Scenes <os-scenes>`).
- **Raise alarm** logs an error and sounds the rack's alarm for as long as the rule is active, and :ref:`5.14 Dashboard <os-dashboard>` lists it.

.. admonition:: CAUTION
   :class: warning

   "Set all alike" acts on every device of the same type on the rack's data network, including devices in rooms you may not be thinking about. Check the target type before you switch such a rule on.

.. _sec-5-15-5:

5.15.5 Creating a rule
----------------------

.. index::
   single: Creating a rule

This example keeps a room above 90 kPa with an active vent, which is also the example the empty Rules screen suggests.

**Requirements:** The room's gas sensor and the active vent must both be on the rack's data network.

1. Press **F2** to add a new rule.
2. Set IF device to the room's gas sensor, Value to Pressure, Compare to <, Limit to 90, Band to 5 and Delay to 2 s.
3. Set THEN to "Set device", the target to the active vent, the setting to On and To to 1.
4. Set ELSE to set the vent back to 0.
5. Press **F1** to switch the rule on.

**Result:** The vent starts when the room's pressure has been below 90 kPa for 2 s, and stops again once it is back above 95 kPa.
