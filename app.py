from flask import Flask, request, jsonify, send_file,render_template
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get('url')
    resolution = data.get('resolution')
    format = data.get('format')

    if not url or not resolution or not format:
        return jsonify({"error": "Missing required parameters"}), 400

    # Set options for yt-dlp
    ydl_opts = {
        'format': f'bestvideo[height<={resolution[:-1]}]+bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': format
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,  # Download only single video, not playlist
    }

    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Assuming the file is saved in the downloads directory
        return jsonify({"message": "Download completed"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
