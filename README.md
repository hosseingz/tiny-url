

# 🌐 Tiny URL - A Django URL Shortener

Tiny URL is a simple URL shortener built using Django. It generates short, unique links for long URLs, making them easier to share and manage.

## ✨ Features

- 🔗 Shorten long URLs into custom short links.
- 🚀 Redirect to the original URL via the shortened link.
- 📅 Automatically store the date when a URL was created.
- 🔄 Fully functional API for creating and managing URLs.

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your machine:

- Python (3.8 or higher)
- Django (5.0 or higher)
- Django REST Framework (3.12 or higher)

### 📂 Project Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hosseingz/tiny-url.git
   cd tiny-url
   ```

2. **Install dependencies:**
   It's a good idea to use a virtual environment.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Create migrations and apply them:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser (for accessing the Django admin):**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server:**
   ```bash
   python manage.py runserver
   ```

Now, your project should be up and running! You can access the Django admin panel at `http://127.0.0.1:8000/admin` and the API endpoints at `http://127.0.0.1:8000/api`.

## 📖 API Endpoints

- **Create a shortened URL** (POST request):
  - Endpoint: `/api/c/`
  - Payload: `{ "url": "https://example.com" }`
  
  Example curl:
  ```bash
  curl -X POST http://127.0.0.1:8000/api/c/ -d '{"url": "https://example.com"}' -H 'Content-Type: application/json'
  ```

- **Redirect using shortened URL**:
  - Endpoint: `/api/t/<short_link>/`
  - Example: `http://127.0.0.1:8000/api/t/abc123` will redirect to the corresponding long URL.


## 🎉 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

