import requests

def download_song(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        
        print(f"Download complete: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the song: {e}")

# Example usage
song_url = "https://youtu.be/Mz2yP0A3t4o"  # Replace with the actual song URL
file_name = "downloaded_song.mp3"
download_song(song_url, file_name)
