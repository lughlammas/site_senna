import os

# Caminho da pasta com as imagens
pasta_imagens = 'assets'

# Lista os arquivos na pasta
arquivos = os.listdir(pasta_imagens)

# Filtra só as imagens jpg
imagens = [arq for arq in arquivos if arq.lower().endswith('.jpg')]

# Ordena só por segurança (caso queira uma ordem alfabética)
imagens.sort()

# Renomeia para ayrton1, ayrton2, ...
for indice, imagem in enumerate(imagens, start=1):
    novo_nome = f"ayrton{indice}.jpg"
    caminho_antigo = os.path.join(pasta_imagens, imagem)
    caminho_novo = os.path.join(pasta_imagens, novo_nome)
    os.rename(caminho_antigo, caminho_novo)

print(f"✅ Todas as imagens renomeadas com sucesso!")
