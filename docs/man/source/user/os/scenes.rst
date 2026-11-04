.. _os-scenes:

5.16 Scenes
===========

.. index::
   single: Scenes

Scenes are snapshots of the settings of every device on the data network, which you can put back with a single key. The rack holds eight of them. It is program 9 in the Automation group; open it with **HOME**, then **3**.

5.16.1 Screen
-------------


.. _figure-5-13:

.. figure:: /images/os-scenes.png
   :alt: Scenes listing eight empty scenes named Day, Night, Storm, Power save, Work shift, Away, Maintenance and Emergency
   :width: 100%

   **Figure 5-13** Eight empty scenes. Set the devices the way you want them, then **F1** stores the selected scene.

The list shows each scene's name and what it holds, and the Settings panel below describes the selected scene.

5.16.2 Keys
-----------


.. _table-5-19:

.. table:: **Table 5-19** Scenes keys

   +-------------------+----------------------------------------------------+
   | Key               | What it does                                       |
   +===================+====================================================+
   | **UP** / **DN**   | Select a scene                                     |
   +-------------------+----------------------------------------------------+
   | **F1**            | Stores the scene: takes a snapshot of the devices  |
   |                   | now                                                |
   +-------------------+----------------------------------------------------+
   | **F2**            | Recalls the scene: writes the stored settings back |
   +-------------------+----------------------------------------------------+
   | **F3** or **INC** | Gives the scene the next name; **DEC** goes back   |
   +-------------------+----------------------------------------------------+
   | **F4**            | Clears the scene                                   |
   +-------------------+----------------------------------------------------+
   | **F5**            | Makes the scene the start-up scene                 |
   +-------------------+----------------------------------------------------+

5.16.3 What a scene stores
--------------------------

.. index::
   single: What a scene stores

A scene stores only settings that a device can both report and accept. Sensors are therefore skipped, while doors, vents, lights and machines are kept. A recall writes only to devices that are still on the network.

Scenes 1–8 start out named Day, Night, Storm, Power save, Work shift, Away, Maintenance and Emergency. **F3** steps a scene's name through those and four more: Lockdown, Party, Custom A and Custom B.

.. admonition:: CAUTION
   :class: warning

   Recalling a scene writes to every device it stored, all over the base at once. Check what a scene holds before you recall it, especially one stored by someone else.

5.16.4 Storing and recalling a scene
------------------------------------

.. index::
   single: Storing and recalling a scene

**Requirements:** The devices must be on the rack's data network and set the way you want them.

1. Select a scene with **UP** and **DN**, and use **F3** to give it a name that will mean something to you later.
2. Press **F1** to store it.
3. To put the base back that way later, select the scene and press **F2**.

**Result:** The event log records how many settings were stored, and how many were written back on recall.

5.16.5 Recalling a scene without the keys
-----------------------------------------

.. index::
   single: Recalling a scene without the keys

Scenes can also be recalled automatically, in two ways.

- **At start-up:** The start-up scene, set with **F5**, is recalled 3 s after the rack starts.
- **From a rule:** A rule whose THEN is "Recall scene" recalls the scene whose number is in its To field (see :ref:`5.15 Rules <os-rules>`). A "Night" scene recalled when a daylight sensor drops is a classic first project.
