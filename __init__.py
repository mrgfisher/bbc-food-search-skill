from mycroft import MycroftSkill, intent_file_handler


class BbcFoodSearch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('search.food.bbc.intent')
    def handle_search_food_bbc(self, message):
        self.speak_dialog('search.food.bbc')


def create_skill():
    return BbcFoodSearch()

