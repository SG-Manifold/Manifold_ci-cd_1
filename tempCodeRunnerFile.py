    # def test_register(self):
    #     data = {
    #         'username': 'testuser',
    #         'email': 'testuser@example.com',
    #         'password': 'password'
    #     }
    #     response = self.app.post('/register', data=json.dumps(data), content_type='application/json')
    #     json_data = json.loads(response.data)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn('message', json_data)
    #     self.assertIn('user_id', json_data)
    #     self.assertEqual(json_data['message'], 'User registered successfully')
    #     self.assertTrue(isinstance(json_data['user_id'], int))