"""
requests doc: https://requests.readthedocs.io/en/master/
"""
import seldom
from seldom import label, data


class TestLabel(seldom.TestCase):
    """
    测试标签
    """

    @label("put")
    def test_put_method(self):
        """
        PUT请求
        """
        self.put('/put', data={'key': 'value'})
        self.assertStatusCode(200)

    @label("post")
    def test_post_method(self):
        """
        POST请求
        """
        self.post('/post', data={'key':'value'})
        self.assertStatusCode(200)

    @data([
        ("case_one", "value1"),
        ("case_two", "value2"),
        ("case_three", "value3"),
    ])
    @label("get")
    def test_get_method(self, _, value):
        """
        GET请求，参数化
        """
        payload = {'key': value}
        self.get("/get", params=payload)
        self.assertStatusCode(200)



if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")

