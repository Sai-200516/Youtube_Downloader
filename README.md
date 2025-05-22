# Buck - YouTube Video Downloader 📹

Buck is a user-friendly web application built with Flask that enables downloading YouTube videos in your preferred resolution and format. With a sleek interface, it supports resolutions from 240p to 720p and formats like MP4, MKV, and WEBM, making video downloading simple and efficient.

## Features
- **Customizable Downloads**: Choose video resolution (240p, 360p, 480p, 720p) and format (MP4, MKV, WEBM).
- **Intuitive Interface**: Enter a YouTube URL, select options, and download with a single click.
- **Server-Side Processing**: Downloads are handled securely on the backend, with files saved to a `downloads/` directory.
- **Error Handling**: Provides clear feedback for invalid URLs or download issues.
- **Lightweight Design**: Built to run locally with minimal dependencies.

## Used Libraries
The Buck YouTube Video Downloader relies on the following libraries:
- **Flask**: A Python web framework for routing, request handling, and rendering the web interface.
- **yt-dlp**: A powerful library for downloading YouTube videos, supporting various formats and resolutions.
- **os** (standard library): Manages file system operations, such as creating the `downloads/` directory.

External libraries (Flask, yt-dlp) are listed in `requirements.txt` and can be installed with:
```bash
pip install -r requirements.txt
```

## Installation
Follow these steps to set up Buck locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sai-200516/Youtube_Downloader.git
   cd Youtube_Downloader
   ```

2. **Create a Virtual Environment**:
   Ensure Python 3.6 or higher is installed.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Application**:
   ```bash
   python app.py
   ```

5. **Access the Web Interface**:
   Open your browser and navigate to `http://localhost:5000`.

## Usage
- **Enter Video URL**: Paste a valid YouTube video URL into the input field.
- **Select Resolution**: Choose from 240p, 360p, 480p, or 720p.
- **Select Format**: Pick MP4, MKV, or WEBM as the output format.
- **Download**: Click the "Download" button to start the process.
- **Check Output**: Downloaded videos are saved in the `downloads/` folder in the project directory.
- **Feedback**: The interface displays a success message or error details after the download attempt.

## Project Structure
- `app.py`: The Flask application handling download requests and yt-dlp integration.
- `templates/index.html`: The HTML template for the web interface.
- `requirements.txt`: Lists external dependencies (Flask, yt-dlp).
- `downloads/`: Directory where downloaded videos are saved (created automatically).

## Notes
- **No FFmpeg Required**: The app uses yt-dlp with options that avoid FFmpeg dependency, ensuring simpler setup.
- **Single Video Downloads**: The app is configured to download individual videos, not playlists.
- **Security**: Ensure YouTube URLs are from trusted sources to avoid potential issues.
- **Local Storage**: Downloaded files are stored in the `downloads/` folder. Manage disk space as needed.

## Contributing
Want to improve Buck? Contributions are welcome!
1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add your feature"`.
4. Push to your branch: `git push origin feature/your-feature`.
5. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support
For issues or suggestions, open an issue on [GitHub](https://github.com/Sai-200516/Youtube_Downloader/issues).

*Download your favorite YouTube videos with ease using Buck!*
