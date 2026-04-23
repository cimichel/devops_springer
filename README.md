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

## 🎭 Why this exists

This project simulates DevOps workflows using a narrative-driven approach inspired by chaotic talk shows — because production failures are basically live TV.
