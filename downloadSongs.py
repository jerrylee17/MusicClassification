import youtube_dl

# Example array of an input array
music = [
    'get your wish porter robinson',
    'look at the sky porter robinson'
]


def downloadSongs(music):
    '''
    Downloads music based on input

        Parameter:
            music [str]: List of tuples 
                with song name and youtube link
    '''
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            # 'preferredquality': '192',
        }],
        'min_views': 100_000,
        'noplaylist': True,
        'outtmpl': './songs/%(title)s.%(ext)s'
    }
    # Set up downloader with options
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    # Process music array
    music = [f'ytsearch1:{m}' for m in music]
    # Download music
    ydl.download(music)


downloadSongs(music)
