from app import app

@app.route('/')
def home():
    return "✅ CRM Flask App is running!"
