# list of some possible file extentions for pics sound, sounds and video
import os
import shutil

# only works with tuples not list (be carefull when adding and updating new formats)
PICTURE_FORMAT = (
    ".webp",
    ".png",
    ".jpg",
    ".JPG",
    ".jpeg",
    ".jpe",
    ".jif",
    ".jfif",
    ".jfi",
    ".gif",
    ".webp",
    ".tiff",
    ".tif",
    ".psd",
    ".raw",
    ".arw",
    ".cr2",
    ".nrw",
    ".k25",
    ".bmp",
    ".dib",
    ".heif",
    ".heic",
    ".ind",
    ".indd",
    ".indt",
    ".jp2",
    ".j2k",
    ".jpf",
    ".jpx",
    ".jpm",
    ".mj2",
    ".svg",
    ".svgz",
    ".CR2",
)
AUDIO_FORMAT = (".mp3", ".acc", ".wma")
VIDEO_FORMAT = (".mp4", ".mov", ".wmv", ".avi", "avchd", ".mkv")

PDF = (".pdf",)
SOFTWARE = (".exe", ".msi")
DOWNLOAD_FOLDER = "C:\\Users\\Peter\\Downloads"
SOURCE_PATH = os.listdir(DOWNLOAD_FOLDER)
DESTINATION = "C:\\Users\\Peter\\"


def picture_management():
    x = f"{DESTINATION}Pictures\\DOWNLOADED PICTURES"
    for file in SOURCE_PATH:
        if file.endswith(PICTURE_FORMAT):
            shutil.move(os.path.join(DOWNLOAD_FOLDER, file), os.path.join(x, file))


def video_management():
    x = f"{DESTINATION}Videos"
    for file in SOURCE_PATH:
        if file.endswith(VIDEO_FORMAT):
            shutil.move(os.path.join(DOWNLOAD_FOLDER, file), os.path.join(x, file))


def audio_management():
    x = f"{DESTINATION}Music"
    for file in SOURCE_PATH:
        if file.endswith(AUDIO_FORMAT):
            shutil.move(os.path.join(DOWNLOAD_FOLDER, file), os.path.join(x, file))


def pdf():
    x = f"{DESTINATION}Downloads\\PDF"
    for file in SOURCE_PATH:
        if file.endswith(PDF):
            shutil.move(os.path.join(DOWNLOAD_FOLDER, file), os.path.join(x, file))


def installer():
    x = f"{DESTINATION}Downloads\\SOFTWARE"
    for file in SOURCE_PATH:
        if file.endswith(SOFTWARE):
            shutil.move(os.path.join(DOWNLOAD_FOLDER, file), os.path.join(x, file))


picture_management()
video_management()
audio_management()
pdf()
installer()
