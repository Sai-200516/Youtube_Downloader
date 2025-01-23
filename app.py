@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get('url')
    resolution = data.get('resolution')
    
    if not url or not resolution:
        return jsonify({"error": "Missing required parameters"}), 400

    # Set options for yt-dlp (Avoiding FFmpeg requirement)
    ydl_opts = {
        'format': f'best[height<={resolution[:-1]}]',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,  # Download only single video, not playlist
    }

    # Create downloads directory if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)

        return jsonify({"message": "Download completed", "file_name": file_name}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
