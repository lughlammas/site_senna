import os
import csv

# Caminho da pasta onde estão as páginas
pasta_pages = 'pages'
arquivo_csv = 'conteudo.csv'

# Lê o CSV e monta uma lista de capítulos e descrições
conteudos = []
with open(arquivo_csv, encoding='utf-8') as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        conteudos.append(linha)

# Para cada arquivo HTML na pasta pages, insere o conteúdo certo
for arquivo in os.listdir(pasta_pages):
    caminho_arquivo = os.path.join(pasta_pages, arquivo)

    # Descobre qual capítulo corresponde a esse arquivo
    capitulo = None
    for item in conteudos:
        if item['capitulo'] in arquivo:
            capitulo = item
            break

    if not capitulo:
        print(f'⚠️ Nenhuma descrição encontrada para {arquivo}')
        continue

    # Cria um conteúdo HTML básico para cada página
    conteudo_html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <title>{capitulo['capitulo']}</title>
        <link rel="stylesheet" href="../css/style.css">
    </head>
    <body>
        <header>
            <h1>{capitulo['capitulo']}</h1>
        </header>
        <main>
            <p>{capitulo['descricao']}</p>
        </main>
        <footer>
            <a href="../index.html">Voltar à galeria</a>
        </footer>
    </body>
    </html>
    """

    # Sobrescreve o arquivo HTML com o conteúdo novo
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo_html)

    print(f'✅ Atualizado: {arquivo}')

print("\n🎉 Todas as páginas foram preenchidas com sucesso!")
