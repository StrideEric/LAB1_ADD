import os
from domain.dataset_csv import DatasetCSV
from domain.dataset_excel import DatasetExcel
from domain.dataset_api import DatasetAPI
from data.data_saver import DataSaver


# Mapeo de extensiones a clases para poder cargar diferentes tipos de datasets
EXTENSION_MAP = {
    ".csv": DatasetCSV,
    ".xlsx": DatasetExcel
    # Puedes agregar más extensiones y clases, si me da el tiempo lo hago xd
}

def cargar_datasets(files_path):
    datasets = [] # Lista para almacenar los datasets cargados
    for filename in os.listdir(files_path): # Recorre los archivos en el directorio especificado
        file_path = os.path.join(files_path, filename) # Obtiene la ruta completa del archivo
        _, ext = os.path.splitext(filename) # Obtiene la extensión del archivo
        ext = ext.lower() # Convierte la extensión a minúsculas para evitar problemas de mayúsculas/minúsculas

        if ext in EXTENSION_MAP: # Verifica si la extensión está en el mapeo, si no esta directamente no lo procesa
            dataset_class = EXTENSION_MAP[ext]
            try:
                print(f"\nCargando archivo: {filename}")
                dataset = dataset_class(file_path) # Crea una instancia de la clase correspondiente al tipo de archivo
                dataset.load_data()
                dataset.show_data()
                datasets.append((dataset, filename)) # Agrega el dataset a la lista de datasets cargados
            except Exception as e:
                print(f"Error al procesar {filename}: {e}")
        else:
            print(f"Tipo de archivo no soportado: {filename}")
            print(f"Por favor, utilice archivos {EXTENSION_MAP.keys()} para cargar los datasets.") 
    return datasets

def main():
    print("< < < < < INICIO DE LA APLICACIÓN > > > > >")

    files_path = os.path.join(os.path.dirname(__file__), "files")
    datasets = cargar_datasets(files_path)

    db = DataSaver()
    type_counters = {} 

    for dataset, filename in datasets:
        _, ext = os.path.splitext(filename)
        ext = ext.lower().replace('.', '')  # csv o xlsx o otras extensiones que se puedan agregar

        # contador para el manejo de multiples archivos con el mismo nombre
        count = type_counters.get(ext,0) + 1 # En type_counters se guarda el nombre del archivo y la cantidad de veces que se ha procesado
        type_counters[ext] = count # en caso de que en este ciclo se procese un archivo con el mismo nombre, se incrementa el contador

        table_name = f"archivo_{ext}_{count}" # se crea el nombre del archivo compuesto por la extension y el contador, para determinar el nombre de la tabla en la base de datos sin repetir nombres

        try:
            db.save_data(dataset.data, table_name)
            print(f"Datos guardados en la tabla: {table_name}")
        except Exception as e:
            print(f"No se pudieron guardar los datos de {filename}: {e}")

    print("\n< < < < < FIN DE LA APLICACIÓN > > > > >")


if __name__ == "__main__":
    main()
