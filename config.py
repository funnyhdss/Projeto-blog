ambiente = 'teste'

if ambiente == 'teste':
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'


if ambiente =='producao':
    DB_HOST = 'heitorssantana17.mysql.pythonanywhere-services.com'
    DB_USER = 'heitorssantana17'
    DB_PASSWORD = 'Sesi390117'
    DB_NAME = 'heitorssantana17$Blog'


SECRET_KEY = 'blog'

MASTER_PASSWORD = 'adm'
MASTER_EMAIL = 'adm@adm'