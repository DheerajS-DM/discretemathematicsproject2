# Bridge Structure Graph Extraction (Classical Image Processing Version)

## Overview

This program analyzes bridge structure diagrams to extract nodes (joints) and edges (bars) using **OpenCV, NumPy, NetworkX, and Matplotlib**—no deep learning required. It builds a graph from the detected structure and analyzes weak points and connectivity.

---

## Installation (Mac & Windows)

Open a terminal (Mac) or command prompt (Windows) in your project directory, then run:


> **Tkinter** is required for file explorer. Usually included with Python.
> - On Mac: Tkinter is installed by default.
> - On Ubuntu/Debian: `sudo apt-get install python3-tk`
> - On Windows: Already included if you used the official Python installer.

---

## File Structure

Place all these scripts in the same folder:

- `main.py`
- `select_file_dialog.py`
- `load_and_preprocess_image.py`
- `detect_nodes.py`
- `detect_edges.py`
- `detect_edge_lines.py`
- `rename_nodes.py`
- `match_lines_to_nodes.py`
- `build_graph_from_image.py`
- `analyze_graph_structure.py`

---

## How to Use

1. **Launch program**
2. **When prompted**, select your bridge diagram image (JPG, PNG, etc.) via the file explorer window.
3. **Wait for processing and results.** You will see:
    - Graph visualization with labeled nodes
    - Output listing graph connectivity and weak (critical) points

---

## Advanced Use and Troubleshooting

- **Node/edge detection not accurate?**  
  Open and edit `detect_nodes.py`:
    - Tune blur kernel sizes, contour area thresholds, or try alternate thresholding (see debug visualization in the function).
- **No file dialog appears?**  
  Install/repair `tkinter` as shown above.
- **Permission/File errors?**  
  Check folder permissions; try opening the terminal as an administrator.

---

## Quick Tips

- Works best on high contrast technical/scanned line drawings with clear dots/circles for joints.
- Output graph is interactively displayed with matplotlib.

---

## License

For academic or research use.  
Uses BSD/MIT-licensed open-source Python libraries.

---

## Authors

Inspired by community bridge structure detection projects and adapted for classical image processing without deep learning.

