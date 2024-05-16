"""
assert method:
 * assertJSON()
 * assertSchema()
 * assertPath()
"""
import seldom


class TestAssert(seldom.TestCase):
    """
    Test Assert
    """

    def test_json_assert(self):
        """
        JSON data assertion.
        """
        self.get("/get")
        self.assertStatusCode(200)
        assert_data = {"headers": {"Host": "httpbin.org", "User-Agent": "python-requests/2.26.0"}}
        self.assertJSON(assert_data, exclude=["headers", "user-agent"])  # exclude 过滤掉 json中的部分字段。

    def test_schema_assert(self):
        """
        json-schema assertion.
        """
        self.get("/get")
        self.assertStatusCode(200)
        # 数据校验
        schema = {
            "type": "object",
            "properties": {
                "headers": {
                    "Host": "httpbin.org",
                    "User-Agent": "python-requests/2.22.0"
                },
                "origin": {"type": "string"},
                "url": {
                    "type": "string",
                    "minLength": 20
                }
            },
        }
        self.assertSchema(schema)

    def test_path_assert(self):
        """
        JMESPath assertion.
        """
        payload = {"foot": "bread"}
        self.get('/get', params=payload)
        self.assertPath("args.foot", "bread")


if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")
