import gizeh
import moviepy.editor as mpy


def title_maker(game_title, clip):
    title = game_title
    original_clip = clip
    fontfamily = "Consolas"
    fontweight = 'bold'
    fontsize = 30
    duration = 8
    rect_y = 50
    rect_x = 20 * len(title) + (20 if len(title) <= 6 else 0)

    # make a shape and draw it on the surface
    black_rectangle = gizeh.rectangle(
        lx=rect_x + 10, ly=rect_y + 10,
        fill=(0, 0, 0),
        xy=(rect_x/2, 0)
        )

    white_rectangle = gizeh.rectangle(
        lx=rect_x, ly=rect_y,
        fill=(255, 255, 255),
        xy=(rect_x/2, 0)
        )

    game_title = gizeh.text(
        title, fontfamily=fontfamily, fontweight=fontweight,
        fill=(0, 0, 0), fontsize=fontsize,
        h_align="left", xy=(20, 0)
        )

    # Try something different to animate
    def make_frame(t):
        if t < 5:
            tr_tranlate_x = -rect_x
            tr_tranlate_x += (rect_x * t)
        else:
            tr_tranlate_x = rect_x
            tr_tranlate_x -= (rect_x * (t - 5))

        if tr_tranlate_x >= 0:
            tr_tranlate_x = 0

        surface = gizeh.Surface(width=1280, height=720)  # in pixels

        text_rect_g = (
            gizeh.Group([black_rectangle, white_rectangle, game_title])
                 .translate(xy=(tr_tranlate_x, 600))
                )

        text_rect_g.draw(surface)
        return surface.get_npimage(transparent=True)

    graphics_clip_mask = mpy.VideoClip(
        lambda t: make_frame(t)[:, :, 3] / 255.0,
        duration=duration, ismask=True
        )

    graphics_clip = mpy.VideoClip(
        lambda t: make_frame(t)[:, :, :3], duration=duration
        ).set_mask(graphics_clip_mask)

    final_clip = mpy.CompositeVideoClip(
        [original_clip,
         graphics_clip],
        size=(1280, 720)
    )
    return final_clip
