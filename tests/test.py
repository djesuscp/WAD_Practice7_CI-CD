import unittest
from src.app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Crea un cliente de prueba usando la aplicación Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Envía una solicitud GET a la ruta '/'
        result = self.app.get('/')
        
        # Verifica que la respuesta sea "Hello, World!"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Hello, World!")

    def test_correct(self):
        # Envía solicitud GET a la ruta '/correct'
        result = self.app.get('/correct')

        # Verifica que la respuesta sea "Everything is correct!"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Everything is correct!")

    def test_wrong(self):
        # Envía solicitud GET a la ruta '/correct'
        result = self.app.get('/wrong')

        # Verifica que la respuesta sea "Something went wrong!"
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode(), "Something went wrong!")


if __name__ == "__main__":
    unittest.main()