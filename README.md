# Проект автоматизации тестирования сервиса Stellar Burgers https://stellarburgers.nomoreparties.site/ 
```
1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска — pytest -v --cache-clear.
```

# Cтруктура проекта:
```
Sprint_5/
│-- config.py (хранит базовые URL) 
│-- conftest.py (настройка браузера для тестов)
│-- locators.py (хранит все локаторы страниц) 
│-- utils.py (функции генерации email, пароля) 
│-- tests/
│   │-- test_login.py (тесты входа) 
│   │-- test_navigation.py (тесты переходов) 
│   │-- test_registration.py (тесты регистрации)
│   │-- test_logout.py (тест выхода из ЛК) 
│-- .gitignore
│-- README.md
```
