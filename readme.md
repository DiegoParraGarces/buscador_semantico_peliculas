
<h1 align="center"> BUSCADOR DE PELÍCULAS SEMÁNTICO </h1>


# Descripción

Con este buscador semántico, podrás realizar búsquedas de películas ingresando una palabra o frase, este buscador te recomendará varias opciones de películas que estén relacionadas en contexto según tu búsqueda haciendo uso del NLP o procesamiento del lenguaje natural y en base al dataset de kaggle.com denominado como "IMDB top 1000".  


# Instalación y uso

Incialmente debes tener en tu PC lo siguiente:
Python 3.10 o superior
Gitbash
virtualenv

- clonar proyecto
    git clone https://github.com/DiegoParraGarces/buscador_semantico_peliculas.git --- comando en consola

- Acceder a ubicación del proyecto
    cd 'url carpeta' --- comando en consola    

- Crear y activar ambiente virtual
    python -m venv venv           --- comando en consola
    source venv/Scripts/activate  --- comando en consola

- Instalación librerías
    pip install -r requirements.txt  --- comando en consola

- Iniciar ejecución proyecto
    python main_students.py  --- comando en consola


Una vez se ejecuta el archivo .py se te indicará el siguiente texto:
" Please enter a text for looking a movie or "end" to finish: ", es allí donde debes ingesar la palabra u oración y teclear enter para realizar la búsqueda, por consola podrás observar los resultados de las películas relacionadas según tu búsqueda y de nuevo aparecerá el texto para otra búsqueda, en caso de no querer continuar debes ingresar la palabra end para finalizar.


# Librerías

| Pandas   | sentence_transformers     |


# Autor

Diego Alexander Parra Garcés
2245281
UAO




