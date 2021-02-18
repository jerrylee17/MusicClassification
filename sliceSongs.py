import os
from pydub import AudioSegment

'''
INCOMPLETE
'''
# Paths
DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
SONG_PATH = DIRECTORY_PATH + '/songs/'
TARGET_PATH = DIRECTORY_PATH + '/processedSongs/'


def renameSongs(PATH):
    songs = os.listdir(PATH)
    for s in songs:
        src = PATH + s
        dst = src.replace(' ', '-')
        os.rename(src, dst)


def sliceSongs(PATH, TARGET_PATH):
    songs = os.listdir(PATH)
    print(songs)


renameSongs(SONG_PATH)
# sliceSongs(SONG_PATH, TARGET_PATH)
