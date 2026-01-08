# Project Setup & Dataset Instructions

## Overview
This project is designed to run on **Google Colab**, where datasets are uploaded directly to the Colab environment.  
You may also optionally load datasets from **Google Drive**.

---

## Dataset Setup

### Option 1: Upload Datasets Directly to Google Colab (Recommended)
1. Place all datasets inside a single folder of your choice (e.g., `datasets/`).
2. Upload this folder to the Google Colab session.
3. Update the dataset paths in the project files to match the folder location.

Example:
```python
path = "/content/datasets/"
```

### Option 2: Load Datasets from Google Drive

1. Upload the datasets to your Google Drive.
2. Run the script below to mount Google Drive:
```
    gdrive_connection.py
```
3. Once connected, update the dataset paths to point to the correct file location.

### Example
```python
    path = "/content/drive/MyDrive/datasets/"
```

---

## Important Notes

- Ensure all dataset paths are correct and consistent across files.
- Incorrect paths will result in file not found / path errors.
- Google Colab resets its environment after each session, so re-upload or re-mount datasets when restarting.

---

## Requirements

- Google Colab  
- Python 3.x  
- Google Drive (optional)

---

## Troubleshooting

- **Path Error:** Verify folder names and directory structure.
- **Drive Not Found:** Make sure Google Drive is mounted successfully.
- **Missing Files:** Re-upload datasets if the Colab session was restarted.

