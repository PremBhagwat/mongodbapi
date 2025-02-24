# FastAPI Blog API

A **FastAPI-powered** Blog API with MongoDB for handling blog posts and comments.  



---

## Features
- **Create, Read, Update, Delete (CRUD) operations** for blog posts and comments  
- **FastAPI with Pydantic Validation**  
- **Async Database Operations with Motor**  
---

## Setup & Installation

### **1. First, install all required packages using **`uv`** (or `pip` if preferred):**

```sh
uv pip install -r requirements.txt
```

### **2. Using Local MongoDB**
- Install MongoDB Community Server 
- Start MongoDB:
```sh
mongod --dbpath C:\data\db
```
- Use the local MongoDB URI in db.py:
```sh
MONGO_URI = "mongodb://localhost:27017"
```



### **3. Run the FastAPI Server**
```sh
uvicorn main:app --reload
```
The API will be available at:  
🔹 **http://127.0.0.1:8000**

### **4. Running Tests**
- Run the Pytest tests to verify functionality:
```sh
pytest tests -v
```  
##  API Documentation
FastAPI automatically generates interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---



