from datetime import datetime


class Base():

    def __init__(self, driver_g):
        self.driver_g = driver_g

    # Method get current url

    def get_current_url(self):
        get_url = self.driver_g.current_url
        print("Current url " + get_url)

    # Method assert word

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    # Method screenshot

    def get_screenshot(self):
        now_date = datetime.utcnow().strftime(" %Y, %m, %d, %H, %M, %S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver_g.save_screenshot('C:\\Users\\Pavel\\PycharmProjects\\pythonProject\\funmill_shop\\screen\\' + name_screenshot)

    # проверяем наличие всплывающего окна ошибки ввода телефона

    def assert_pop_up(self, result_pop_up):
        assert self.assert_pop_up(result_pop_up)


