# Student Grade Manager

A simple browser app built with Streamlit. Add students and marks, view their grades, and see the class average, highest mark, and lowest mark.

## Requirements

- Python
- Streamlit

## Install Streamlit

Open PowerShell in the folder containing the app and run:

```powershell
py -m pip install streamlit
```

## Run the app

If the Python file is named `grade_app.py`, run:

```powershell
py -m streamlit run .\grade_app.py
```

If your file is named `gradeapp.py`, run:

```powershell
py -m streamlit run .\gradeapp.py
```

## Features

- Stores students in `st.session_state` so they remain during Streamlit reruns
- Accepts marks from 0 to 100
- Shows each student's name, mark, and grade
- Displays the class average, highest mark, and lowest mark
- Uses a styled HTML table for results

## Grade scale

- A: 90–100
- B: 80–89
- C: 70–79
- D: 60–69
- F: below 60
