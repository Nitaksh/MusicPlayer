from pygame import mixer
from moviepy.editor import *
import os 
from pytube import *
import tkinter as tk
y,z=0,0
class node:
    def __init__(s,link=None):
        s.linker=link
        s.nextval=None
        s.preval=None
class ll:
    def __init__(s):
        s.headval=None
        s.start=None
def inputer():
    global l
    l=ll()
    w=tk.Toplevel()
    f=open("musicfiles.txt","r")
    r=f.readlines()
    global le
    le=len(r)
    j=0
    tk.Label(w,text="Your Playlist",font=('Consolas',20)).grid(row=0,column=0)
    global y
    for i in r:
        y=y+1
        tk.Label(w,text=i[0:-1],font=('Consolas',10)).grid(row=y,column=1)
    y=y+1
    tk.Button(w,text="prev",command=prev,font=('Consolas',20)).grid(row=y,column=0)
    tk.Button(w,text="Play",command=play,font = ('Consolas',20)).grid(row=y,column=1)
    tk.Button(w,text="next",command=next1,font=('Consolas',20)).grid(row=y,column=2)
    tk.Button(w,text="Pause",command=pause,font=('consolas',20)).grid(row=y+1,column=1)
    tk.Button(w,text="unpause",command=unpause,font=('consolas',20)).grid(row=y+2,column=1)
    tk.Button(w,text="stop",command=stop,font=('consolas',20)).grid(row=y+3,column=1)
    for i in r:
        j=j+1
        if j==1:
            a=node(i)
            l.headval=a
            l.start=a
            a.nextval=l.start
            a.preval=l.start
        else:
            a=node(i)
            l.start.nextval=a
            a.preval=l.start
            a.nextval=l.headval
            l.headval.preval=a
            l.start=a
def next1():
    stop()
    l.start=l.start.nextval
    mixer.music.load((l.start.linker)[0:-1])
    mixer.music.play()
    
def prev():
    stop()
    l.start=l.start.preval
    mixer.music.load((l.start.linker)[0:-1])
    mixer.music.play()
def play():
    l.start=l.headval
    mixer.init()
    mixer.music.load((l.start.linker)[0:-1])
    mixer.music.play()
def pause():
   mixer.music.pause()
def unpause():
    mixer.music.unpause()
def stop():
    mixer.music.stop()
    mixer.music.unload()
def download():
    win=tk.Toplevel()
    win.title("download")
    tk.Label(win,text="Enter the search string for the song you want to download ... ",font = ('Consolas',20)).grid(row=1,column=0)
    global x
    x=tk.StringVar()
    tk.Entry(win,textvariable=x).grid(row=1,column=1)
    tk.Button(win,text="Search",command=search,font = ('Consolas',20)).grid(row=3,column=1)
def search():
    s=x.get()   
    print(s)
    a = Search(s)
    result = a.results
    query = ((str(result[0]).split("="))[-1])[0:-1]
    os.system('pytube https://www.youtube.com/watch?v='+query)
    fname = YouTube('https://www.youtube.com/watch?v='+query)
    vidname = fname.title
    vidname = vidname.split('|')
    fname = ''.join(vidname)
    temp = fname 
    temp = temp.split('.')
    fname = ''.join(temp)
    temp=fname
    temp=temp.split(',')
    fname=''.join(temp)
    temp=fname
    temp=temp.split("'")
    fname = ''.join(temp)
    Mp4 = fname+".mp4"
    Mp3 = fname+".mp3"
    Video = VideoFileClip(Mp4)
    Audio = Video.audio
    Audio.write_audiofile(Mp3)
    Audio.close()
    f=open("musicfiles.txt","a")
    f.write(Mp3+'\n')
    f.close()
root=tk.Tk()
root.title("main")
top = tk.Frame(root)
top.pack()
top.grid(row = 0,column = 0)
tk.Label(top,text="Welcome to our music player !!!",font = ('Consolas',20)).grid(row = 0,column = 1)
tk.Button(root,text = "DOWNLOAD MUSIC",command=download,font = ('Consolas',18,'bold'), padx = 20).grid(row = 1,column = 0)
tk.Button(root,text = "YOUR LIBRARY",command=inputer,font = ('Consolas',18,'bold')).grid(row = 2,column = 0)
root.mainloop()