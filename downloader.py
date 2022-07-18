#!/usr/bin/python

from pytube import YouTube
from sys import argv

link= argv[1]
yt= YouTube(link)

print("Title:", yt.title, "\n")

print("Views:", yt.views, "\n")

print("\n")

audio= yt.streams.get_audio_only()

audio.download("C:\\Users\\diego\\Music\\Downloads")
