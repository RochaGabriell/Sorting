import streamlit as st
import time

class BubbleSort:

    def __init__(self, lista: list, velocity: int) -> None:

        self.lista = lista
        self.velocity = velocity


    def sort(self) -> None:

        troca = False

        for n in range(len(self.lista)-1, 0, -1):
            for i in range(n):

                graphic = st.bar_chart(
                        data=self.lista,
                        height=400, 
                        use_container_width=True
                        )

                title = st.title(f"{list(self.lista[i].keys())} > {list(self.lista[i + 1].keys())} = {list(self.lista[i].keys()) > list(self.lista[i + 1].keys())}", anchor=None)            

                time.sleep(self.velocity) # Controla o tempo de uma execução pra outra

                title.empty() # Limpe os elementos do título
                graphic.empty() # Limpe os elementos do gráfico
                
                if list(self.lista[i].keys()) > list(self.lista[i + 1].keys()): # Pegando apenas a key do dict, para fazer a comparação

                    troca = True
                    self.lista[i], self.lista[i + 1] = self.lista[i + 1], self.lista[i]       

            if not troca:
                graphic = st.bar_chart(
                        data=self.lista,
                        height=400, 
                        use_container_width=True
                        )
                title = st.title("A lista já está ordenada")

                return

        graphic = st.bar_chart(
                        data=self.lista,
                        height=400, 
                        use_container_width=True
                        )
    

    def code(self) -> None:
        
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
        # Exiba um bloco de código com a sintaxe do Python
        st.code(code, language='python')