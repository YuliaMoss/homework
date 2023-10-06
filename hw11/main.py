from hw11.menu.boil.soup import Soup
from hw11.menu.boil.porrige import Porridge
from hw11.menu.fry.fish import Fish
from hw11.menu.fry.meat import Meat
from hw11.menu.bake.cake import Cake

if __name__ == '__main__':
    borsch = Soup("Borsch", "first dish", 15, ["potatoes", "carrots", "beets"])
    borsch.cook()
    borsch.is_prepared()
    borsch.get_ingredients()

    oatmeal = Porridge("Oatmeal", "first dish", 10, 2)
    oatmeal.cook()
    oatmeal.is_prepared()
    oatmeal.get_water_level()

    steak = Meat("Steak", "main dish", "beef", "garlic and herbs")
    steak.cook()
    steak.marinate()
    steak.all_info()

    zander = Fish("Zander", "main dish", "fresh", "peper")
    zander.cook()
    zander.is_prepared()
    zander.add_spices()
    zander.all_info()

    sachertorte = Cake("Sachertorte", "dessert", "chocolate cake",
                       ["dark chocolate icing", "unsweetened whipped cream"])
    sachertorte.cook()
    sachertorte.is_prepared()
    sachertorte.all_info()
