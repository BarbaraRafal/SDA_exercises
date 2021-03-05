import unittest
from tdd_day1.account import Account


class AccountTestCase(unittest.TestCase):
    def test_transfer_when_money_withdrawal(self):
        # Given
        account = Account(100, "owner")
        # When
        account.transfer(-50)
        self.assertEqual(account.balance(), 50)

    def test_user_status(self):
        # Given
        account = Account(100, "owner")
        # When
        status = account.user_status
        self.assertEqual(status, "owner")


if __name__ == '__main__':
    unittest.main()
