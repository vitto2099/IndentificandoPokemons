import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import tensorflow as tf
import numpy as np

IMG_SIZE = (64, 64) 
class_names = ["Chansey", "Cubone", "Exeggcute", "Gengar", "Hitmonlee", 
               "Horsea", "Onix", "Staryu", "Tangela", "Voltorb"]

INFO_POKEMON = {
    "Chansey": "Tipo: Normal\nUma criatura gentil que carrega um ovo nutritivo e adora ajudar os feridos.",
    "Cubone": "Tipo: Terra\nUsa o crânio de sua mãe como capacete. Suas manchas de choro são visíveis no osso.",
    "Exeggcute": "Tipo: Planta/Psíquico\nSeis ovos que se comunicam por telepatia. Se um se quebra, os outros sobrevivem.",
    "Gengar": "Tipo: Fantasma/Veneno\nEsconde-se nas sombras das cidades à noite para roubar o calor dos passantes.",
    "Hitmonlee": "Tipo: Lutador\nConhecido como o mestre dos chutes. Suas pernas esticam como molas para golpear.",
    "Horsea": "Tipo: Água\nUm cavalo-marinho que cospe tinta preta para confundir predadores e escapar.",
    "Onix": "Tipo: Pedra/Terra\nUma serpente de pedra gigante que cava túneis a 80 km/h sob a terra.",
    "Staryu": "Tipo: Água\nSeu núcleo central brilha em vermelho. Pode regenerar qualquer parte do corpo perdida.",
    "Tangela": "Tipo: Planta\nO corpo é oculto por vinhas azuis que nunca param de crescer e balançar.",
    "Voltorb": "Tipo: Elétrico\nIdentico a uma Pokébola. É extremamente perigoso pois explode ao menor contato."
}

model = None

def abrir_e_identificar():
    global model
    if model is None:
        lbl_info.config(text="Carregando ")
        janela.update()
        model = tf.keras.models.load_model('pokemon.h5')
        lbl_info.config(text="Carregado!")

    caminho = filedialog.askopenfilename()
    if caminho:
        try:
            img_original = Image.open(caminho)
            img_exibir = img_original.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img_exibir)
            lbl_img.config(image=img_tk)
            lbl_img.image = img_tk

            img_ia = img_original.convert('RGB').resize(IMG_SIZE)
            img_array = np.array(img_ia) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            predicao = model.predict(img_array, verbose=0)
            indice = np.argmax(predicao)
            nome = class_names[indice]
            confianca = predicao[0][indice] * 100
            
            lbl_nome.config(text=nome.upper())
            lbl_confianca.config(text=f"Confiança: {confianca:.2f}%")
            lbl_info.config(text=INFO_POKEMON[nome])
        except Exception as e:
            lbl_nome.config(text="Erro")
            lbl_confianca.config(text="")
            print(f"Erro na identificação: {e}")

janela = tk.Tk()
janela.title("Pokédex")
janela.configure(bg="#CC0000")

largura = 800
altura = 750
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")

container = tk.Frame(janela, bg="#CC0000")
container.pack(expand=True)

tk.Label(container, text="POKÉDEX", font=("Arial", 30, "bold"), bg="#CC0000", fg="white").pack(pady=20)

btn_procurar = tk.Button(
    container, text="🔍 QUAL O SEU POKEMON!!! ", 
    command=abrir_e_identificar,
    font=("Arial", 16, "bold"), bg="#3B4CCA", fg="white", 
    padx=30, pady=20, cursor="hand2"
)
btn_procurar.pack(pady=20)

moldura = tk.Frame(container, bg="black", bd=5)
moldura.pack(pady=10)
lbl_img = tk.Label(moldura, bg="#333", width=300, height=300)
lbl_img.pack()

lbl_nome = tk.Label(container, text="AGUARDANDO", font=("Arial", 25, "bold"), bg="#CC0000", fg="#FFCC00")
lbl_nome.pack(pady=5)

lbl_confianca = tk.Label(container, text="", font=("Arial", 14, "bold"), bg="#CC0000", fg="white")
lbl_confianca.pack(pady=5)

lbl_info = tk.Label(container, text="Selecione um arquivo", font=("Arial", 12), bg="#CC0000", fg="white", wraplength=500, justify="center")
lbl_info.pack(pady=10)

janela.mainloop()