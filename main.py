import youtube_dl
from pathlib import Path

try:
    entrada = (input('digite o link do video que deseja baixar: '))
    link = [entrada]

    caminho_download = str(Path.home() / "Downloads")

    ydl_opts = {
        'outtmpl': caminho_download + '/%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(link)

except:
    print('LINK INVALIDO')
