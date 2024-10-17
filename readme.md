
<h1 align="center"> BUSCADOR DE PELÍCULAS SEMÁNTICO </h1>


# Descripción

Con este buscador semántico, podrás realizar búsquedas de películas ingresando una palabra o frase, este buscador te recomendará varias opciones de películas que estén relacionadas en contexto según tu búsqueda haciendo uso del NLP o procesamiento del lenguaje natural y en base al dataset de kaggle.com denominado como "IMDB top 1000".  


# Instalación y uso

Incialmente debes tener en tu PC lo siguiente:
Python 3.10 o superior
Gitbash
virtualenv
Docker desktop

Desde tu editor de código de preferencia: 
- clonar proyecto<br>
    git clone 
    https://github.com/DiegoParraGarces/buscador_semantico_peliculas.git --- comando en consola

- Acceder a ubicación del proyecto<br>
    cd 'url carpeta' --- comando en consola    


- Iniciar ejecución proyecto<br>
    docker build -t nombre_archivo .<br><br>

    docker run -it nombre_archivo<br>


Una vez se ejecuta el dockerfile se te indicará el siguiente texto:
" Please enter a text for looking a movie or "end" to finish: ", es allí donde debes ingesar la palabra u oración y teclear enter para realizar la búsqueda, por consola podrás observar los resultados de las películas relacionadas según tu búsqueda y de nuevo aparecerá el texto para otra búsqueda, en caso de no querer continuar debes ingresar la palabra end para finalizar.

# Realizar test

- Ubicarse en la carpeta del proyecto<br><br>

- Habilitar ambiente virtual<br>
$ source semantic_search/venv/Scripts/activate

- Ejecutar instalación de liberías<br>
$ pip install -r requirements.txt

- Ejecutar por terminal pruebas unittest<br>
$ python -m unittest discover -s tests

- Ejecutar por terminal el coverage<br>
$ python -m coverage run -m unittest discover -s tests

- Generar reporte coverage<br>
$ python -m coverage report



# Librerías

| Pandas   | sentence_transformers   |
| Especificadas en requirements.txt



# Principios SOLID

Se creó la clase para manejar la lógica de recomendación manteniendo las responsabilidades separadas -- Single Responsability

la clase es extensible para agregar nuevas funcionalidades -- Open closed


# Autor

Diego Alexander Parra Garcés<br>
2245281<br>
UAO

