from fromzerotohero.settings import BASE_DIR


def my_cron():
    path = BASE_DIR + '/deneme.txt'
    file = open(path, 'w', encoding="utf-8")
    file.write("Crontab is running!")
    file.close()
