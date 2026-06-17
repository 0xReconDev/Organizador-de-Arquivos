#Próximo passo é fazer uma verificação de arquivos não listados e criar uma pasta separada para eles.

import os
import shutil

pasta_alvo = os.path.expanduser('~/Documentos') #Encontra o caminho absoluto para a pasta solicitada.

tipos = {
        'imagens': ['.jpg', 'jpeg', '.png', '.gif'],
        'Videos': ['.mp4', '.mkv', '.avi'],
        'PDFs': ['.pdf'],
        'Texto': ['.txt', '.md'],
        'Compactados': ['.zip', '.rar', '.7z']
}

def organizar():
    for arquivos in os.listdir(pasta_alvo):

        caminho_arquivo = os.path.join(pasta_alvo, arquivos) # Organiza o caminho até o arquivo. Ex: Pasta/arquivo.md.
        if os.path.isfile(caminho_arquivo): # Verifica se é realmente um arquivo e não pasta.

            movido = False

            for pasta, formato in tipos.items(): # Atribui a extensão de arquivo ao arquivo.

                if any(arquivos.lower().endswith(ext) for ext in formato): #Verifica se o arquivo temina com extensoes válida na lista, retorna TRUE.

                    destino = os.path.join(pasta_alvo, pasta) # Essa variável vai entrar na pasta alvo e criar uma pasta referente a lista.
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(caminho_arquivo,  os.path.join(destino, arquivos))

                    movido = True
                    continue
organizar()
print('Movido')
