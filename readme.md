# 📱 Identificador de Pokémon (Pokédex)

Este projeto é uma **Pokédex** simples que utiliza uma rede neural convolucional (CNN) para identificar 10 tipos diferentes de Pokémon a partir de imagens.

## 🚀 Funcionalidades

*   **Treinamento:** Um script para treinar o modelo com novas imagens.
*   **Interface Gráfica:** Uma interface amigável construída com `Tkinter`.
*   **Identificação:** Reconhece Pokémon com base no modelo treinado e exibe informações sobre eles.
*   **Confiança:** Exibe a porcentagem de confiança da predição da IA.

## 👾 Pokémon Suportados

Atualmente, o modelo consegue identificar os seguintes Pokémon:
*   Chansey
*   Cubone
*   Exeggcute
*   Gengar
*   Hitmonlee
*   Horsea
*   Onix
*   Staryu
*   Tangela
*   Voltorb

## 🛠️ Tecnologias Utilizadas

*   **Python 3**
*   **TensorFlow/Keras** (Redes Neurais)
*   **Pillow** (Processamento de Imagem)
*   **Tkinter** (Interface Gráfica)
*   **NumPy** (Operações Matemáticas)

## 📁 Estrutura do Projeto

*   `treino.py`: Script responsável por criar e treinar a rede neural.
*   `pokedex.py`: O aplicativo principal com interface gráfica.
*   `pokemon.h5`: Arquivo do modelo já treinado.
*   `Pokemons/`: Pasta contendo o dataset de imagens para treinamento.

## 📖 Como Usar

1.  **Instale as dependências:**
    ```bash
    pip install tensorflow pillow numpy
    ```

2.  **Para rodar a Pokédex:**
    ```bash
    python pokedex.py
    ```
    Clique no botão "QUAL O SEU POKEMON!!!", selecione uma imagem de um dos Pokémon suportados e veja o resultado!

3.  **Para treinar o modelo novamente:**
    ```bash
    python treino.py
    ```

---
Desenvolvido por vitto2099.
