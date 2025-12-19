
from pytube import YouTube

def download_video_in_480p(video_url, output_path=None):
    
    Download a YouTube video in 480p resolution.

    Parameters:
    - video_url: The YouTube video URL
    - output_path: The directory to save the video to (default: current directory)

    Returns:
    - Path to the downloaded video file or None if an error occurs.
    
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Print video information
        print(f"Title: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"Length: {yt.length} seconds")

        # Filter streams for 480p resolution and progressive (video + audio)
        stream = yt.streams.filter(res="480p", progressive=True).first()

        # If no 480p stream is available, notify the user
        if not stream:
            print("480p resolution is not available for this video.")
            return None

        # Set output path or use current directory
        if output_path is None:
            output_path = "."

        # Download the video
        print(f"Downloading video in 480p...")
        file_path = stream.download(output_path)
        print(f"Download complete! File saved to: {file_path}")

        return file_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    output_dir = input("Enter output directory (press Enter for current directory): ")

    if not output_dir.strip():
        output_dir = None

    download_video_in_480p(video_url, output_dir)
