import moviepy.editor as mpy
import moviepy.video.fx.all as vfx
import moviepy.audio.fx.all as afx
import gizeh_title as gt
import os

# get the information to render the final video
videofolder = "/home/joaopedro/Videos/GGTP/Creating Videos/Current_Videos/"
defaultVideos = "/home/joaopedro/Videos/GGTP/Creating Videos/Default_Videos/"
savePath = "/home/joaopedro/Videos/GGTP/Creating Videos/Output_Videos/"
codec = 'libx264'
preset = 'ultrafast'
videoname = 'OutputVideo' + '.mp4'
fps = 30
intro = mpy.VideoFileClip(defaultVideos + "intro.mp4")
outro = mpy.VideoFileClip(defaultVideos + "outro.mp4")
# list where the clips are going to be stored
clips = [intro]
title_list = []

with open("list.txt") as f:
    for num, line in enumerate(f, 1):
        if num % 2 != 0:
            title = line.replace('#', '')
            title = title.replace('\n', '')
            title_list.append(title)

i = 0
# iterate through the video folder, alphanumeric sorted
# every video in the folder are edited and added to the clips list
for path in sorted(os.listdir(videofolder)):
    full_path = os.path.join(videofolder, path)

    if os.path.isfile(full_path):
        currentclip = mpy.VideoFileClip(full_path)
        title_clip = gt.title_maker(title_list[i], currentclip)

        newclip = (title_clip.fx(vfx.fadein, 2.0)
                             .fx(vfx.fadeout, 2.0)
                             .resize(height=720))

        i += 1
        clips.append(newclip)

clips.append(outro)
finalclip = mpy.concatenate_videoclips(clips)
finalclip.audio = finalclip.audio.set_fps(44100)
finalclip.fx(afx.audio_normalize)
finalclip.write_videofile(
    savePath + videoname,
    codec=codec,
    preset=preset,
    fps=fps
)

"""
# old way of iterating through a directory
with os.scandir(videofolder) as it:
    for entry in it:
        if entry.is_file():
            currentclip = mpy.VideoFileClip(entry.path)
            newclip = (currentclip.fx(vfx.fadein, 2.0)
                                  .fx(vfx.fadeout, 2.0))

            clips.append(newclip)
"""
