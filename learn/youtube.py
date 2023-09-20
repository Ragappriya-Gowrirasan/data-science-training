from pytube import YouTube

# URL of the YouTube video you want to download
video_url_1 = "https://www.youtube.com/shorts/ugVG-0prZGA" 
video_url_2 = "https://www.youtube.com/shorts/8OLAi6Eba98" 
video_url_3 ="https://www.youtube.com/shorts/q2h7f133ZcI"

video = [video_url_2,video_url_1,video_url_3]
# Create a YouTube object
yt = YouTube(video)

# Select the stream with the desired resolution and file format (e.g., mp4)
stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

# Download the video to the current directory
stream.download()

print("Download complete.")


