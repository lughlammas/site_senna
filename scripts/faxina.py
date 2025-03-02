import os

# Caminho da pasta com as imagens
pasta_imagens = "assets"

# Extensões que a gente vai trabalhar (se quiser pode expandir)
extensoes_validas = ['.jpg', '.jpeg', '.png', '.webp']

# Percorre os arquivos da pasta
for arquivo in os.listdir(pasta_imagens):
    caminho_antigo = os.path.join(pasta_imagens, arquivo)

    # Só processa se for arquivo (ignora pastas)
    if not os.path.isfile(caminho_antigo):
        continue

    # Separa nome e extensão
    nome, ext = os.path.splitext(arquivo)

    # Normaliza a extensão (força .jpg, se quiser)
    nova_ext = '.jpg'

    # Cria novo nome: tudo minúsculo, sem espaços esquisitos
    novo_nome = nome.strip().replace(" ", "_").lower() + nova_ext
    novo_caminho = os.path.join(pasta_imagens, novo_nome)

    # Renomeia o arquivo
    os.rename(caminho_antigo, novo_caminho)

    print(f"✅ {arquivo} -> {novo_nome}")

print("\n🏁 FAXINA CONCLUÍDA!")
