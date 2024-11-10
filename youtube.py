import os

def download_youtube_video(video_url, download_path='.'):
    # Use yt-dlp to download the best quality video and audio
    os.system(f'yt-dlp -f "bestvideo+bestaudio" -o "{download_path}/%(title)s.%(ext)s" {video_url}')

if __name__ == '__main__':
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (leave blank for current directory): ") or '.'
    download_youtube_video(video_url, download_path)
