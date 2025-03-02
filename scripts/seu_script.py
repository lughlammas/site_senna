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

print(f"\n📂 Achamos {len(arquivos)} arquivos na pasta '{pasta_imagens}'")

if not arquivos:
    print("⚠️ A pasta está vazia! Não tem nem o que converter.")
    exit()

convertidos = 0

for arquivo in arquivos:
    print(f"\n🔎 Analisando arquivo: {arquivo}")

    caminho_completo = os.path.join(pasta_imagens, arquivo)
    print(f"📍 Caminho completo: {caminho_completo}")

    nome, extensao = os.path.splitext(arquivo.lower())
    print(f"📄 Nome: {nome}")
    print(f"🧩 Extensão detectada: {extensao}")

    if extensao not in extensoes_validas:
        print(f"❌ Ignorado (extensão não válida): {arquivo}")
        continue

    print(f"✅ Válido! Tentando converter {arquivo}...")

    try:
        imagem = Image.open(caminho_completo).convert('RGB')

        novo_arquivo = os.path.join(pasta_convertidas, f'{nome}.jpg')
        print(f"💾 Salvando como: {novo_arquivo}")

        imagem.save(novo_arquivo, 'JPEG', quality=95)
        print(f"✅ Sucesso: {arquivo} convertido para JPG!")
        convertidos += 1

    except Exception as e:
        print(f"❌ ERRO ao tentar converter {arquivo}: {e}")

if convertidos == 0:
    print("\n⚠️ Nenhuma imagem foi convertida. Algo deu muito errado.")
else:
    print(f"\n🏁 {convertidos} imagens convertidas com sucesso! Arquivos salvos em: {pasta_convertidas}")
