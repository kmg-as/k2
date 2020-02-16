class CashMachine:
    pass
    is_available = False

    def __init__(self):
        self.bills = []

    def put_money(self, bills):
        self._bills.extend(bills)

    @propety

    def is_available(self):
        if self._bills:
            return True
        return False


def withdraw_money(self, amount):
    to_withdraw = self._bills
    for bill in self._bills:
        if sum(to_withdraw) + bill <= amount:
            to_withdraw.append(bill)
            self._bills.remove(bill)
    return to_withdraw


class TestCashMachine:

    def test__initialization(self):
        assert CashMachine()

    def test_is_available(self):
        cs = CashMachine()
        assert not cs.is_available

    def test_cs_is_available_after_put_money(self):
        cs = CashMachine()
        assert not cs.is_available
        cs.put_money([100, 100])
        assert cs.is_available

    def test_withdraw_money(self):
        cs = CashMachine()
        cs.put_money([100, 100])
        assert cs.withdraw_money(200) == [100, 100]
        assert cs.is_available is False
