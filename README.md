# Flask App Template

## Getting Started

### Prerequisites
Ensure you have Docker and Docker Compose installed on your system.

### Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/MucahidAydin/flask-app-template.git
   cd flask-app-template
   ```

2. Build and start the project:
   ```bash
   docker compose up --build
   ```

## API Usage

### Get Current Weather Forecast

To test the API, run:
```bash
curl -X GET "http://localhost/api/v1/weather-forecasts/current?city=ankara"
```

Alternatively, open a browser and navigate to:
```
http://localhost/api/v1/weather-forecasts/current?city=ankara
```

### Stopping the Application

To stop the running containers, use:
```bash
docker compose down
```