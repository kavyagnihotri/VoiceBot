# RaspberryPi Voicebot Python Implementation
This directly contains the python implementation of backend flow of a basic voicebot which has support of 11 Indian Languages. All of this is mentioned in the [report](../voicebot-report.pdf).

### Files
#### `requirements.txt`
It contains all the dependencies required to run the program on PC or desktop.

#### `main.py`
Use `main.py` to run the program.

#### `keys.py`
Fill the file `keys.py` and add the required API keys, endpoints, regions, etc from your Azure AI services.

#### `constants.py`
This file contains the constants used in the program

#### `helper.py`
Contains the helper function of Test-to-Speech, Speech-to-Text, Translation, Audio-Playing and some basic functions.

#### `clu_model.py`
Contains the  Topic-Prediction functions.

#### Known Limitations
- The free version of Azure Translation AI Service has a limit of 2 million chars per month. 
- The current architecture is incompatible with RaspberryPi as the azure.cognitiveservices.speech library is not available for Raspian OS.


