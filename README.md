
# 🎓 UTel University - Computer Engineering Curriculum

**A Dynamic, Data-Driven Curriculum Engine**

This repository contains the source code for the UTel University Computer Engineering curriculum portal. It has been refactored from a static multi-page site into a dynamic engine driven by `data/curriculum.json`.

## 🚀 Deployment

This app is designed to be deployed on **Streamlit Cloud**.

### 1. New Deployment (Recommended)
Since this is a new repository structure, it is best to create a fresh deployment.

1. Go to [Streamlit Cloud](https://streamlit.io/cloud).
2. Click **"New app"**.
3. Select this repository: `yandri918/computer_enginer`.
4. **Main file path**: `Home_Dynamic.py` (This is crucial!).
5. Click **Deploy**.

### 2. Updating Existing Deployment
If you already have a deployment pointing to this folder (e.g., as a subdirectory of another repo), you need to change the entry point.

1. Go to your App Settings on Streamlit Cloud.
2. Change "Main file path" to `Home_Dynamic.py`.
3. Save.

## 📁 Project Structure

- `Home_Dynamic.py`: The main engine. Reads JSON and renders the UI.
- `data/curriculum.json`: The database of all courses, syllabi, and metadata.
- `simulations.py`: Python logic for interactive components (e.g., Calculus plots, Matrix calculators).
- `pages/`: (Optional) Legacy static files (can be archived).

## 🛠️ Maintenance

- **To add a course**: Simply add an entry to `data/curriculum.json`.
- **To update a syllabus**: Edit the text in `data/curriculum.json`.
- **To add a simulation**: 
    1. Write the function in `simulations.py`.
    2. Add the function to `SIMULATION_MAP` in `simulations.py`.
    3. Update the `id` in `data/curriculum.json` to match.
