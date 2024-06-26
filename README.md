# HarvestHub

HarvestHub is an API-based platform that provides real-time agricultural information and notifications to farmers via WhatsApp. It integrates AI models for personalized recommendations and updates.

## Features

- WhatsApp Integration: Receive notifications and interact with the system via WhatsApp.
- Crop Recommendations: AI-powered recommendations for seeds, fertilizers, and pesticides.
- Weather Updates: Daily weather forecasts for specific regions.
- Market Insights: Real-time market prices and demand trends.
- Community Chat: Farmers can share experiences and ask questions.

## Installation

1. Clone this repository:

```python
git clone https://github.com/SBMOYO/HarvestHub.git
```

2. Install dependencies:

```python
   pip install -r requirements.txt
```

3. Set up your Twilio account and configure API keys.
4. Run migrations:

```python
   python manage.py migrate
```

5. Start the development server:

```python
   python manage.py runserver
```

## Usage

1. Access the API at `python http://127.0.0.1:8000/`.
2. Subscribe to receive WhatsApp notifications.
3. Explore available endpoints for crop recommendations, weather updates, and more.

## Contributing

Contributions are welcome! Please follow our contribution guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
