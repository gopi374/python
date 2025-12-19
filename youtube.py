import os
import pytube
from pytube import YouTube

def download_youtube_video(video_url, output_path=None, resolution="highest"):
    """
    Download a YouTube video at the specified resolution.
    
    Parameters:
    - video_url: The YouTube video URL
    - output_path: The directory to save the video to (default: current directory)
    - resolution: The video resolution to download ("highest", "lowest", or specific like "720p")
    
    Returns:
    - Path to the downloaded video file
    """
    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Print video information
        print(f"Title: {yt.title}")
        print(f"Length: {yt.length} seconds")
        print(f"Author: {yt.author}")
        
        # Get the appropriate stream
        if resolution == "highest":
            # Get the highest resolution progressive stream (with video and audio)
            stream = yt.streams.get_highest_resolution()
        elif resolution == "lowest":
            # Get the lowest resolution
            stream = yt.streams.get_lowest_resolution()
        else:
            # Get a specific resolution if available
            stream = yt.streams.filter(res=resolution, progressive=True).first()
            
            # If the requested resolution is not available, get the highest resolution
            if stream is None:
                print(f"Resolution {resolution} not available. Using highest available resolution.")
                stream = yt.streams.get_highest_resolution()
        
        # Set output path
        if output_path is None:
            output_path = os.getcwd()
        
        # Create the directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        
        # Download the video
        print(f"Downloading: {stream.resolution}")
        file_path = stream.download(output_path)
        print(f"Download complete! File saved to: {file_path}")
        
        return file_path
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    
    # Optional: ask for output directory
    output_dir = input("Enter output directory (press Enter for current directory): ")
    if output_dir.strip() == "":
        output_dir = None
    
    # Optional: ask for resolution
    res = input("Enter resolution (highest/lowest/720p/480p/etc., press Enter for highest): ")
    if res.strip() == "":
        res = "highest"
    
    download_youtube_video(video_url, output_dir, res)
