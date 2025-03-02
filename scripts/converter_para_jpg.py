from PIL import Image
import os

# Caminho da pasta onde estão suas imagens
pasta_imagens = r"C:\Users\guilh\Documents\Projetos\EBAC\Ayrton\assets"

# Cria uma pasta chamada "convertidas" dentro da pasta original
pasta_convertidas = os.path.join(pasta_imagens, 'convertidas')
os.makedirs(pasta_convertidas, exist_ok=True)

# Extensões válidas
extensoes_validas = ['.webp', '.png', '.jpeg', '.jpg']

# Lista arquivos da pasta
arquivos = os.listdir(pasta_imagens)
print(f"📂 {len(arquivos)} arquivos encontrados na pasta.\n")
from PIL import Image
import os

caminho = 'assets'

# Cria a pasta caso não exista
if not os.path.exists(caminho):
    os.makedirs(caminho)

# Pega todos os arquivos dentro da pasta
for arquivo in os.listdir(caminho):
    antigo_caminho = os.path.join(caminho, arquivo)
    novo_nome = arquivo.lower()

    # Verifica se é imagem válida
    if arquivo.lower().endswith(('png', 'webp', 'jpeg', 'jpg')):
        novo_caminho = os.path.join(caminho, novo_nome)

        # Renomeia para minúsculo
        os.rename(antigo_caminho, novo_caminho)

        # Converte para JPG
        if not novo_nome.endswith('.jpg'):
            img = Image.open(novo_caminho).convert('RGB')
            novo_caminho_jpg = novo_caminho.rsplit('.', 1)[0] + '.jpg'
            img.save(novo_caminho_jpg, 'JPEG')
            os.remove(novo_caminho)  # Deleta original após conversão

convertidos = 0

for arquivo in arquivos:
    caminho_completo = os.path.join(pasta_imagens, arquivo)

    # Normaliza extensão pra minúsculo e remove dupla extensão se existir
    nome, extensao = os.path.splitext(arquivo.lower())

    if extensao in extensoes_validas:
        try:
            imagem = Image.open(caminho_completo).convert('RGB')
            novo_arquivo = os.path.join(pasta_convertidas, f'{nome}.jpg')
            imagem.save(novo_arquivo, 'JPEG', quality=95)

            print(f'✅ Convertido: {arquivo} -> {nome}.jpg')
            convertidos += 1
        except Exception as e:
            print(f'❌ Erro ao converter {arquivo}: {e}')

if convertidos == 0:
    print("⚠️ Nenhuma imagem convertida.")
else:
    print(f"\n🏁 {convertidos} imagens convertidas com sucesso!")
