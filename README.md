# 📂 File Organizer using Python

A simple and efficient desktop application built with **Python** and **Tkinter** that automatically organizes files into categorized folders based on their file extensions.

This project was developed as part of my **Python Development Internship** at **Upskill Campus** in collaboration with **UniConverge Technologies Pvt. Ltd. (UCT)**.

## 📌 Features

- 📁 Browse and select any folder
- 🗂️ Automatically organize files by category
- 📄 Supports multiple file types
- 📂 Creates folders automatically if they don't exist
- 🔄 Handles duplicate filenames safely
- 📝 Generates activity logs (`organizer.log`)
- 📊 Displays an organization summary after completion
- 🖥️ User-friendly GUI built with Tkinter

## 🗃️ File Categories

| Category | Supported Extensions |
|----------|----------------------|
| Documents | .pdf, .doc, .docx, .txt, .ppt, .pptx, .xls, .xlsx, .csv |
| Images | .jpg, .jpeg, .png, .gif, .bmp, .webp, .svg |
| Videos | .mp4, .avi, .mkv, .mov, .wmv, .flv |
| Audio | .mp3, .wav, .aac, .ogg, .flac |
| Archives | .zip, .rar, .7z, .tar, .gz |
| Programs | .exe, .msi, .apk, .bat, .py |
| Others | Any unsupported file type |

## 🛠️ Technologies Used

- Python 3
- Tkinter
- os
- shutil
- pathlib
- logging

## 📁 Project Structure

FileOrganizer/
│
├── main.py
├── organizer.py
├── file_types.py
├── logger.py
├── organizer.log
├── requirements.txt
├── README.md
└── screenshots/

## 💻 How It Works

1. Launch the application.
2. Click **Browse Folder**.
3. Select the folder you want to organize.
4. Click **Organize Files**.
5. The application:
   - Detects each file's extension.
   - Creates category folders if required.
   - Moves files into their respective folders.
   - Handles duplicate filenames automatically.
   - Displays a summary of organized files.
   - Records all actions in `organizer.log`.

## 📸 Screenshots

### Main Window
![Main Window](screenshots/main_window.png)

### Before Organizing
![Before Organizing](screenshots/efore_organizing.png)

### After Organizing
![After Organizing](screenshots/after_organizing.png)

### Organization Summary
![Summary](screenshots/summary_popup.png)

## 📝 Log File

The application creates an `organizer.log` file containing information about:

- Folder selected
- Files moved
- Destination folders
- Total files organized

## 🎯 Future Improvements

- Dark Mode
- Drag and Drop Support
- Progress Bar
- Undo Last Organization
- File Preview
- Duplicate File Detection using Hashing
- File Search
- Export Summary Report (PDF)

## 👨‍💻 Author

**Aadarsh Kumar**

Bachelor of Computer Applications (BCA)

Amity University Jharkhand

---

## 📄 License

This project was developed for educational and internship purposes.