import os
import smtplib
from dotenv import load_dotenv

from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")



from_email = "devmanorg@yandex.ru"
to_email = "mariam130396@gmail.com"

email = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!
%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.
Как будет проходить ваше обучение на %website%?
Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь. Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.
Регистрируйся → %website%
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

website = "https://dvmn.org/profession-ref-program/mariam130396/BHVPI/"
name = "Emily"
sender = "Mariam"

email = email.replace("%website%", website)
email = email.replace("%friend_name%", name)
email = email.replace("%my_name%", sender)

letter = f"""From:  {from_email}
To: {to_email}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

{email}"""

server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
server.login(login, password)
server.sendmail(login, "{from_email}", letter.encode("utf-8"))
server.quit()
