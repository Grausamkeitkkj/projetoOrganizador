from pathlib import Path

def organizar():
    p = Path(input('Informe o caminho da pasta a ser organizada: '))
    diretorio_base = Path(input(r'Informe o caminho diretório base (Pasta anterior a que será organizada): '))
    print('Informe o nome da pasta a partir do diretório base')
    diretorio_imagens = diretorio_base.joinpath(input('Informe o caminho da pasta de imagens: '))
    diretorio_videos = diretorio_base.joinpath(input('Informe o caminho da pasta de vídeos: '))
    diretorio_musica = diretorio_base.joinpath(input('Informe o caminho da pasta de música: '))
    diretorio_documentos = diretorio_base.joinpath(input('Informe o caminho da pasta de documentos: '))
    diretorio_downloads = diretorio_base.joinpath(input('Informe o caminho da pasta de downloads: '))
    diretorio_executaveis = diretorio_base.joinpath(input('Informe o caminho da pasta de executáveis: '))

    extencoes ={
        'pdf': diretorio_documentos,
        'txt': diretorio_documentos,
        'doc': diretorio_documentos,
        'docx':diretorio_documentos,
        'xls': diretorio_documentos,
        'xlsx':diretorio_documentos,
        'ppt': diretorio_documentos,
        'pptx':diretorio_documentos,
        'jpg': diretorio_imagens,
        'jpeg':diretorio_imagens,
        'png': diretorio_imagens,
        'gif': diretorio_imagens,
        'mp4': diretorio_videos,
        'mp3': diretorio_musica,
        'zip': diretorio_downloads,
        'rar': diretorio_downloads,
        'exe': diretorio_executaveis,
    }

    for arquivos in p.iterdir():
        if arquivos.is_file():
            extencao = arquivos.suffix[1:].lower()
            if extencao in extencoes:
                try:
                    diretorio_alvo= diretorio_base / extencoes[extencao]
                    arquivos.rename(diretorio_alvo / arquivos.name)
                except FileNotFoundError:
                    diretorio_alvo.mkdir()
                    arquivos.rename(diretorio_alvo / arquivos.name)

if __name__ == "__main__":
    organizar()