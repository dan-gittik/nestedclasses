import nestedclasses


@nestedclasses.nestedclasses()
class A:
    x = 1
    class B:
        y = x + 1
        class C:
            x = 0
            z = y + 1


def test_nestedclasses():
    assert A.x     == 1
    assert A.B.y   == 2
    assert A.B.C.x == 0
    assert A.B.C.z == 3
