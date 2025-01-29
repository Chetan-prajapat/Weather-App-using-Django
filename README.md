🌦️ Weather App with Django Rest Framework
Welcome to the Weather App, a mini personal project built to understand and explore APIs using Django Rest Framework (DRF). This app allows you to check the current weather for any city using the Weatherstack API.

🚀 Features
Real-Time Weather Data: Fetch real-time weather information for any city.

Simple Interface: Enter a city name, and get the weather details instantly.

Built with Django Rest Framework: A great way to learn and practice DRF.

Powered by Weatherstack API: Reliable and accurate weather data.

🛠️ Technologies Used
Backend: Django Rest Framework

API: Weatherstack API

Frontend: Basic HTML/CSS (optional, for a simple interface)

Tools: Python, Django, RESTful APIs

📋 How to Use
Enter a City Name: On the homepage, enter the name of the city you want to check the weather for.

Get Weather Details: The app will fetch and display the current weather information, including:

Temperature

Weather Description

Humidity

Wind Speed

and more!

🛠️ Setup and Installation
Prerequisites
Python 3.x

Django

Django Rest Framework

Weatherstack API Key (Sign up at Weatherstack to get your free API key)

Steps to Run the Project
Clone the Repository:

bash
Copy
git clone https://github.com/Chetan-prajapat/Weather-App-using-Django.git
cd weather-app-django
Install Dependencies:

bash
Copy
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file in the root directory and add your Weatherstack API key:

Copy
WEATHERSTACK_API_KEY=your_api_key_here
Run Migrations:

bash
Copy
python manage.py migrate
Start the Development Server:

bash
Copy
python manage.py runserver
Access the App:
Open your browser and go to http://127.0.0.1:8000/.

🖼️ Screenshots
Weather App Screenshot
Example: Weather details for New York.

📂 Project Structure
Copy
weather-app-django/
├── api/                  # Django app for API endpoints
├── templates/            # HTML templates for the frontend
├── manage.py             # Django management script
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
🤝 Contributing
This is a personal project, but feel free to fork the repository and contribute! If you have any suggestions or improvements, open an issue or submit a pull request.

📜 License
This project is open-source and available under the MIT License.

🙏 Acknowledgments
Thanks to Weatherstack for providing the weather data API.

Thanks to the Django and Django Rest Framework communities for their amazing documentation and support.

📧 Contact
Have questions or feedback? Feel free to reach out!
Email: prajapatchetan18@gmail.com
GitHub: https://github.com/Chetan-prajapat

Enjoy exploring the weather! 🌤️🌧️🌪️

