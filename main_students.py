import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Cargar modelo
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def main(query):
    df = pd.read_csv('./IMDB top 1000.csv')
    # print(df.head())
    # TODO: Completar esta función para realizar búsquedas semánticas con base en el código del archivo test.ipynb
    
    # Crear nueva columna concatenando descripción e información y generar los embeddings con esta columna creada
    df['Votes'] = df['Description'] + ' ' + df['Info']
    embeddings = model.encode(df['Votes'],batch_size=64,show_progress_bar=True)
    df['embeddings'] = embeddings.tolist()

    #aplicar modelo y generar nueva columna con la similaridad y organizar de manera descendente
    query_embedding = model.encode([query])[0]
    df['similarity'] = df.apply(lambda x: compute_similarity(x, query_embedding), axis=1)
    df = df.sort_values(by='similarity', ascending=False)
    print('Similar movies: \n')
    print(df['Title'].drop_duplicates())


def compute_similarity(example, query_embedding):
    embedding = example['embeddings']
    similarity = util.cos_sim(embedding, query_embedding).item()
    return similarity



if __name__ == '__main__':
    
    while True:
        query = input('Please enter a text for looking a movie or "end" to finish: ')
        if query.lower() == 'end':
            break
        main(query)