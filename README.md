# CS2 Demo Reader

## Extract player IDs to listen to comms

Use the following command:
```
python list-players.py .\sample-data\demo.dem
```
.. or with the binary:
```
list-players.exe .\sample-data\demo.dem
```

This will extract player IDs in demos and calculates a bitmap.

The result looks like:
```
CT players:
[(5, 'Samura1i', 'ct'), (11, 'theawaker', 'ct'), (3, 'CiRO53', 'ct'), (10, 'TriSchnitt', 'ct'), (4, 'Qud13', 'ct')]

T players:
[(6, 'nikha69', 't'), (12, 'Tniv', 't'), (9, 'tyto', 't'), (8, 'UauUauu', 't'), (7, 'liluzifan-', 't')]

CT bitmap: 0b110000111000
tv_listen_voice_indices_h 3128
tv_listen_voice_indices 3128
```

Paste the two last lines into the CS2 developer console after opening the demo via `playdemo`. This will enable the voice comms for the respective team.

## Prebuilds

Find single file prebuild binaries to use in [dist](./dist).
They are large, but do not require python or any knowledge.

You can also build a binary yourself. See next section.


## Build

Build the app yourself by
1. Installing python
2. Install dependencies using `pip install`
3. Build via `pyinstaller --onefile list-players.py`

This will results in an exe file in the dist folder.

