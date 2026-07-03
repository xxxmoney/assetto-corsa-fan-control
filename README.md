
# Assetto Corsa Fan Control

## What this does
- Assetto Corsa car speed -> change fan 𖣘 speed irl
- Xiaomi Smart Fans supported

## Disclaimer OS
- Currently *Windows* supported

## Prerequisities (start here)
- Python - version 3.12
- Clone this repo
  - Choose some folder
  - Open terminal in said folder
  - `git clone https://github.com/xxxmoney/assetto-corsa-fan-control`
  - Open folder `assetto-corsa-fan-control`
  - Continue with [Setup for Plugin](#setup-for-plugin)

## What's in here
- There are two main parts
  - Assetto Corsa plugin (reads speed from game)
  - A python script (sets speed to fan)

## Setup for `Plugin`
- Copy whole folder `wind_speed` from `/addon` to Assetto Corsa ath
  - Something like this:
    - `C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\apps\python\wind_speed`
- Make sure path correct in the `wind_speed\wind_speed.py`:
  - `assetto_path = Path("C:/Program Files (x86)/Steam/steamapps/common/assettocorsa")`
- Continue with [Setup for App](#setup-for-app)

## Setup for `App`
- Get host address and token
  - Use this [Token Extractor](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor)
- Rename `config.example.toml` -> `config.toml`
  - Set values - from Token Extractor
    - host is ip address (something like `192.168.1.5`) of device
    - token is token (like `6666u9q32df4fe84383f362a44cd678b`) >]
- Continue with [Setup final](#setup-final)

## Setup final
- After steps [Setup for Plugin](#setup-for-plugin) and [Setup for App](#setup-for-app), do this
  - Open terminal run commands (make sure you in correct directory)
    - `poetry install`
    - `poetry run dev`
  - App will run in background (it should write stuff)
- Continue with [Testing](#testing)

## Testing
  - Change text in file:
    - `"C:\Users\%username%\AppData\Roaming\AssettoCorsaFanControl\speed.json"`
      - If file does not exist, create it
      - You can now play with it, like setting `{"percentage": 50}`, `{"percentage": 80}`, etc
  - After setting value, saving, should change fan speed
  - If above works correctly, you start game >]
  - If not, look at program output in terminal
  