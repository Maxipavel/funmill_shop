# funmill_shop
Автоматизация проверки цикла выбора товара и последующего его заказа на сайте funmill.ru


Название тестового сценария: Проверка цикла выбора товара и последующего его заказа 

Цель теста: Проверить, что весь цикл работает корректно

Предусловие: Chrome, Selenium, Pycharm

Шаги теста:
1. Открыть сайт https://funmill.ru/ в браузере.
2. Ввод логина и пароля.
3. Вход в корзину для удаления предыдущего введенного товара.
4. Нажатие кнопки "Очистить заказ"
5. Возврат на главную страницу.
6. Выбор категории "Семейные игры"
7. Выбор игр "Атлантида (Atlantis)" , Пэчворк (Patchwork), Проект L (Project L)
8. Переход в корзину.
9. Проверка перехода в корзину по слову "Корзина"
10. Нажатие кнопки "Оформить заказ"
11. Ввод данных:
      - очистка плейсхолдера для ввода города.
      - ввод города "Москва"
      - ожидание выпадающего списка и нажатие на город "Москва"
      - выбор доставки "Почта Росии"
      - выбор оплаты "Банковская карта"
      - очистка поля ввода ФИО 
      - ввод "Иванов Иван Иванович"
      - очистка поля ввода email
      - ввод e-mail "proverka@mail.ru"
      - нажатие на поле ввода номера телефона
      - ввод номера телефона "92137647"
      - ввод адреса "Археологическая улица 3, дом 2, кв 666"
      - ввод индекса "192666" 
      - нажатие галочки "Я согласен с условиями обслуживания"
      - ввод комментария "Позвонить заранее, так как внизу злые бабки могут отобрать мои настолочки"
12. Нажатие кнопки "Оформить заказ"
13. Проверка всплывающего окна ошибки о неверно введенном номере телефона.
14. Скриншот

Ожидаемый результат: После нажатия кнопки "Оформление заказа", всплывает окно ошибки о неверно введенном номере. 

Результат теста: Тест пройден успешно.
