# Email Classification API

This project provides an API to automatically classify support emails and mask sensitive information (PII).

---

## Setup

1. Install Python 3.8 or newer  
   https://www.python.org/downloads/

2. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/email-classification.git
   cd email-classification
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_md
   ```

---

## Usage

1. Start the API server:

   ```bash
   python app.py
   ```

2. Open Postman and send a POST request to:

   ```
   http://localhost:8000/classify
   ```

   With this JSON body:

   ```json
   {
     "email_body": "Hello, my name is John Doe, and my email is johndoe@example.com."
   }
   ```

3. Expected response:

   ```json
   {
     "masked_email": "Hello, my name is [name], and my email is [email_address].",
     "category": "General Inquiry"
   }
   ```

4. You can also access the interactive documentation at:
   ```
   http://localhost:8000/docs
   ```

---

## Features

- Detects and masks sensitive information: names, phone numbers, emails, credit cards
- Classifies emails into predefined categories (e.g., General Inquiry, Complaint, etc.)
- Interactive API documentation via FastAPI

---

## Project Structure

```
app.py           # Main application
api.py           # API endpoints and routes
models.py        # Email classification logic
utils.py         # PII masking and utilities
requirements.txt # Python dependencies
README.md        # Project instructions
```

---

## Production

To run the server with a production setup:

```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```
# email-classification-system
# email-classification-system
# email-classification-system
# email-classification-system
