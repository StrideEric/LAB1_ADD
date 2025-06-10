from domain.dataset import Dataset
import pandas as pd

class DatasetExcel(Dataset):
    def __init__(self, dataset_path: str):
        super().__init__(dataset_path)
        self.load_data()

    def load_data(self):
        try:
            df = pd.read_excel(self.dataset_path) # convierte el archivo CSV en un DataFrame de pandas
            self.data= df # asigna el DataFrame a la variable de instancia
            print(f"Datos cargados correctamente desde {self.dataset_path}.") # imprime un mensaje de éxito
            
            self.preprocess_data() # llama al método de preprocesamiento de datos
            
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo {self.dataset_path} no se encuentra.") # si no se encuentra el archivo, lanza una excepción
        except pd.errors.InvalidIndexError:
            raise ValueError(f"El archivo {self.dataset_path} tiene un índice inválido.") # si el índice del archivo CSV es inválido, lanza una excepción
        except pd.errors.DtypeWarning:
            raise ValueError(f"El archivo {self.dataset_path} tiene un tipo de dato no válido.") # si el tipo de dato del archivo CSV es inválido, lanza una excepción
        except pd.errors.EmptyDataError:
            raise ValueError(f"El archivo {self.dataset_path} está vacío.") # si el archivo CSV está vacío, lanza una excepción
        except pd.errors.ParserError:
            raise ValueError(f"Error al analizar el archivo {self.dataset_path}. Asegúrese de que el formato sea correcto.") # si hay un error al analizar el archivo CSV, lanza una excepción
        except Exception as e:
            raise Exception(f"Error al cargar el archivo {self.dataset_path}: {e}") # maneja cualquier otro error inesperado
        
        self.data = pd.read_excel(self.dataset_path)