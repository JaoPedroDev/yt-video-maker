import moviepy.editor as mpy
import gizeh_title as gt

clip = mpy.VideoFileClip("current_videos/03_Nidhogg 2 Launch Trailer _ PS4.mp4")
title = "Naruto Ultimate Ninja Storm"

final_clip = gt.title_maker(title, clip)

final_clip.write_gif("test.gif", fps=2)
