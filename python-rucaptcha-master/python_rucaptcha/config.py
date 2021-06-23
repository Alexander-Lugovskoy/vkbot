# Сервер для отправки данных
url_request_2captcha = "http://2captcha.com/in.php"
# Сервер для получения ответа
url_response_2captcha = "http://2captcha.com/res.php"
# Сервер для отправки данных
url_request_rucaptcha = "http://rucaptcha.com/in.php"
# Сервер для получения ответа
url_response_rucaptcha = "http://rucaptcha.com/res.php"
# ключ приложения
app_key = "1899"

"""
Параметры для callback
"""
# IP для работы callback`a
HOST = "85.255.8.26"
# PORT для работы callback`a
PORT = 8001
# данные для подключения к RabbitMQ на callback сервере
RTMQ_USERNAME = "hardworker_1"
RTMQ_PASSWORD = "password"
RTMQ_HOST = "85.255.8.26"
RTMQ_PORT = 5672
RTMQ_VHOST = "rucaptcha_vhost"

"""
JSON возвращаемы пользователю после решения капчи

serverAnswer - ответ сервера при использовании RuCaptchaControl
captchaSolve - решение капчи,
taskId - находится Id задачи на решение капчи,
         можно использовать при жалобах и прочем,
error - False - если всё хорошо, True - если есть ошибка,
errorBody - полная информация об ошибке:
    {
        text - Развернётое пояснение ошибки
        id - уникальный номер ошибка в ЭТОЙ бибилотеке
    }
"""
JSON_RESPONSE = {
    "serverAnswer": {},
    "captchaSolve": {},
    "taskId": None,
    "error": False,
    "errorBody": {"text": None, "id": 0},
}


# генератор в котором задаётся кол-во поптыок на повторное подключение
def connect_generator():
    for i in range(5):
        yield i
