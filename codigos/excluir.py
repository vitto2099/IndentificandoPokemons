import os

# Lista expandida focada em formatos de web e animação
FORMATOS_PARA_DELETAR = {
    '.webp', '.gif', 
    '.jfif', '.bmp', '.tiff', '.ico', '.webrip'
}

def limpar_arquivos_visuais():
    diretorio_base = os.getcwd()
    removidos = 0
    
    print(f"--- Iniciando limpeza em: {diretorio_base} ---")

    for raiz, pastas, arquivos in os.walk(diretorio_base):
        # Protege a pasta do Git
        if '.git' in pastas:
            pastas.remove('.git')
            
        for arquivo in arquivos:
            extensao = os.path.splitext(arquivo)[1].lower()
            
            if extensao in FORMATOS_PARA_DELETAR:
                caminho = os.path.join(raiz, arquivo)
                try:
                    os.remove(caminho)
                    print(f"[-] Removido: {arquivo}")
                    removidos += 1
                except Exception as e:
                    print(f"[!] Erro ao deletar {arquivo}: {e}")

    print(f"\n========================================")
    print(f"Limpeza concluída! {removidos} arquivos removidos.")
    print(f"========================================\n")

if __name__ == "__main__":
    limpar_arquivos_visuais()