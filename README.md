# 👨‍🎓 Face Recognition and Advanced Attendance System

![Main Window Screenshot](https://github.com/Rishikesh1411/Face-Recognition-and-Advanced-attendance-System/raw/main/college_images/PIC/main_window.png)

An intelligent attendance system using facial recognition technology to automate and streamline the attendance process for educational institutions.

## ✨ Features

- **Facial Recognition** - Accurate face detection and identification
- **Real-time Attendance** - Automatic marking of attendance
- **User Management** - Add/remove students and faculty
- **Data Export** - Generate attendance reports in multiple formats
- **Multi-platform Support** - Works on Windows and Linux

## 🛠️ Technologies Used

- OpenCV (for face detection and recognition)
- Python (backend logic)
- Tkinter (GUI interface)
- SQLite (database management)
- NumPy (numerical computations)

## 📸 Sample Images

| Developer Photo | Sample Detection |
|-----------------|------------------|
| <img src="https://github.com/Rishikesh1411/Face-Recognition-and-Advanced-attendance-System/raw/main/college_images/rishikesh.jpg" width="200"> | <img src="https://github.com/Rishikesh1411/Face-Recognition-and-Advanced-attendance-System/raw/main/college_images/PIC/detection_sample.png" width="200"> |

## 🚀 Getting Started

### Prerequisites
- Python 3.6+
- OpenCV
- Tkinter
- NumPy

### Installation
```bash
git clone https://github.com/Rishikesh1411/Face-Recognition-and-Advanced-attendance-System.git
cd Face-Recognition-and-Advanced-attendance-System
pip install -r requirements.txt
python main.py

graph TD
    A[Camera Input] --> B[Face Detection]
    B --> C[Face Recognition]
    C --> D[Database Match]
    D --> E[Attendance Marking]
    E --> F[Report Generation]

