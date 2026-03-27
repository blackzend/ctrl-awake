from pathlib import Path
import json
import sys

APP_NAME = "ctrl-awake"

CONFIG_PATH = Path.home() / ".config" / f"{APP_NAME}" / "config.json"
DEFAULT_CONFIG = {
    "start_on_login": False,
    "auto_start_session": False,

    "default_session": {
        "duration": "infinite",  # o minutos
        "custom_minutes": 60
    },

    "system": {
        "mouse_enabled": True,
        "mouse_interval": 30,   # segundos
        "idle_before": 60       # segundos
    },

    "theme": {
        "name": "default",
        "show_elapsed": False
    }
}


def get_base_path():
    # Caso empaquetado (PyInstaller futuro)
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)

    # Caso instalado vía .deb (futuro)
    system_path = Path("/usr/share") / APP_NAME
    if system_path.exists():
        return system_path

    # Desarrollo
    return Path(__file__).resolve().parents[1]


def get_asset_path(*parts):
    return str(get_base_path().joinpath("assets", *parts))

def get_icon(theme: str, state: str) -> str:
    return get_asset_path("icons", theme, f"{state}.png")

def load_config():
    if not CONFIG_PATH.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

def save_config(config):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=4)