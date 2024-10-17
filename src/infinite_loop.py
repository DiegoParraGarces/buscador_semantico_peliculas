from main_students import recomPeliculas #


def main():
    recomendacion = recomPeliculas('sentence-transformers/all-MiniLM-L6-v2', 'data/IMDB top 1000.csv')

    while True:
        query = input('Please enter a text for looking a movie or "end" to finish: ')
        if query.lower() == 'end':
            break
        recomendaciones = recomendacion.recomendar(query)
        print('Similar movies: \n', recomendaciones)


if __name__ == '__main__':
        main()