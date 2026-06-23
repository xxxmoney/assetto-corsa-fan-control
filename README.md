
# Assetto Corsa Fan Control

## What this does
- In game car speed controls your real-life fan 𖣘
- As of now, Xiaomi Smart Fans are supported

## Disclaimer OS
- Currently *Windows* is supported

## Prerequisities
- Python - preferably version 3.12
- Cloning this repo

## What's in here
- There are two main parts
  - Assetto Corsa plugin (reads speed from game)
  - A python script (sets speed to fan)

## Setup for `Plugin`
- Copy the whole folder `wind_speed` from `/addon` to your Assetto Corsa apps path
  - May be something like this:
    - `C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\apps\python\wind_speed`
- Make sure the path is correct in the `wind_speed\wind_speed.py` file:
  - `assetto_path = Path("C:/Program Files (x86)/Steam/steamapps/common/assettocorsa")`

## Setup for `App`
- Get host address and token
  - Use this [Token Extractor](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor)
- Rename `config.example.toml` -> `config.toml`
  - Set the values - the ones you got from the Token Extractor
    - host is ip address (something like `192.168.1.5`) of the device
    - token is token (like `6666u9q32df4fe84383f362a44cd678b`) >]

## Setup final
- After you have done the setup for `Plugin` and `App`, you can do these steps:
  - Open terminal and run these two commands (make sure you are in the correct directory)
    - `poetry install`
    - `poetry run dev`
  - The app will now run in background (it should periodically write stuff in console)

## Testing 
  - I advise testing before starting the game
  - Change the value of this file
    - `"C:\Users\%username%\AppData\Roaming\AssettoCorsaFanControl\speed.json"`
      - If the file does not exist, just create it and put this value in:
        - `{"percentage": 0}`
        - You can now play with the value, like setting `{"percentage": 50}`, `{"percentage": 80}`, etc
        - After setting the value and saving, it should change the fan speed
  - If the above works correctly, you can start the game >]
  