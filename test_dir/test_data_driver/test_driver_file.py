import seldom
from seldom import file_data


class FileDataTest(seldom.TestCase):
    """form input test case"""

    @file_data("test_data/json_data.json", key="name")
    def test_json_list(self, firstname, lastname):
        """
        used file_data test
        """
        self.get("/get", params={firstname: lastname})
        self.assertStatusCode(200)

    @file_data("test_data/json_data.json", key="login")
    def test_json_dict(self, _, username, password):
        """
        used file_data test
        """
        self.get("/get", params={username: password})
        self.assertStatusCode(200)

    @file_data("test_data/yaml_data.yaml", key="name")
    def test_yaml_list(self, firstname, lastname):
        """
        used file_data test
        """
        self.get("/get", params={firstname: lastname})
        self.assertStatusCode(200)

    @file_data("test_data/yaml_data.yaml", key="login")
    def test_yaml_dict(self, username, password):
        """
        used file_data test
        """
        self.get("/get", params={username: password})
        self.assertStatusCode(200)

    @file_data("test_data/csv_data.csv", line=2)
    def test_csv(self, firstname, lastname):
        """
        used file_data test
        """
        self.get("/get", params={firstname: lastname})
        self.assertStatusCode(200)

    @file_data("test_data/excel_data.xlsx", sheet="Sheet1", line=2)
    def test_excel(self, firstname, lastname):
        """
        used file_data test
        """
        self.get("/get", params={firstname: lastname})
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")
