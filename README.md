
---
# 📝 Smart Note Taking App
## 🚀 Features

- **Text and Voice Note Input**  
  Create notes by typing or speaking, with real-time speech-to-text functionality.

- **ToDo Management**  
  Track your tasks for today and the future with completion status and category tagging.

- **Achievements & Gamification**  
  Earn points for completing tasks and notes. Unlock productivity levels like 🎯 Goal Getter, 📈 Productivity Master, and 🌟 Note-Taking Pro.

- **Categorization & Color Coding**  
  Organize notes and todos into categories like Work, Personal, Ideas, and Urgent with intuitive color labels.

- **Data Export**  
  Export your notes and todos as CSV files for backup or further use.

- **Voice Recognition Support**  
  Add todos for "tomorrow" using a special voice command like:
  > *"Buy groceries for tomorrow"*

- **Persistent Storage**  
  All your notes, todos, and points are stored in a local JSON file under the `data/` directory.

- **Custom UI Styling**  
  Elegant custom CSS and JS animations for an improved user experience.

---

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/your-username/smart-note-taking-app.git
cd smart-note-taking-app
````

### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Required Packages

If `requirements.txt` is not provided, install manually:

```bash
pip install streamlit speechrecognition pandas
```

> **Note**: For voice recognition, `pyaudio` is required. You can install it with:

```bash
pip install pyaudio
```

On some systems, you might need to install portaudio with a package manager like `brew` (macOS) or `apt` (Linux) before installing `pyaudio`.

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🎤 Using Voice Notes

* Click the **🎤 Start Voice Recording** button.
* Speak your note or todo clearly.
* Say “for tomorrow” to automatically add it as a future task.

---

## 🗂 Project Structure

```
├── app.py                 # Main Streamlit app
├── data/
│   └── app_data.json      # Saved notes, todos, and points
├── README.md
└── requirements.txt       # Python dependencies
```

---

## 📦 Export & Backup

Export your notes and todos via the sidebar into CSV files:

* `notes.csv`
* `todos.csv`

---

## 💡 Future Features (Coming Soon)

* Tag support
* Priority levels
* Cloud sync
* Mobile layout improvements

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* [Streamlit](https://streamlit.io/)
* [Google Speech Recognition API](https://pypi.org/project/SpeechRecognition/)
* [UI Avatars](https://ui-avatars.com/)

---

## ✨ Demo

*Coming soon: Deployed version or GIF showcasing app usage.*

```
