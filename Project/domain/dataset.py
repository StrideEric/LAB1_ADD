from abc import ABC, abstractmethod


class Dataset(ABC):
    def __init__(self, dataset_path: str):
        self.dataset_path = dataset_path # Path to the dataset	idem a self.__fuente = fuente
        self.__data = None


    @property # Getter para poder acceder al dataset
    def data(self):
        return self.__data
    
    @data.setter # Setter para poder asignar el dataset
    def data(self, value):
        self.__data = value

    @property
    def dataset_path(self):
        return self.__dataset_path
    
    @dataset_path.setter
    def dataset_path(self, value):
        self.__dataset_path = value

    
    @abstractmethod # Obliga a las clases hijas a implementar este método
    def load_data(self):

        pass

    def preprocess_data(self):


        # validaciones de los datos
        #if self.data is None:
        #    raise ValueError("data no cargada. Por favor, cargue los datos primero.")
        
        #if self.data.empty:
        #    raise ValueError("data está vacía. Por favor, cargue un dataset válido.")
        
        #if self.data.isnull().values.any() or self.data.isnull().sum().sum() > 0:
        #    raise ValueError("data contiene valores nulos. Por favor, procese los datos para eliminar o imputar los valores nulos.")

        #if self.data.duplicated().sum() > 0:
        #    raise ValueError("data contiene filas duplicadas. Por favor, procese los datos para eliminar las filas duplicadas.")

        #if not isinstance(self.data, (list, dict)):
        #    raise TypeError("data debe ser una lista o un diccionario. Por favor, cargue un dataset válido.")
        
        # procesamiento de los datos
        if self.data is not None:
            self.__data.columns = self.data.columns.str.lower().str.replace(' ', '_')  # Normaliza los nombres de las columnas
            self.__data = self.data.drop_duplicates()  # Elimina filas duplicadas
            for col in self.data.select_dtypes(include = "object").columns:
                self.__data[col] = self.data[col].astype(str).str.strip()  # Elimina espacios en blanco al inicio y al final de los valores de tipo string
            print("Datos preprocesados correctamente.")
        else:
            raise ValueError("Datos no cargados. Por favor, cargue los datos primero.")
        

        return True

    def get_data(self):
        pass

    def show_data(self):
        return print(self.data.describe(include="all")) if self.data is not None else print("No hay datos para mostrar.")