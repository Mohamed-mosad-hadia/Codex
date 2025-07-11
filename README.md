# 🎓 Codex – Student Tracking System for Educational Centers

**Codex** is a web-based student management and tracking system developed using **Django**. It’s designed for educational centers to monitor student progress, attendance, payments, and academic performance through a clean and user-friendly interface.

## 🔧 Features

### 🔐 Admin Panel (for Assistants)
- Add and manage student profiles (name, phone number, group)
- Record attendance and absence per session
- Track monthly payment status (with month labeling)
- Log student exam grades
- Filter and search students by phone number, group, or payment status
- Simple and intuitive interface for non-technical users

### 🧑‍🎓 Student Dashboard (Frontend)
- RTL Arabic design tailored for high school students
- View attendance and absence history
- Check payment status
- View exam grades
- Dark mode toggle
- Responsive layout with clean UI and engaging visuals

## 💻 Tech Stack
- **Backend**: Django
- **Frontend**: HTML5, CSS3, Django Template Language (DTL)
- **Database**: SQLite (can be switched to PostgreSQL or MySQL)
- **Other Tools**: Git, GitHub

## 🚀 Future Enhancements
- SMS/email notifications for absences or due payments
- Parent login with limited access
- Export reports as PDF
- Multi-language support

## 🧩 Installation
```bash
git clone https://github.com/Mohamed-mosad-hadia/Codex.git
cd Codex
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
