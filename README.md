# Overview

ai agents using python sdk

# step 1: clone github repo and copy env example file

`git clone https://github.com/videosdk-community/ai-agent.git && cd ai-agent && cp .env.example .env`

- change environment variable

# step 2: install python version >= 3.11.2 and modules

`python3.11 -m pip install -r requirements.txt`
or
`python3 -m pip install requirements.txt`

- add flag `break-system-packages` if required.

# step 3: run the project

`python3.11 main.py`

# Additional

- change variable `system_prompt` as per requirements in file [intelligence_client.py](./intelligence/intelligence_client.py)
- change vad or utterance constants as per requirements in file [deepgram_stt.py](./stt/deepgram_stt.py)
