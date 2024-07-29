import unittest
from app import app, db
from models import User

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Setup the database
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_user(self):
        response = self.app.post('/users', json={
            'first_name': 'Sourabh',
            'last_name': 'Salokhe',
            'account_number': '12345',
            'email': 'ss@gmail.com',
            'birth_date': '2000-01-01'
        })
        self.assertEqual(response.status_code, 201)

    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_account_number(self):
        self.app.post('/users', json={
            'first_name': 'Sourabh',
            'last_name': 'Salokhe',
            'account_number': '12345',
            'email': 'ss@gmail.com',
            'birth_date': '2000-01-01'
        })
        response = self.app.get('/users/12345')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
