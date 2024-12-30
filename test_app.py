import unittest
from app import app, db, SumResult

class TestSumResults(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://example_sum_postgres_2moj_user:lcOZ8DlDUF3Mu2ZnQLm3Xcq9AGnqlJFk@dpg-ctpfkrrqf0us73ebldcg-a.ohio-postgres.render.com/example_sum_postgres_2moje'
        self.app = app.test_client()

        # Create application context
        self.app_context = app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

        # Pop the application context
        self.app_context.pop()

    def test_get_sums_by_result_valid(self):
        sum_result = SumResult(a=1, b=3, result=4)
        db.session.add(sum_result)
        db.session.commit()
        response = self.app.get('/sum/result/4')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'1', response.data)
        self.assertIn(b'3', response.data)
        self.assertIn(b'4', response.data)

    def test_get_sums_by_result_invalid(self):
        response = self.app.get('/sum/result/999')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'No sums found with the specified result', response.data)

if __name__ == '__main__':
    unittest.main()
