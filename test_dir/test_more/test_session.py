import seldom


class TestSession(seldom.TestCase):

    def start(self):
        self.s = self.Session()
        self.s.get('/cookies/set/sessioncookie/123456789')

    def test_get_cookie(self):
        """get cookie"""
        self.s.get('/cookies')


if __name__ == '__main__':
    seldom.main(debug=True, base_url="https://httpbin.org")
