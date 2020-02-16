class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x=self.x + other.x
        y=self.y + other.y

    def __dif__(self, other):
        x = self.x - other.x
        y = self.y - other.y


class Test_Vector:
    def test_init(self):
        assert Vector(1, 2)
        assert Vector(2, 2)

    def test_add(self):
        assert Vector1(1, 2) == 3
        assert Vector2(2, 2) == 4
        assert Vector1 + Vector2 == (3,4)


    def test_dif(self):
        assert Vector1(1, 2) == -1
        assert Vector2(2, 2) == 0
