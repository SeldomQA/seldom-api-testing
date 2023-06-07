import seldom


class TestRequest(seldom.TestCase):
    """
    http api test demo
    doc: https://requests.readthedocs.io/en/master/
    """

    def test_put_method(self):
        """
        test put request
        """
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    def test_post_method(self):
        """
        test post request
        """
        self.post('/post', data={'key':'value'})
        self.assertStatusCode(200)

    def test_get_method(self):
        """
        test get request
        """
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.get("/get", params=payload)
        self.assertStatusCode(200)

    def test_delete_method(self):
        """
        test delete request
        """
        self.delete('/delete')
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")

