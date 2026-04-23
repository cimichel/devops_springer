
# 🚀 Running the DevOps Springer API

## 🧱 Prerequisites

* Python 3.11+
* Virtual environment (`.venv`) activated

---

## 📦 Install dependencies

```bash
python3 -m pip install fastapi uvicorn
```

---

## ▶️ Run the API

From the project root:

```bash
python3 -m uvicorn api:app --reload
```

---

## 🌐 Access the API

Open in your browser:

```
http://127.0.0.1:8000/docs
```

This will show the interactive Swagger UI where you can test endpoints.

---

## 🧪 Example Endpoints

### Get a Jerry quote

```
GET /jerry
```

### Get audience reaction

```
GET /audience
```

---

## 🛑 Stop the server

To stop the API, press:

```
Ctrl + C
```

---

## 💡 Notes

* If you see `command not found: python`, try using `python3`
* Make sure your virtual environment is active:

  ```bash
  source .venv/bin/activate
  ```
* If dependencies are missing, reinstall using pip

---
<img width="2860" height="1330" alt="96EB46F2-05CC-43FE-8564-E458A326B362" src="https://github.com/user-attachments/assets/4a3b5c21-e1dc-4f13-9cdb-580e04daee10" />

<img width="1608" height="936" alt="CC9E553C-EEC0-4958-BB89-20A687148062" src="https://github.com/user-attachments/assets/db28707e-2116-4114-9074-5a06158364af" />

<img width="1576" height="922" alt="B0D1F9B3-CE83-4CBB-99E9-C4BBA625838D" src="https://github.com/user-attachments/assets/ec7def0d-0ca2-4158-8c07-8e589721fe58" />


## 🎭 Why this exists

This project simulates DevOps workflows using a narrative-driven approach inspired by Jerry Springer show (because production failures are basically reality TV).

![Jerry Chaos](https://media1.tenor.com/m/-is6u2LpO4QAAAAC/jerry-springer.gif)

