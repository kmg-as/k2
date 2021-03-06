class Employee:
    def __init__(self, f_name, l_name, rph):
        self.f_name = f_name
        self.l_name = l_name
        self.rph = rph

    def register_time(self, hours):
        self._worked_hours = hours

    def pay_salary(self):
        return self._worked_hours * self.rate_per_hour + self.bonuses


class PremiumEmployee(Employee):
    def give_bonus(self,bonus):
        self.bonuses +=bonus



class TestEmployee:
    def test__init__(self):
        employee = Employee("Jan", "Nowak", 100.0)
        assert employee.f_name == "Jan"
        assert employee.l_name == "Nowak"
        assert employee.rph == 100.0

    def test_register_time(self):
        employee = Employee("Jan", "Nowak", 100.0)
        employee.register_time(5)
        assert employee._worked_hours == 5

    #   def test_register_salary(self):
    #      employee=Employee("Jan", "Nowak", 100.0)
    #     employee.salary(5)
    #    assert employee._worked_hours == 5

    def test_pay_salary_when_no_worked_hours(self):
        employee = Employee("Jan", 'Nowak', 100.0)
        assert employee.pay_salary() == 0

    def test_pay_salary_with_worked_hours(self):
        employee = Employee("Jan", 'Nowak', 100.0)
        employee.register_time(5)
        assert employee.pay_salary() == 5 * 100
        assert employee.pay_salary() == 0


class TestPremiumEmployee:
    def test_inizialization(self):
        pe = PremiumEmployee("Jan", "Nowak", 100.0)
        assert pe.f_name == "Jan"
        assert pe.l_name == "Nowak"
        assert pe.rph == 100.0

    def test_give_bonus(self):
        pe = PremiumEmployee("Jan", 'Nowak', 100.0)
        assert pe.pay_salary() == 5 * 100
        assert pe.pay_salary() == 0
