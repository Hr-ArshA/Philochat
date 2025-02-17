# PhiloChat

PhiloChat is a real-time chat application built with Django and Django Channels. It allows users to engage in private and group chats using WebSockets for seamless communication. The project is containerized using Docker for easy deployment and comes with PostgreSQL and Redis integration.

## Features

- **User Authentication**: Custom user model with profile pictures and bios.
- **Group Chat**: Users can create and join group chats.
- **Private Messaging**: One-on-one chat functionality.
- **WebSockets Support**: Real-time messaging using Django Channels.
- **Redis for Channels Layer**: Enhances scalability and performance.
- **PostgreSQL Database**: Used as the primary database.
- **Docker Support**: Easily set up the development environment using `docker-compose`.

---

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/Hr-ArshA/Philochat.git
cd philochat
```

### 2. Set Up Environment Variables

Copy the sample `.env-sample` file and rename it to `.env`:

```sh
cp .env-sample .env
```

Modify the `.env` file with your database credentials and secret keys.

### 3. Install Dependencies

**Using Python Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Run Database Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional)

```sh
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

---

## Running the Application

### Option 1: Using Docker

```sh
docker-compose up --build
```

This will start:
- PostgreSQL Database
- Redis Cache
- Django Server

### Option 2: Running Locally

If you prefer running the project without Docker:

```sh
python manage.py runserver
```

The app will be accessible at `http://127.0.0.1:8000/`.

---

## Usage

- Visit the homepage to enter a chat room.
- Enter a chat room name and start chatting.
- Messages will be broadcasted in real-time using WebSockets.

---

## Project Structure

```
/philochat
│-- account/            # User authentication and profile management
│-- chat/               # Chat application (models, views, consumers)
│-- config/             # Django project settings
│-- templates/          # HTML templates for UI
│-- docker-compose.yml  # Docker configuration
│-- manage.py           # Django management script
│-- requirements.txt    # Dependencies
│-- .env-sample         # Sample environment variables
```

---

## Technologies Used

- **Django**: Web framework
- **Django Channels**: WebSockets support
- **PostgreSQL**: Database
- **Redis**: Caching and Channels Layer
- **Docker**: Containerization
- **Bootstrap**: Frontend styling
- **WebSockets**: Real-time messaging

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added a new feature"`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

---

## Contact

For any issues or feature requests, feel free to open an issue or reach out:

📧 **E-mail**: [a_sh1379@yahoo.com](mailto:a_sh1379@yahoo.com)
🔗 **GitHub**: [https://github.com/Hr-ArshA](https://github.com/Hr-ArshA)

---

Enjoy chatting with **PhiloChat**! 🚀
