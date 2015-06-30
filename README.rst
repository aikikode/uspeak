USpeak - control PC with your voice
===================================

Linux software to perform different operations using voice control:

- open folders and websites
- search google
- control music and video playback: pause, mute, etc.
- type text

Requirements
------------
Install the following packages if you want to have the corresponding functionality:

- python3 *(must-have, usually already present)*
- python3-pyaudio *(also must-have)*
- xautomation *(to control media and type text with your voice)*
- python3-espeak *(to receive computer voice notifications)*

To install all requirements on Ubuntu:

.. code:: bash

  sudo apt-get install xautomation python3 python3-pyaudio python3-espeak

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

Available commands (en)
-----------------------

Folders
#######

Open ~/Documents: 'open documents'

Open ~/Downloads: 'open downloads'

Open ~/Dropbox: 'open dropbox'

Open ~/Music: 'open music'

Open ~/Videos: 'open videos'

Browser
#######
Open website: 'open' or 'go (to)' <site address or site name>, e.g. 'open youtube'

Search Google: 'search' or 'google' <text to search> or just ask any question

Media
#####
Insrease volume: 'louder' or 'volume up'

Decrease volume: 'volume down'

Mute all sounds: 'mute'

Unmute all sounds: 'unmute'

Play next song/video in queue: 'next'

Play previous song/video in queue: 'latest' or 'previous'

Pause/unpause: 'pause' or 'play'

Text
####
Type text: 'type' <text>

Other
#####
For complete list of commands and their variations look at dictionary files, e.g. for English: `dictionary/data/main_en.dic <https://github.com/aikikode/uspeak/blob/develop/dictionary/data/main_en.dic>`__ (you should be familiar with regular expressions)

Other Languages
###############
For help on commands in Russian run:

.. code:: bash

  ./uspeak.py --lang=ru --list-commands

About
-----
- Based on `LiSpeak <https://github.com/BmanDesignsCanada/LiSpeak>`__

