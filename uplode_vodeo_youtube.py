import os
import google.auth
import google.auth.transport.requests
import google.oauth2.credentials
import googleapiclient.discovery
import googleapiclient.errors

def upload_video_to_youtube(video_file_path, title, description):
    # Set up the YouTube API client
    credentials, project = google.auth.default(scopes=["https://www.googleapis.com/auth/youtube.upload"])
    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

    # Create a video insert request with video metadata
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["tag1", "tag2"]
        },
        "status": {
            "privacyStatus": "private"
        }
    }

    # Create a media upload request for the video file
    media_file = googleapiclient.http.MediaFileUpload(video_file_path, chunksize=-1, resumable=True)
    insert_request = youtube.videos().insert(part="snippet,status", body=request_body, media_body=media_file)

    # Upload the video and handle the API response
    response = None
    while response is None:
        status, response = insert_request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}.")
    print(f"Video ID '{response['id']}' was successfully uploaded.")

if __name__ == "__main__":
    video_file_path = "/path/to/video.mp4"
    title = "My Uploaded Video"
    description = "This is a description of my uploaded video."
    upload_video_to_youtube(video_file_path, title, description)
