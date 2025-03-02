import os

# Caminho da pasta 'pages'
pasta = 'pages'

# Novos nomes com títulos completos
novos_nomes = [
    "1 - O Kart de Lata que Virou Lenda.html",
    "2 - Primeira Vitória na F1 — Estoril 1985.html",
    "3 - A Magia na Chuva — Donington 1993.html",
    "4 - A Volta Perfeita em Mônaco.html",
    "5 - Senna e Prost — Guerra de Gigantes.html",
    "6 - Brasil em Lágrimas — Interlagos 1991.html",
    "7 - Ayrton Off-Track — O Homem por Trás do Mito.html",
    "8 - O Capacete Amarelo — Símbolo Imortal.html",
    "9 - O Último Ato — Imola 1994.html",
    "10 - O Legado Inquebrável.html"
]

# Arquivos atuais (ordenados pelo número no nome)
arquivos = [f"curiosidade{i}.html" for i in range(1, 11)]

# Renomear cada um na ordem certa
for indice, arquivo in enumerate(arquivos):
    antigo_path = os.path.join(pasta, arquivo)
    novo_path = os.path.join(pasta, novos_nomes[indice])
    os.rename(antigo_path, novo_path)

print("✅ Arquivos renomeados com sucesso!")
