from pathlib import Path

x = Path(r'C:\Users\User')
s = Path(r'C:\Users\User\Downloads')

extencoes ={
    'pdf': 'Documents',
    'txt': 'Documents',
    'doc': 'Documents',
    'docx': 'Documents',
    'xls': 'Documents',
    'xlsx': 'Documents',
    'ppt': 'Documents',
    'pptx': 'Documents',
    'jpg': 'Pictures',
    'jpeg': 'Pictures',
    'png': 'Pictures',
    'gif': 'Pictures',
    'mp4': 'Videos',
    'mp3': 'Music',
    'zip': 'Downloads',
    'rar': 'Downloads',
    'exe': 'Downloads',
}

def organize():
    diretorio_base = input('Informe o diretório base: ')
    p = input('Informe o diretório a ser organizado: ')
    diretorio_base = Path(diretorio_base) 
    p = Path(p) 
    for file in p.iterdir():
        if file.is_file():
            extencao = file.suffix[1:].lower()
            if extencao in extencoes:
                diretorio_alvo= diretorio_base / extencoes[extencao]
                file.rename(diretorio_alvo / file.name)

organize()