import os
from PIL import Image

DATA_DIR = 'data/'

print("Convertendo e limpando todas as imagens para JPG padrão...")

convertidos = 0
erros = 0

for raiz, pastas, arquivos in os.walk(DATA_DIR):
    for nome in arquivos:
        caminho = os.path.join(raiz, nome)
        try:
            # Abre a imagem (não importa se é png, webp ou jpg bugado)
            with Image.open(caminho) as img:
                # Converte para RGB (remove transparências e perfis de cores estranhos)
                rgb_img = img.convert('RGB')
                
                # Salva por cima como um JPG legítimo
                # Se quiser manter a extensão original, pode, mas o conteúdo será JPG
                novo_nome = os.path.splitext(caminho)[0] + ".jpg"
                
                # Se o arquivo original não era .jpg, removemos o antigo depois
                rgb_img.save(novo_nome, "JPEG")
                
                if caminho != novo_nome:
                    os.remove(caminho)
                
                convertidos += 1
                if convertidos % 100 == 0:
                    print(f"{convertidos} imagens processadas...")

        except Exception as e:
            print(f"[-] Não deu para salvar o arquivo {nome}: {e}")
            try:
                os.remove(caminho) # Se nem a PIL abre, o arquivo é lixo eletrônico
                erros += 1
            except:
                pass

print(f"\nPronto! {convertidos} imagens agora são JPGs legítimos.")
print(f"{erros} arquivos eram impossíveis de recuperar e foram apagados.")