import streamlit as st
from random import randrange
import time

@st.experimental_memo
def random():
    lista = []
    for i in range(randrange(5, 15)):
        aux = randrange(0, 100)
        lista.append({aux: aux})
    return lista


with st.sidebar:
    option = st.selectbox(
        "Escolha o algoritmos de ordenação e busca:", 
        ["Bubble Sort", "Insertion Sort", "Quick Sort", "Merge Sort"]
        )

    ordenado = st.radio(
        "Ordenado:",
        ["Aleatório", "Crescente", "Decrescente"], 
        horizontal=False
        )

    create_list = st.text_input("Create list:")
    st.write("Ex: 1, 2, 3, 4, 5")

    clicked_random = st.button("Random")

    velocity = st.slider(
        "Velocidade de Reprodição:",
        0, 5, 1
    )

    st.write(f"Velocidade: {velocity}s")

    start = st.button("Iníciar Simulação")



st.title(f"{option.upper()}", anchor=None)



if create_list:
    lista = list(map(int, create_list.split(", ")))
    aux = []
    for i in lista:
        aux.append({i: i})
    lista = aux

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


if clicked_random:
    random.clear()
    lista.clear()
    lista = random()


graphic = st.bar_chart(
    data=lista,
    height=400, 
    use_container_width=True
    )


def bubblesort(lista):
    troca = False

    for n in range(len(lista)-1, 0, -1):
        for i in range(n):

            graphic = st.bar_chart(
                    data=lista,
                    height=400, 
                    use_container_width=True
                    )

            title = st.title(f"{list(lista[i].keys())} > {list(lista[i + 1].keys())} = {list(lista[i].keys()) > list(lista[i + 1].keys())}", anchor=None)            

            time.sleep(velocity)

            title.empty()
            graphic.empty()
            
            if list(lista[i].keys()) > list(lista[i + 1].keys()):

                troca = True
                lista[i], lista[i + 1] = lista[i + 1], lista[i]       

        if not troca:
            graphic = st.bar_chart(
                    data=lista,
                    height=400, 
                    use_container_width=True
                    )
            title = st.title("A lista já está ordenada")

            return

    graphic = st.bar_chart(
                    data=lista,
                    height=400, 
                    use_container_width=True
                    )


if start:
    graphic.empty()

    if option == "Bubble Sort":
        bubblesort(lista)

    elif option == "Insertion Sort":
        pass
    
    elif option == "Quick Sort":
        pass

    elif option == "Merge Sort":
        pass


code = '''
def bubblesort(lista = lista):
    troca = False
    for n in range(len(lista)-1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                troca = True
                lista[i], lista[i + 1] = lista[i + 1], lista[i]       
        if not troca:
            return
'''
    
st.code(code, language='python')