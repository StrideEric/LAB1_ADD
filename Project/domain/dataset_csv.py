from domain.dataset import Dataset
import pandas as pd
import csv

class DatasetCSV(Dataset):
    def __init__(self, dataset_path: str):
        super().__init__(dataset_path)
        self.load_data()

    def detect_csv_dialect(self, file_path):
        with open(self.dataset_path, 'r', encoding='utf-8') as file: # Abre el archivo CSV en modo lectura
            first_line = file.readline() # Lee la primera línea del archivo para verificar si es un CSV válido
            if ';' in first_line:
                return ';'
            elif ',' in first_line:
                return ','
            else:
                return ';' # Si no se encuentra un delimitador válido, retorna una coma por defecto


    def load_data(self):
        try:
            #delimiter = self.detect_csv_dialect(self.dataset_path) # Detecta el delimitador del archivo CSV
            df = pd.read_csv(self.dataset_path, delimiter=';') # Carga el archivo CSV en un DataFrame de pandas
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
        
        self.data = pd.read_csv(self.dataset_path)
