import json
from datetime import datetime, timezone
import requests

# Myanmar Geographic Bounding Box
BBOX = {
    "minlatitude": 9.5,
    "maxlatitude": 28.6,
    "minlongitude": 92.1,
    "maxlongitude": 101.2
}

def download_usgs_earthquakes():
    print("Downloading earthquake data from USGS Search Catalog...")
    present_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": "2025-03-28T00:00:00",
        "endtime": present_iso,
        **BBOX,
        "limit": 20000
    }
    
    response = requests.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()

    # Filter strictly for events occurring within Myanmar (or Burma in USGS place naming)
    myanmar_features = [
        f for f in data.get("features", [])
        if any(k in (f.get("properties", {}).get("place") or "").lower() for k in ("myanmar", "burma"))
    ]

    geojson_out = {
        "type": "FeatureCollection",
        "metadata": data.get("metadata", {}),
        "features": myanmar_features
    }

    with open("myanmar_earthquakes.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson_out, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(myanmar_features)} earthquake events to 'myanmar_earthquakes.geojson'.")

def intersects_bbox(geometry):
    if not geometry or "coordinates" not in geometry:
        return False
    coords = geometry["coordinates"]
    gtype = geometry["type"]
    
    def in_box(pt):
        return (BBOX["minlongitude"] <= pt[0] <= BBOX["maxlongitude"] and
                BBOX["minlatitude"] <= pt[1] <= BBOX["maxlatitude"])

    if gtype == "LineString":
        return any(in_box(pt) for pt in coords)
    elif gtype == "MultiLineString":
        return any(any(in_box(pt) for pt in line) for line in coords)
    return False

def download_gem_faults():
    print("Downloading GEM Global Active Faults Database from GitHub...")
    gem_url = "https://raw.githubusercontent.com/GEMScienceTools/gem-global-active-faults/master/geojson/gem_active_faults_harmonized.geojson"
    response = requests.get(gem_url, timeout=120)
    response.raise_for_status()
    data = response.json()

    myanmar_faults = [
        f for f in data.get("features", [])
        if "myanmar" in (f.get("properties", {}).get("catalog_name") or "").lower()
        or intersects_bbox(f.get("geometry"))
    ]

    geojson_out = {
        "type": "FeatureCollection",
        "name": "myanmar_gem_active_faults",
        "features": myanmar_faults
    }

    with open("myanmar_active_faults.geojson", "w", encoding="utf-8") as f:
        json.dump(geojson_out, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(myanmar_faults)} active fault traces to 'myanmar_active_faults.geojson'.")

if __name__ == "__main__":
    download_usgs_earthquakes()
    download_gem_faults()