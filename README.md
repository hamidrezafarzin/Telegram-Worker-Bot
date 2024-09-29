
# Telegram-Worker-Bot

A simple integration of Telegram Bot API with Cloudflare Workers. This project allows you to proxy requests to Telegram's API via a Cloudflare Worker and send messages or files (such as documents, photos, etc.) using a Python script.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Cloudflare Worker Setup](#cloudflare-worker-setup)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Dependencies](#dependencies)
7. [License](#license)
8. [Acknowledgements](#acknowledgements)

## Features
- **Worker Script**: A Cloudflare Worker script to proxy requests to Telegram's Bot API.
- **Python Script**: A Python class to send messages and files via the Worker proxy to Telegram chats.

## Installation

### 1. Clone the Repository:
```bash
git clone https://github.com/hamidrezafarzin/Telegram-Worker-Bot.git
cd TelegramWorkerBot
```

### 2. Set Up the Python Environment:
Create and activate a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Cloudflare Worker:
Deploy your Cloudflare Worker using the script in `worker/worker.js`.
Make sure your Worker is configured to proxy requests to the Telegram Bot API.

## Cloudflare Worker Setup

### Steps to run on Cloudflare Workers:

1. **Create a Cloudflare Worker**: 
    - Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/).
    - Select your domain, and navigate to "Workers" in the sidebar.
    - Click "Create a Worker" and give it a name.
    - Replace the default Worker script with the content from `worker/worker.js` in this repository.

2. **Update the Worker script**: 
    - Make sure that the Worker script proxies requests to Telegram's Bot API by adding the following code to handle the Telegram requests correctly.

3. **Deploy the Worker**: 
    - Click "Save and Deploy" in the Cloudflare dashboard. 
    - Once deployed, your Worker will have a unique URL (e.g., `https://your-worker-id.your-domain.workers.dev`).

4. **Update your Python script**:
    - In `src/telegram_bot.py`, set the `worker_url` to the URL of your deployed Cloudflare Worker.

## Usage

### Send a Message:
You can use the `send_message()` method from the Python script to send a text message to a chat.

```python
from telegram_bot import TelegramBot

bot = TelegramBot(
    worker_url="https://your-worker-id.your-domain.workers.dev",
    bot_token="123456789:ABCDEF123456789ghijklmnopqrst",
    chat_id="987654321"  # Replace with your chat ID
)

response = bot.send_message("Hello, world!")
print(response)
```

### Send a Document:
You can send a document from your local file system or a URL using the `send_document()` method.

```python
# Send a document from a local file
response = bot.send_document(file_path="path_to_file.pdf")
print(response)

# Send a document from a URL
response = bot.send_document(file_url="https://example.com/path_to_file.pdf")
print(response)
```

### Send a Photo:
Send a photo using the `send_photo()` method:

```python
# Send a photo from a local file
response = bot.send_photo(photo_path="path_to_image.jpg")
print(response)

# Send a photo from a URL
response = bot.send_photo(photo_url="https://example.com/path_to_image.jpg")
print(response)
```

## Project Structure

```bash
TelegramWorkerBot/
│
├── worker/
│   └── worker.js           # Cloudflare Worker script for proxying requests
│
├── src/
│   └── telegram_bot.py      # Python script to send messages and files via the worker
│
├── README.md                # This documentation file
├── requirements.txt         # Python dependencies
└── .gitignore               # Ignoring unnecessary files
```

## Dependencies
- `requests`: Used to handle HTTP requests. Install via `pip install -r requirements.txt`.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Thanks to [Armin darabi](https://github.com/arminadm) for the helpful hints and guidance!
