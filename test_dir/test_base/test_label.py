"""
requests doc: https://requests.readthedocs.io/en/master/
"""
import seldom
from seldom import label, data


class TestRequest(seldom.TestCase):
    """
    http api test demo
    """

    @label("put")
    def test_put_method(self):
        """
        test put request
        """
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    @label("post")
    def test_post_method(self):
        """
        test post request
        """
        self.post('/post', data={'key':'value'})
        self.assertStatusCode(200)

    @data([
        ("case_one", "value1"),
        ("case_two", "value2"),
        ("case_three", "value3"),
    ])
    @label("params")
    def test_get_method(self, _, value):
        """
        test get request
        """
        payload = {'key': value}
        self.get("/get", params=payload)
        self.assertStatusCode(200)



if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")

