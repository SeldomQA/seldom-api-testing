import seldom


class TestRespData(seldom.TestCase):
    """
    Test response data
    """

    def test_resp_data(self):
        """
        Get the returned data
        """
        payload = {'key1': 'value1', 'key2': 'value2'}
        self.post("/post", data=payload)
        self.assertStatusCode(200)
        self.assertPath("form.key1", "value1")
        self.assertPath("form.key2", "value2")

    def test_data_dependency(self):
        """
        Test for interface data dependencies
        """
        headers = {"X-Account-Fullname": "bugmaster"}
        self.get("/get", headers=headers)
        self.assertStatusCode(200)

        username = self.response["headers"]["X-Account-Fullname"]
        self.post("/post", data={'username': username})
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")
