from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

name = "Defuse_conflicts_62s"
max = 119


def slice_video(name, max):
    for i in range(0, max, 10):
        start = i
        end = i + 10
        ffmpeg_extract_subclip(F"/Users/Apple/Desktop/{name}.mp4", start, end, targetname= F"/Users/Apple/Desktop/Sliced_movie/{name}_{i}.mp4")


if __name__ == '__main__':
    slice_video(name, max)
