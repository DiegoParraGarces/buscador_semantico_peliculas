import pandas as pd
from sentence_transformers import SentenceTransformer, util


class recomPeliculas:
     def __init__(self, modelo, data_route):
          self.modelo = SentenceTransformer(modelo)
          self.df = pd.read_csv(data_route)
          self._prepara_data() #


     def _prepara_data(self):
           # Crear nueva columna concatenando descripción e información y generar los embeddings con esta columna creada
           self.df['votes'] = self.df['Description'] + ' ' + self.df['Info']
           embeddings = self.modelo.encode(self.df['votes'].tolist(), batch_size=64,show_progress_bar=True)
           self.df['embeddings'] = embeddings.tolist()   


     def recomendar(self, query):
              # Recomendar películas según la búsqueda semánticarealizada
              query_embedding = self.modelo.encode([query])[0]
              self.df['similarity'] = self.df['embeddings'].apply(lambda x: self._compute_similarity(x, query_embedding))
              recomendaciones = self.df.sort_values(by='similarity', ascending=False)
              return recomendaciones[['Title', 'similarity']].drop_duplicates()
     
     
     def _compute_similarity(self, embedding, query_embedding):
           #calcular similitud entre embeddings
           return util.cos_sim(embedding, query_embedding).item()
         
            
