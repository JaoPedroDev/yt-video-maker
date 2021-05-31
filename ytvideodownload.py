import os

downloadPath = (
    "/home/joaopedro/Videos/GGTP/Creating Videos/Current_Videos/" +
    "%(autonumber)02d_%(title)s.%(ext)s"
)

linkList = "list.txt"

os.system(
    f'youtube-dl -f best -o "{downloadPath}" -a "{linkList}"'
)

print("downloads done...")
