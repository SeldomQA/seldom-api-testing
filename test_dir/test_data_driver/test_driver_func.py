import seldom
from seldom import data


class TestDDT(seldom.TestCase):
    """
    Test Data Driver
    """

    @data([
        ("case1", "key1", 'value1'),
        ("case2", "key2", 'value2'),
        ("case3", "key3", 'value3')
    ])
    def test_list_data(self, _, key, value):
        """
        Data-Driver Tests
        """
        payload = {key: value}
        self.post("/post", data=payload)
        self.assertStatusCode(200)
        self.assertEqual(self.response["form"][key], value)

    @data([
        {"name": "case1", "username": "user1", "password": "abc123"},
        {"name": "case2", "username": "user2", "password": "abc456"},
        {"name": "case3", "username": "user3", "password": "abc789"}
    ])
    def test_dict_data(self, _, username, password):
        """
        Data-Driver Tests
        """
        self.post("/post", data={username: password})
        self.assertStatusCode(200)
        self.assertEqual(self.response["form"][username], password)


if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")
