# Translator

A simple yet powerful translator app built using Django that can translate text into up to 50 different languages. The app leverages the `googletrans` Python library to provide seamless language translations.

![alt text](https://github.com/sachnaror/core/raw/main/image-1.png =500x500)

## Features

- **Multi-Language Support:** Translate text into over 50 different languages.
- **User-Friendly Interface:** A simple form where users can input the text they want to translate and select the destination language.
- **Real-Time Translation:** Translations are processed instantly using Google Translate.

## Requirements

- Python 3.12+
- Django 5.1+
- googletrans==4.0.0-rc1

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/translator.git
   cd translator

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Run the development server:**
   ```bash
   python manage.py runserver

5. **Access the app:**
   Open your web browser and navigate to http://localhost:8000/

## Usage

   1. Enter the text you want to translate in the input field.
   2. Select the language you want to translate the text into from the dropdown menu.
   3. Click the "Translate" button.
   4. The translated text will be displayed below the input field.


