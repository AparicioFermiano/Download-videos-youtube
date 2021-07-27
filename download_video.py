from pytube import Playlist, YouTube
url = input("Digite a URL: ")
youtube = YouTube(url)
youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
print('Instalação realizada com sucesso')