"""
AOM: https://seldomqa.github.io/api-testing/api_object.html
"""
import seldom
from api_object.user_api import UserApiObject


class TestRequest(seldom.TestCase):

    def test_user_login(self):
        """
        test case
        """
        user = UserApiObject()
        user.user_account_login("tom", "tom123")
        self.assertPath("form.username", "tom")
        self.assertStatusCode(200)


if __name__ == '__main__':
    seldom.main(debug=True)
