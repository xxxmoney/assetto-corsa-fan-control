
# Assetto Corsa Fan Control

## What this does
- Simply - car speed in game controls your real-life fan 𖣘
- As of now Xiaomi Smart Fans are supported

## Disclaimer
- Currently only *Windows* supported

## Installation
- Clone this repo
- Run `poetry install`

## What's in here
- There are two main parts
  - Assetto Corsa plugin (reads speed from game)
  - A python script (sets speed to fan)

## Plugin in `/addon`
- Copy the whole folder `wind_speed` to your Assetto Corsa apps path
  - May be something like this:
    - `C:\Program Files (x86)\Steam\steamapps\common\assettocorsa\apps\python\wind_speed`
- Make sure the path is correct in the `wind_speed\wind_speed.py` file:
  - `assetto_path = Path("C:/Program Files (x86)/Steam/steamapps/common/assettocorsa")`

## App in `/src`
- Firstly, you need to get host address and token
  - Use this [Token Extractor](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor)
- Then rename or copy the `config.example.toml` -> `config.toml`
  - Set the values - the ones you got from the Token Extractor

## Setup
- If done setup for Plugin and App, you can do steps here:
  - Run `poetry run dev`
  - The app will now run in background
  - You can now start Assetto Corsa


