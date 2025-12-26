from pydantic import BaseModel

class WifiScan(BaseModel):
    scan_id: str
    node_id: str
    timestamp: int
    zone_id: str
    ssid: str
    bssid: str
    rssi_dbm: int
    channel: int
    band: int
    auth_mode: str
    hidden: bool
