html = '''
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Galeria Ayrton Senna</title>
    <style>
        body { background-color: #111; color: white; font-family: Arial, sans-serif; }
        .galeria { display: grid; grid-template-columns: repeat(5, 1fr); gap: 10px; }
        .foto { position: relative; }
        .foto img { width: 100%; border-radius: 5px; }
        .hover-text {
            position: absolute; bottom: 0; left: 0; right: 0;
            background: rgba(0,0,0,0.7); color: #FFD700;
            text-align: center; padding: 5px; opacity: 0;
            transition: opacity 0.3s ease;
        }
        .foto:hover .hover-text { opacity: 1; }
    </style>
</head>
<body>
    <h1 style="text-align: center; color: #FF3131;">Galeria de Imagens</h1>
    <div class="galeria">
'''

for i in range(1, 11):
    html += f'''
        <div class="foto">
            <a href="pages/curiosidade{i}.html">
                <img src="assets/Ayrton{i}.jpg" alt="Curiosidade {i}">
                <div class="hover-text">Curiosidade {i}</div>
            </a>
        </div>
    '''

html += '''
    </div>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Index restaurado!")
