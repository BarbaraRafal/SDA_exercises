import requests
from home_work.mocks_example import get_content_from_google, get_response_status_code


class MocksExampleTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @patch("home_work.mocks_example.requests")
    def test_message_when_response_status_code_200(self, mocked_request):
        mocked_get = mocked_request.get = MagicMock()
        mocked_get.status_code = 200
        result = get_content_from_google(mocked_get.status_code)
        self.assertEqual(result, f"OK, status: {200}")

    @patch("home_work.mocks_example.get_response_status_code")
    def test_func_returns_code_400(self, mocked_request):
        mocked_request.return_value = 400
        result = mocked_request()
        self.assertEqual(result, 400)
