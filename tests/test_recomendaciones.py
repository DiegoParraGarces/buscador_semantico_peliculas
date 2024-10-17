import unittest
import sys
import os
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../semantic_search/src')))

from main_students import recomPeliculas

class TestMovieRecommender(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.recomendacion = recomPeliculas('sentence-transformers/all-MiniLM-L6-v2', 'data/IMDB top 1000.csv')

    def test_recomendacion(self):
        result = self.recomendacion.recomendar("crime")
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertTrue('Title' in result.columns)
        self.assertTrue('similarity' in result.columns)

    def test_similarity_computation(self):
        embedding1 = self.recomendacion.df['embeddings'].iloc[0]
        embedding2 = self.recomendacion.df['embeddings'].iloc[1]
        similarity = self.recomendacion._compute_similarity(embedding1, embedding2)
        self.assertGreaterEqual(similarity, 0)  # La similitud debe ser >= 0

if __name__ == '__main__':
    unittest.main()        