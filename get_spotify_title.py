import os
import sys
import time
import json
import ctypes
from pathlib import Path
from typing import Tuple
import win32gui

def get_spotify_window_title() -> str:
    titles = []

    def foreach_window(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            class_name = win32gui.GetClassName(hwnd)
            if class_name == "Chrome_WidgetWin_0":
                title = win32gui.GetWindowText(hwnd)
                if " - " in title:
                    titles.append(title)
        return True

    win32gui.EnumWindows(foreach_window, None)

    if titles:
        return titles[0].strip()

    return "No title found"

def get_current_song(title: str) -> Tuple[str, str]:
    artist, name = title.split(" - ", 1)
    return artist.strip(), name.strip()

def save_song_info(config, name, artist):
    data_path = Path(config["SavePath"])
    data_path.mkdir(parents=True, exist_ok=True)

    with open(data_path / "artist.txt", "w", encoding="utf-8") as f:
        f.write(artist)

    with open(data_path / "song.txt", "w", encoding="utf-8") as f:
        f.write(name)

    with open(data_path / "entire.txt", "w", encoding="utf-8") as f:
        f.write(f"{name} - {artist}")

    with open(data_path / "entire-descending.txt", "w", encoding="utf-8") as f:
        f.write(f"{artist} - {name}")

def load_config() -> dict:
    default_config = {
        "SavePath": "./data"
    }

    config_path = Path("./data/config.json")
    config_path.parent.mkdir(parents=True, exist_ok=True)

    if not config_path.exists():
        return default_config

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    return config

def save_config(config: dict):
    config_path = Path("./data/config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

