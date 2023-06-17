from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory
import tkinter as tk
from pytube import YouTube
import moviepy.editor as mp
import re
import os


def selecionar_arquivo():
    caminho_arquivo = askdirectory(title='SELECIONE O LOCAL')
    caminho_path.set(caminho_arquivo)
    print(caminho_path)


def download_video():
    link = link_yt.get()
    entry_absoluto = caminho_path.get()
    if entry_absoluto is not None:
        path = os.path.abspath(entry_absoluto)
        print(path)
        yt = YouTube(link)
        ys = yt.streams.filter(
            only_audio=False, file_extension='mp4').first().download(path)
        messagebox.showinfo(title="YouTube Downloader",
                            message="Download Finalizado!")


def download_music():
    link = link_yt.get()
    entry_absoluto = caminho_path.get()
    if entry_absoluto is not None:
        path = os.path.abspath(entry_absoluto)
        yt = YouTube(link)
        ys = yt.streams.filter(only_audio=True).first().download(path)
        for file in os.listdir(path):
            if re.search('mp4', file):
                mp4_path = os.path.join(path, file)
                mp3_path = os.path.join(
                    path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        messagebox.showinfo(title="YouTube Downloader",
                            message='Download e Conversão para MP3 Finalizado')


window = Tk()
window.geometry("710x404")
window.configure(bg="#ffffff")
window.title('YouTube Downloader - V1.0')
caminho_icone = "icons/youtube.ico"
window.iconbitmap(caminho_icone)


canvas = Canvas(
    window,
    bg="#ffffff",
    height=404,
    width=710,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

background_img = PhotoImage(file="icons/background.png")
background = canvas.create_image(640.0, 360.0, image=background_img)

fechar_img = PhotoImage(file="icons/img0.png")
b_fechar = Button(
    image=fechar_img,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
b_fechar.place(x=549, y=363, width=91, height=35)

mp3_img = PhotoImage(file="icons/img1.png")
b_mp3 = Button(
    image=mp3_img,
    borderwidth=0,
    highlightthickness=0,
    command=download_music,
    relief="flat"
)
b_mp3.place(x=493, y=241, width=147, height=34)

video_img = PhotoImage(file="icons/img2.png")
b_video = Button(
    image=video_img,
    borderwidth=0,
    highlightthickness=0,
    command=download_video,
    relief="flat"
)
b_video.place(x=199, y=241, width=147, height=34)


caminho_os = tk.Button(
    text="SELECIONAR LOCAL",
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0,
    command=selecionar_arquivo
)
caminho_os.place(x=199, y=188, width=441, height=22)

caminho_path = tk.StringVar()

link_img = PhotoImage(file="icons/img_textBox1.png")
link_bg = canvas.create_image(419.5, 152.5, image=link_img)

link_yt = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0
)
link_yt.place(x=199, y=141, width=441, height=21)

window.resizable(False, False)
window.mainloop()
