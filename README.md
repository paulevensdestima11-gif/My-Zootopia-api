# Zootopia Animals API Project

## Description
This project generates a dynamic website that displays information about animals using data fetched from an external API.

The user enters an animal name, and the program retrieves matching results from the API and generates an HTML page showing the animal details.

The project demonstrates:
- API integration using requests
- Separation of concerns (data fetching vs website generation)
- Use of environment variables for security
- Dynamic HTML generation
- Error handling for missing data

---

## Project Structure

- `animals_web_generator.py` → Generates the HTML website
- `data_fetcher.py` → Fetches data from the API
- `animals_template.html` → HTML template file
- `requirements.txt` → Required Python packages
- `.env` → Stores API key (not included in GitHub)
- `.gitignore` → Prevents sensitive/system files from being pushed

---

## Installation

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
