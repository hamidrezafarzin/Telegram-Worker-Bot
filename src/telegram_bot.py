import requests

class TelegramBot:
    def __init__(self, worker_url, bot_token, chat_id):
        """
        Initialize the TelegramBot class with worker URL, bot token, and chat ID.
        :param worker_url: The Cloudflare worker URL (e.g. "https://<your-worker-id>.<your-domain>.workers.dev")
        :param bot_token: Your Telegram bot token (received from BotFather)
        :param chat_id: The chat ID where you want to send the message/file
        """
        self.worker_url = worker_url.rstrip('/')  # Remove trailing slash if present
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_message(self, text):
        """
        Send a text message to the chat.
        :param text: The text of the message to be sent
        :return: The response from the Telegram API
        """
        url = f"{self.worker_url}/proxy/bot{self.bot_token}/sendMessage"
        data = {
            'chat_id': self.chat_id,
            'text': text
        }
        response = requests.post(url, data=data)
        return response.json()

    def send_document(self, file_path=None, file_url=None):
        """
        Send a document to the chat, either from a local file or via URL.
        :param file_path: The path to the file on your local system (optional)
        :param file_url: The URL of the file to send (optional)
        :return: The response from the Telegram API
        """
        url = f"{self.worker_url}/proxy/bot{self.bot_token}/sendDocument"
        data = {'chat_id': self.chat_id}
        
        if file_url:
            # Sending a file via URL
            data['document'] = file_url
            response = requests.post(url, data=data)
        elif file_path:
            # Sending a file from local system
            with open(file_path, 'rb') as file:
                files = {'document': file}
                response = requests.post(url, data=data, files=files)
        else:
            raise ValueError("You must provide either a file path or a file URL.")
        
        return response.json()

    def send_photo(self, photo_path=None, photo_url=None):
        """
        Send a photo to the chat, either from a local file or via URL.
        :param photo_path: The path to the photo on your local system (optional)
        :param photo_url: The URL of the photo to send (optional)
        :return: The response from the Telegram API
        """
        url = f"{self.worker_url}/proxy/bot{self.bot_token}/sendPhoto"
        data = {'chat_id': self.chat_id}

        if photo_url:
            # Sending a photo via URL
            data['photo'] = photo_url
            response = requests.post(url, data=data)
        elif photo_path:
            # Sending a photo from local system
            with open(photo_path, 'rb') as photo:
                files = {'photo': photo}
                response = requests.post(url, data=data, files=files)
        else:
            raise ValueError("You must provide either a photo path or a photo URL.")
        
        return response.json()

    def send_audio(self, audio_path=None, audio_url=None):
        """
        Send an audio file to the chat, either from a local file or via URL.
        :param audio_path: The path to the audio file on your local system (optional)
        :param audio_url: The URL of the audio file to send (optional)
        :return: The response from the Telegram API
        """
        url = f"{self.worker_url}/proxy/bot{self.bot_token}/sendAudio"
        data = {'chat_id': self.chat_id}

        if audio_url:
            # Sending an audio file via URL
            data['audio'] = audio_url
            response = requests.post(url, data=data)
        elif audio_path:
            # Sending an audio file from local system
            with open(audio_path, 'rb') as audio:
                files = {'audio': audio}
                response = requests.post(url, data=data, files=files)
        else:
            raise ValueError("You must provide either an audio path or an audio URL.")
        
        return response.json()

    def send_video(self, video_path=None, video_url=None):
        """
        Send a video file to the chat, either from a local file or via URL.
        :param video_path: The path to the video file on your local system (optional)
        :param video_url: The URL of the video file to send (optional)
        :return: The response from the Telegram API
        """
        url = f"{self.worker_url}/proxy/bot{self.bot_token}/sendVideo"
        data = {'chat_id': self.chat_id}

        if video_url:
            # Sending a video file via URL
            data['video'] = video_url
            response = requests.post(url, data=data)
        elif video_path:
            # Sending a video file from local system
            with open(video_path, 'rb') as video:
                files = {'video': video}
                response = requests.post(url, data=data, files=files)
        else:
            raise ValueError("You must provide either a video path or a video URL.")
        
        return response.json()