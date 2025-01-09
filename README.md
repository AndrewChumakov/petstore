<h1 align="center">Проект автоматизации тестирования api Petstore</h1>

# Описание

### Кейсы:

- Создание заказа
- Удаление существующего заказа
- Невозможность удаления несуществующего заказа
- Получение существующего заказа
- Невозможность получения существующего заказа

### Используемый стек технологий и инструментов:

| Python                                                | Pycharm                                                | Git                                                | Pytest                                                | Allure <br/> Report                                   | Jenkins                                                |                                                Telegram |
|:------------------------------------------------------|--------------------------------------------------------|----------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------:|
| <img height="50" src="source/Python.png" width="50"/> | <img height="50" src="source/Pycharm.png" width="50"/> | <img height="50" src="source/git.svg" width="50"/> | <img height="50" src="source/Pytest.png" width="50"/> | <img height="50" src="source/allure.svg" width="50"/> | <img height="50" src="source/Jenkins.svg" width="50"/> | <img height="50" src="source\Telegram.svg" width="50"/> |

# Запуск тестов

```   
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest 
```

# Сборка в Jenkins

Для запуска сборки необходимо нажать кнопку **"Build Now"**.

<p align="center">
<img title="Jenkins Build" src="source/build.png"> 
</p>

# Интеграция с Allure Report

<p align="center">   
<img title="Allure Report" src="source/allure_report.png">    
</p>

# Уведомление в Telegram

<p align="center">   
<img title="Telegram" src="source/telegram.png">    
</p>

