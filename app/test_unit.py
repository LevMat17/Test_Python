import unittest
import requests as req
import json

class TestStringMethods(unittest.TestCase):

    def test_post(self):
        headers = {'Content-Type': 'application/json'}
        body = '{"name":"Task Post","priority":1,"description":"task 1 test"}'

        result = req.post("http://127.0.0.1:5000/task", body, headers=headers)
        self.assertEqual(result.status_code, 201)
        print("Post OK : OK")

    def test_get_all(self):
        headers = {'Content-Type': 'application/json'}
        body1 = '{"name":"Task Test Get All 1", "priority":1,"description":"task get test"}'
        body2 = '{"name":"Task Test Get All 2", "priority":1,"description":"task get test"}'
        result = req.post("http://127.0.0.1:5000/task", body1, headers=headers)
        result = req.post("http://127.0.0.1:5000/task", body2, headers=headers)

        result = req.get("http://127.0.0.1:5000/task", headers=headers)

        self.assertNotEqual(len(result.json()["Task"]), 1)
        print("Get All : OK")

    def test_get_OK(self):
        headers = {'Content-Type': 'application/json'}
        body = '{"name":"Task Test Get OK", "priority":1,"description":"task get test"}'
        result = req.post("http://127.0.0.1:5000/task", body, headers=headers)

        id = result.json()["Task"]["id"]

        result = req.get("http://127.0.0.1:5000/task/"+str(id), headers=headers)

        self.assertEqual(result.status_code, 200)
        self.assertEqual("Task Test Get OK", str(result.json()["Task"][0]["name"]))
        print("Get OK : OK")

    def test_get_KO(self):
        headers = {'Content-Type': 'application/json'}
        id=443
        result = req.get("http://127.0.0.1:5000/task/"+str(id), headers=headers)

        self.assertEqual(result.status_code, 404)
        print("Get KO : OK")

    def test_put_OK(self):
        headers = {'Content-Type': 'application/json'}
        body = '{"name":"Task Test Put OK", "priority":1,"description":"task get test"}'
        result = req.post("http://127.0.0.1:5000/task", body, headers=headers)

        id = result.json()["Task"]["id"]

        result = req.get("http://127.0.0.1:5000/task/"+str(id), headers=headers)

        new_body = '{"name":"Task Test Put OK Change"}'

        new_result = req.put("http://127.0.0.1:5000/task/"+str(id), new_body, headers=headers)

        self.assertEqual(result.status_code, 200)
        self.assertNotEqual(result.json()["Task"][0]["name"], new_result.json()["Task"]["name"])
        print("Put OK : OK")

    def test_put_K0(self):
        headers = {'Content-Type': 'application/json'}
        new_body = '{"name":"Task Test Put Change"}'
        id=443
        result = req.put("http://127.0.0.1:5000/task/"+str(id), new_body, headers=headers)

        self.assertEqual(result.status_code, 404)
        print("Put KO : OK")


    def test_delete(self):
        body = '{"name":"Task Test Delete", "priority":1,"description":"task get test"}'
        headers = {'Content-Type': 'application/json'}

        result_post = req.post("http://127.0.0.1:5000/task", body, headers=headers)
        id = result_post.json()["Task"]["id"]

        result_delete = req.delete("http://127.0.0.1:5000/task/"+str(id), headers=headers)

        self.assertEqual(result_delete.status_code, 200)

        result_get = req.get("http://127.0.0.1:5000/task/"+str(id), headers=headers)
        self.assertEqual(result_get.status_code, 404)
        print("Deletion : OK")

if __name__ == '__main__':
    unittest.main()
