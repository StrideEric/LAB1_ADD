import requests
import pandas as pd
from domain.dataset import Dataset

class DatasetAPI(Dataset):
    def __init__(self, dataset_path: str):
        super().__init__(dataset_path)
        self.load_data()

    def load_data(self):
        try:
            response = requests.get(self.dataset_path)  # Realiza una solicitud GET a la API
            if response.status_code == 200:
                df = pd.json_normalize(response.json())  # Convierte la respuesta JSON en un DataFrame de pandas
                def is_list(x): # Verifica si un elemento es una lista
                    return isinstance(x, list)
                def list_to_string(x): # Convierte listas en cadenas de texto
                    if isinstance(x, list):
                        return ', '.join(map(str, x))

                for col in df.columns:
                    if df[col].apply(is_list).any():
                        df[col] = df[col].apply(list_to_string)
                
                self.data = df  # Asigna el DataFrame a la variable de instancia
                print(f"Datos cargados correctamente desde la API {self.dataset_path}.")  # Imprime un mensaje de éxito
                self.preprocess_data()  # Llama al método de preprocesamiento de datos
            else:
                raise ValueError(f"Error al cargar los datos desde la API: {response.status_code} - {response.text}")

        except Exception as e:
            raise Exception(f"Error al cargar el dataset desde la API: {e}")