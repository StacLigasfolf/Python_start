import re


def email_parse(email_addres):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email_addres):
        raise ValueError(f'wrong email: {email_addres}')
    print(re_email.match((email_addres).groupdict()))


for i in ['forestgump@geekbrains.ru', 'fura@geekbrains.ru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)
