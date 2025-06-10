
import pandas as pd
import os

from sqlalchemy import create_engine # Para crear la conexión a la base de datos
from sqlalchemy.exc import SQLAlchemyError # Para manejar errores de SQLAlchemy
from decouple import config # Para cargar las variables de entorno desde un archivo .env


class DataSaver:
    def __init__(self): #,db_path):
        #self.__db_path = db_path # utilizado con sqlite
        #carpeta = os.path.dirname(db_path)
        #if carpeta and not os.path.exists(carpeta):
        #    os.makedirs(carpeta, exist_ok=True)  # Crea la carpeta si no existe
        user = config('DB_USER')
        password = config('DB_PASSWORD')
        host = config('DB_HOST')
        port = config('DB_PORT')
        database = config('DB_NAME')

        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(url, echo=False)  # Crea el motor de conexión a la base de datos con MySQL


    def save_data(self, df, table_name):
        if df is None:
            #raise ValueError("El DataFrame está vacío o no se ha proporcionado.")
            print("El DataFrame está vacío o no se ha proporcionado. No se guardarán datos.")
            return

        if not isinstance(df, pd.DataFrame):
            #raise TypeError("El objeto proporcionado no es un DataFrame de pandas. Se recibio: {}".format(type(df)))
            print(f"El objeto proporcionado no es un DataFrame de pandas. Se recibió: {type(df)}")
            return

        try:
            #conn = sqlite3.connect(self.__db_path)  # Conecta a la base de datos SQLite
            #df.to_sql(table_name, conn, if_exists='replace', index=False)  # Guarda el DataFrame en la tabla especificada
            #conn.commit()  # Confirma los cambios
            #conn.close()  # Cierra la conexión a la base de datos
            df.to_sql(table_name, con=self.engine, if_exists='replace', index=False)  # Guarda el DataFrame en la tabla especificada
            print(f"Datos guardados correctamente en la tabla '{table_name}' de la base de datos.")
            
        except SQLAlchemyError as e:
            print(f"Error al guardar los datos en la base de datos: {e}")
            return
        #except Exception as e:
            #raise Exception(f"Error al guardar los datos en la base de datos: {e}")
            #print(f"Error al guardar los datos en la base de datos: {e}")
            #return