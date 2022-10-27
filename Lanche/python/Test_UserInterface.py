from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order


def test_get_user_input():
    result = "2 5".split(" ")

    assert result[0].isnumeric() == True
    assert result[1].isnumeric() == True


def test_get_total_price():
    menu_repository = MenuRepository()
    lanche = Menu(3, "X-Bacon",5.00)
    menu_repository.set_menu_item(lanche)

    order = Order(3, 5)
    assert (order.quantity * lanche.price) == 25
    

def test_get_total_price2():

    lanche = Menu(1, "Hot-dog", 4.00)
    order = Order(1, 5)

    assert (order.quantity * lanche.price) == 20    