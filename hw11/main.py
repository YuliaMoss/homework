from hw11.menu.boil.soup import Soup
from hw11.menu.boil.porrige import Porridge
from hw11.menu.fry.fish import Fish
from hw11.menu.fry.meat import Meat
from hw11.menu.bake.cake import Cake

if __name__ == '__main__':
    borsch = Soup("Borsch", "first dish", 15, ["potatoes", "carrots", "beets"])
    borsch.cook()
    borsch.serve()
    borsch.done_boiling()
    borsch.get_ingredients()
    borsch.all_soup_info()

    oatmeal = Porridge("Oatmeal", "first dish", 10, 2)
    oatmeal.cook()
    oatmeal.serve()
    oatmeal.done_boiling()
    oatmeal.get_water_level()
    oatmeal.all_porridge_info()

    steak = Meat("Steak", "main dish", "beef", "garlic and herbs")
    steak.cook()
    steak.done_frying()
    steak.marinate()
    steak.all_meat_info()

    zander = Fish("Zander", "main dish", "fresh", "peper")
    zander.cook()
    zander.done_frying()
    zander.add_spices()
    zander.all_fish_info()

    sachertorte = Cake("Sachertorte", "dessert", "chocolate cake",
                       ["dark chocolate icing", "unsweetened whipped cream"])
    sachertorte.cook()
    sachertorte.serve()
    sachertorte.done_baking()
    sachertorte.all_cake_info()
