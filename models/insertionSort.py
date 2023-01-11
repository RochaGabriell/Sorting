import streamlit as st
import time

class InsertionSort:
    def __init__(self, lista: list, velocity: int) -> None:
        self.lista = lista
        self.velocity = velocity

    def sort(self) -> None:

        for i in range(1, len(self.lista)):
            
            key_item = list(self.lista[i].keys())

            j = i - 1

            while j >= 0 and list(self.lista[j].keys()) > key_item:

                graphic = st.bar_chart(
                    data=self.lista,
                    height=400, 
                    use_container_width=True
                    )

                col1, col2 = st.columns(2)
                
                with col1:
                    title_key_item = st.title(f"Key - {key_item}")
                    
                with col2:
                    title = st.title(f"{list(self.lista[j].keys())} > {key_item} - {list(self.lista[j].keys()) > key_item}")

                time.sleep(self.velocity)

                title_key_item.empty()
                title.empty()
                graphic.empty()

                self.lista[j+1] = self.lista[j]
                j -= 1

            self.lista[j+1] = {key_item[0]: key_item[0]}

        graphic = st.bar_chart(
                    data=self.lista,
                    height=400, 
                    use_container_width=True
                    )

    def code(self) -> None:
        
        code = """
def insertion_sort(array):
    for i in range(1, len(array)):

        key_item = array[i]

        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array
        """

        st.code(code, language='python')