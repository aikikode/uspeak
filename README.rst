USpeak - control PC with your voice
===================================

Linux software to perform different operations using voice control:

- open websites
- search google
- control music and video playbak: pause, mute, etc.
- type text

Requirements
------------
Install the following packages if you want to have the corresonding functionality:

- python3 *(must-have, usually already present)*
- xautomation *(to control media and type text with your voice)*
- python3-espeak *(to receive computer voice notifications)*

Installation
------------
No installation is required. Just download uspeak and it's ready.

Usage
-----
Get to program directory and run

.. code:: bash

  ./uspeak -h

to get the list of supported parameters. By now the following languages are supported for commands:

- en (English)
- ru (Russian)

Usually you'll want to run the tool two ways:

1. **Execute single voice command and exit**

   .. code:: bash

     ./uspeak.py --lang=en

   Useful to set system hotkey for this command. You'll have a couple of second to start speaking otherwise it will exit.

2. **Wait for loud sound to trigger the voice input**

   .. code:: bash

     ./uspeak.py --lang=en --continuous

   Almost the same, but the tool will run continuously and be triggered each time you produce some load noise: say something, clap your hands, tap the mic, etc. After that it will wait a couple of seconds for your command, execute it and continue waiting for next trigger event.
   
   You'd better setup your microphone volume to comfortable level then. If the tool is triggered too often, decrease the volume. And vice a versa.

About
-----
- Based on `LiSpeak <https://github.com/BmanDesignsCanada/LiSpeak>`__