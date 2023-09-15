from pytube import YouTube

# URL of the YouTube video you want to download
#video_url = "https://www.youtube.com/shorts/ugVG-0prZGA"

# Create a YouTube object
yt = YouTube("https://www.youtube.com/shorts/ugVG-0prZGA")

# Select the stream with the desired resolution and file format (e.g., mp4)
stream = yt.streams.filter(progressive=True, file_extension="mp4").first()

# Download the video to the current directory
stream.download()

print("Download complete.")

link = "https://www.youtube.com/shorts/FcZ0U-6EMkw"
link1 = "https://www.youtube.com/shorts/ugVG-0prZGA"
link2 = "https://www.youtube.com/shorts/LHCTB-iFsz0"

list = []

for r in list:



