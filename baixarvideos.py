from pytube import YouTube
import moviepy.editor as mp
import re
import os

#Recebendo o link

link = input("Digite o link que di vídeo que deseja baixar: ")
path = input("Digite o diretório que deseja salvar o vídeo: ")
yt = YouTube(link)

#Iniciar o download
print("Baixando")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download completo")

#converter , mp2 pra mp3

print("Convertentendo pra mp3")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Sucesso")        
        


