


PAGER_VERSIONS = [
    "1.0.6-stable",
    "1.0.4-stable",
    "1.0.3-stable",
    "1.0.2-stable",
    "1.0.1-stable",
    "1.0.0-stable",
]


VOLUME_MUTE = "mute"
VOLUME_LOW = "low"
VOLUME_MEDIUM = "medium"
VOLUME_HIGH = "high"

BATTERY_DISCHARGING = "discharging"
BATTERY_CHARGING = "charging"
BATTERY_CHARGING_25 = "charging_25"
BATTERY_CHARGING_50 = "charging_50"
BATTERY_CHARGING_75 = "charging_75"
BATTERY_CHARGING_100 = "charging_100"
BATTERY_CHARGED = "charged"

pager_time = 0

class Pager:
    def __init__(self, firmware: str):
        self.firmware = firmware
        self.volume = VOLUME_HIGH
        self.battery_status = BATTERY_DISCHARGING
        self.battery_percentage = 100
        self.selection_index = (0,0)
        self.selection_history = []
        self.current_menu = None