# 🌏 Myanmar Seismic & Active Fault Viewer (Mar 28, 2025 – Present)

An interactive, single-file web GIS application that visualizes real-time earthquake data from the **USGS Earthquake Catalog** (starting from March 28, 2025, to the present date) alongside active tectonic fault lines from the **GEM Global Active Faults Database** across Myanmar.

Designed to run natively on **GitHub Pages** with zero build steps, backend servers, or API keys required.

🔗 **Live Map:** `https://<your-github-username>.github.io/<your-repo-name>/` *(Update with your GitHub Pages URL)*

---

## ✨ Key Features

* **Real-Time USGS Seismic Feed:** Dynamically queries the USGS FDSN Event Web Service API for all seismic events recorded from `2025-03-28T00:00:00 UTC` up to the exact moment the page is loaded.
* **GEM Active Faults Integration:** Fetches and clips the harmonized GEM Global Active Faults dataset to Myanmar's tectonic region, highlighting major structures such as the **Sagaing Fault**, **Sunda Megathrust**, and regional strike-slip/thrust systems.
* **One-Click GeoJSON Exporter:** Allows users and researchers to directly download the filtered datasets (`myanmar_earthquakes_20250328_present.geojson` and `myanmar_gem_active_faults.geojson`) as valid, standards-compliant GeoJSON files for use in QGIS, ArcGIS, or Python.
* **Strict vs. Bounding-Box Filtering:** Toggle between a strict country filter (matching `"Myanmar"` or `"Burma"` in the USGS location description) or a broader regional bounding box (`9.5°N–28.6°N`, `92.1°E–101.2°E`).
* **100% Keyless Basemaps:** Includes four free, no-API-key-required basemap layers:
  * **Dark Basemap (OSM):** Custom CSS-inverted OpenStreetMap tiles for high-contrast data visualization.
  * **Satellite Imagery:** Esri World Imagery.
  * **Topographic:** Esri World Topographic Map.
  * **Terrain:** OpenTopoMap.
* **Offline / Local File Support:** Includes a local file loader to drag-and-drop or browse pre-exported `.geojson` files if working offline.

---

## 📂 Repository Structure

```text
├── index.html                           # Complete single-file web map application (HTML/CSS/JS)
├── README.md                            # Project documentation
├── download_datasets.py                 # (Optional) Python script for CLI GeoJSON extraction
├── myanmar_earthquakes.geojson          # (Optional) Pre-exported USGS earthquake catalog
└── myanmar_active_faults.geojson        # (Optional) Pre-exported GEM active faults dataset
```

---

## 🚀 Deploying to GitHub Pages

Because the main application is named `index.html` and uses client-side HTTPS API requests, deploying to GitHub Pages takes less than a minute:

1. Create a new GitHub repository (or use an existing one) and push `index.html` and `README.md` to the `main` branch:
   ```bash
   git init
   git add index.html README.md
   git commit -m "Initial commit: Myanmar Seismic & Active Fault Viewer"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-repo-name>.git
   git push -u origin main
   ```
2. Open your repository on GitHub and click on **Settings** (top navigation bar).
3. In the left sidebar, click **Pages**.
4. Under **Build and deployment** → **Source**, select **Deploy from a branch**.
5. Under **Branch**, select `main` and `/ (root)`, then click **Save**.
6. Wait 1–2 minutes and refresh the page. Your live map will be published at:
   `https://<your-username>.github.io/<your-repo-name>/`

---

## 🗺️ Map Symbology & Legend

### 1. Earthquakes (USGS)
* **Circle Size:** Scaled exponentially by earthquake **Magnitude ($M$)** so major events and mainshocks stand out clearly against aftershock sequences.
* **Circle Color (Hypocentral Depth):**
  * 🔴 **Red:** Shallow (`< 30 km`)
  * 🟠 **Orange:** Intermediate (`30 – 70 km`)
  * 🟡 **Yellow:** Deep (`> 70 km`)

### 2. Active Faults (GEM GAF-DB)
* **Line Color (Fault Kinematics / Slip Type):**
  * 🩷 **Magenta (`#ff2a85`):** Strike-Slip (*Dextral / Sinistral / Strike-Slip*) — e.g., Sagaing Fault (rendered with increased line weight).
  * 🩵 **Cyan (`#00e5ff`):** Reverse / Thrust / Subduction.
  * 💚 **Lime Green (`#a3e635`):** Normal / Transtensional.
  * 🤍 **Light Slate (`#cbd5e1`):** Other / Unspecified kinematics.

---

## 📊 Data Sources & APIs

### 1. USGS Earthquake Hazards Program (FDSNWS Event API)
* **Endpoint:** `https://earthquake.usgs.gov/fdsnws/event/1/query`
* **Parameters Used:**
  * `format=geojson`
  * `starttime=2025-03-28T00:00:00`
  * `endtime=<Current UTC Timestamp>`
  * `minlatitude=9.5`, `maxlatitude=28.6`
  * `minlongitude=92.1`, `maxlongitude=101.2`
  * `limit=20000`

### 2. GEM Global Active Faults Database (GAF-DB)
* **Repository:** [GEMScienceTools/gem-global-active-faults](https://github.com/GEMScienceTools/gem-global-active-faults)
* **Data URL:** `gem_active_faults_harmonized.geojson`
* **Filtering Logic:** Retains all fault traces belonging to the Myanmar regional catalog (`catalog_name` containing `"myanmar"`) or intersecting the Myanmar geographic bounding box.

---

## 💻 Local Development & Usage

No build tools or `npm` packages are needed. To run locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Double-click `index.html` to open it directly in any modern browser, or serve it over localhost using Python:
   ```bash
   python -m http.server 8000
   ```
3. Visit `http://localhost:8000` in your browser.

---

## 📚 Citations & Acknowledgments

If you use the exported GeoJSON datasets or visualizations in academic or technical reports, please credit the upstream data providers:

* **Earthquake Data:** U.S. Geological Survey (USGS) Earthquake Hazards Program, *ANSS Comprehensive Earthquake Catalog (ComCat)*. Accessed via the USGS API.
* **Active Faults Data:** Styron, R., and Pagani, M. (2020). *The GEM Global Active Faults Database*. Earthquake Spectra, 36(1_suppl), 160–180. https://doi.org/10.1177/8755293020944182
* **Mapping Library:** [Leaflet.js](https://leafletjs.com/) & [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE). Underlying seismic and fault datasets are subject to the respective public domain (USGS) and Creative Commons (CC BY-SA 4.0, GEM Foundation) licenses.