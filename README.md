# gw2_TAB
Tool Asisted Benchmark for Guild Wars 2

#TODO
- support key combo (alt+1)
- support multiple keyboards (querty,azerty...)
- Correct the readme

# Setup 
- Download python 3.11 https://www.python.org/downloads/release/python-3113/
- Install virtual env ```pip install virtualenv```
- Create your venv ```python3 -m venv mynenv```
  - Activate your venv : Win(```.\mynenv\Scripts\activate```), Unix(```source monenv/bin/activate```)
  - download requirements ```pip install -r requirements.txt```

# How to Use

## Record
To record a rotation, use "record_keyboard_input.py" , start the script (console or IDE). To start recording press "Key.home"(Querty) or "Début"(Azerty). To stop the record, press "Escape".
Start and stop keybind can be edited at the beginning of the script 
```
key_start = 'Key.home'
key_stop = 'Key.esc'
```

A file "input_records.txt" will be generated, containing your keylogged rotation

# Run

To run a rotation with gw2_TAb, use "run_keyboard_input.py", start the script (console or IDE). To start press "Key.home"(Querty) or "Début"(Azerty). To stop the record, press "Escape".

For now it only support querty keyboards inputs, special keys can be edited and modified at the beginning of the file. Respecting "Pynput" format.

```
special_keys = {
    'Key.f1': Key.f1,
    'Key.f2': Key.f2,
    'Key.f3': Key.f3,
    'Key.f4': Key.f4,
    'Key.f5': Key.f5,
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7' : '7',
    '8' : '8',
    '9' : '9',
    '0' : '0',
}
```

## Rotation file format

```
('7', 0.088) 
5.0000
('7', 0.082)
.
.
.
```
```
('Key', press_time)
pause
('Key', press_time)
.
.
.
```

This file can be edited, numbers has to stay floats and Keys Querty keys (no special accent)

