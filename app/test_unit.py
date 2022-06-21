import unittest
import requests as req
import json

class TestStringMethods(unittest.TestCase):



    def test_post(self):
        headers = {'Content-Type': 'application/json'}
        body = '{"name":"Task 1","priority":"1","description":"task 1 test"}'

        result = req.post("http://127.0.0.1:5000/task", body, headers=headers)
        self.assertEqual(result.status_code, 201)

    # def test_get_all(self):
    #
    #     headers = {'Content-Type': 'application/json'}
    #     result = req.get("http://127.0.0.1:5000/tasks", headers=headers)
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    def test_get(self):
        headers = {'Content-Type': 'application/json'}
        body = '{"name":"Task Test Get", "priority":"1","description":"task get test"}'
        result = req.post("http://127.0.0.1:5000/task", body, headers=headers)

        id = result.json()["Task"]["id"]

        result = req.get("http://127.0.0.1:5000/task/"+str(id), headers=headers)

        self.assertEqual(result.status_code, 200)
        self.assertEqual("Task Test Get", str(result.json()["Task"][0]["name"]))

        # self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        # with self.assertRaises(TypeError):
        #     s.split(2)

    # def test_put(self):
    #     headers = {'Content-Type': 'application/json'}
    #     result = req.put("http://127.0.0.1:5000/task", headers=headers)
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    #
    # def test_delete(self):
    #     headers = {'Content-Type': 'application/json'}
    #     result = req.post("http://127.0.0.1:5000/task", headers=headers)
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
