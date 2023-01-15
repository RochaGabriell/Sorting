from models.bubbleSort import BubbleSort
from models.insertionSort import InsertionSort

import streamlit as st
from random import randrange
import time

# Decorador de funções para memorizar execuções de funções.
# Os dados memorizados são armazenados na forma "em conserva", o que significa que o retorno o valor de uma função memorizada deve ser selecionável.
# Cada chamador de uma função memorizada recebe sua própria cópia dos dados em cache.
@st.experimental_memo
def random():
    lista = []
    for i in range(randrange(5, 15)): # Sortear o tamanho da lista
        aux = randrange(0, 100) # Sortear os valores da lista
        lista.append({aux: aux})
    return lista

# Widgets de barra lateral
# Os elementos são passados ​​para "st.sidebar" usando a notação "with"
with st.sidebar:
    # Widget de seleção
    option = st.selectbox(
        "Escolha o algoritmos de ordenação e busca:", 
        ["Bubble Sort", "Insertion Sort", "Quick Sort", "Merge Sort"]
        )

    # Widget do botão de opção
    ordenado = st.radio(
        "Ordenado:",
        ["Aleatório", "Crescente", "Decrescente"], 
        horizontal=False
        )

    # Widget de entrada de texto
    create_list = st.text_input("Create list:")
    st.write("Ex: 1, 2, 3, 4, 5")

    # Widget do botão
    clicked_random = st.button("Random")

    # Widget deslizante, responsavel por controlar o tempo de transação entre animação
    velocity = st.slider(
        "Velocidade de Reprodição:",
        0, 5, 1
    )

    st.write(f"Velocidade: {velocity}s")

    start = st.button("Iníciar Simulação")


# Exibir o texto no formato de títulos
st.title(f"{option.upper()}", anchor=None)


# Verifica sem tem dados digitados pelo usuário, se estiver, ele cria uma lista com esses dados
if create_list:
    lista = list(map(int, create_list.split(", ")))
    aux = []
    for i in lista:
        aux.append({i: i})
    lista = aux

# Verifica se foi selecionado a opção "Crescente", se estiver, ele ordena a lista aleatória gerada
elif ordenado == "Crescente":
    lista = random()
    aux = []

    for i in lista:
        for key, value in i.items():
            aux.append(key)
    
    aux.sort(reverse=False)
    
    lista.clear()
    
    for i in aux:
        lista.append({i: i})

# Verifica se foi selecionado a opção "Decrescente", se estiver, ele ordena a lista aleatória gerada    
elif ordenado == "Decrescente":
    lista = random()
    aux = []

    for i in lista:
        for key, value in i.items():
            aux.append(key)
    
    aux.sort(reverse=True)
    
    lista.clear()
    
    for i in aux:
        lista.append({i: i})

else:
    lista = random()

# Sempre que o botão for acionado, ele entregara uma nova lista randômica
if clicked_random:
    random.clear() # Limpar o cache de uma função memorizada 
    lista.clear()
    lista = random()

# Cria um gráfico de barras com base na lista informada
graphic = st.bar_chart(
    data=lista,
    height=400, 
    use_container_width=True
    )

if start:
    # Limpe os elementos do gráfico
    graphic.empty()

    if option == "Bubble Sort":
        bubble = BubbleSort(lista, velocity)
        bubble.sort()
        bubble.code()

    elif option == "Insertion Sort":
        st.title("AGUARDE! EM BREVE")

        # insertion = InsertionSort(lista, velocity)
        # insertion.sort()
        # insertion.code()
    
    elif option == "Quick Sort":
        st.title("AGUARDE! EM BREVE")

    elif option == "Merge Sort":
        st.title("AGUARDE! EM BREVE")