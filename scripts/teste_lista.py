import os

pasta = r"C:\Users\guilh\Documents\Projetos\EBAC\Ayrton\assets"

print(f"Testando acesso direto a: {pasta}")
print(f"Existe? {os.path.exists(pasta)}")
print(f"Arquivos na pasta:")
print(os.listdir(pasta))
