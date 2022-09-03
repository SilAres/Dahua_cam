import requests
from requests.auth import HTTPDigestAuth


def dahua_name(cam, headers, name):
    print(f'Смена имени камеры {cam}')
    s = requests.session()
    url_hosts = "http://{}/cgi-bin/configManager.cgi?action=setConfig&ChannelTitle[0].Name={}".format(cam, name)
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print("Имя успешно изменено")
    else:
        print("Ошибка изменения имени")


def dahua_network(cam, headers, seting):
    print(f'Смена сетевых настроек камеры {cam}')
    # print(seting)
    s = requests.session()
    url_hosts = f"http://{cam}/cgi-bin/configManager.cgi?action=setConfig"
    for key, value in seting.items():
        url_hosts += f'&{key}={value}'
    # print(url_hosts)
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    # print(page.status_code)

    if page.status_code == 200:
        print("Eспешно изменены сетевые настройки")
    else:
        print("Ошибка изменения сетевые настроек")


def dahua_video(cam, headers, video):
    print(f'Смена видео настроек камеры {cam}')
    s = requests.session()
    url_hosts = f"http://{cam}/cgi-bin/configManager.cgi?action=setConfig"
    for key, value in video.items():
        url_hosts += f'&{key}={value}'
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print("Eспешно изменены настройки видео")
    else:
        print("Ошибка изменения настроек видео")


def dahua_audio(cam, headers, audio):
    print(f'Смена аудио настроек камеры {cam}')
    s = requests.session()
    url_hosts = f"http://{cam}/cgi-bin/configManager.cgi?action=setConfig"
    for key, value in audio.items():
        url_hosts += f'&{key}={value}'
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print("Звук включен")
    else:
        print("Ошибка включения звука")


def dahua_ntp(cam, headers, ntp_cam):
    print(f'Смена настроек ntp камеры {cam}')
    s = requests.session()
    url_hosts = f"http://{cam}/cgi-bin/configManager.cgi?action=setConfig"
    for key, value in ntp_cam.items():
        url_hosts += f'&{key}={value}'
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print("Eспешно изменены настройки ntp")
    else:
        print("Ошибка изменения настроек ntp")


def dahua_add_user(cam, headers, user_name, user_pass, group="user"):
    print(f'Добавление пользователей камеры {cam}')
    s = requests.session()
    url_hosts = f"http://{cam}/cgi-bin/userManager.cgi?action=addUser&user.Name={user_name}&user.Password={user_pass}" \
                f"&user.Group={group}&user.Sharable=true&user.Reserved=false"
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print(f'Пользователь {user_name} создан на камере {cam}')
    else:
        print(f'Пользователь {user_name} не создан')


def dahua_get_network(cam, headers):
    print(f'Сохранени настроек сети камеры {cam} в файл')
    s = requests.session()
    url_hosts = f"http://{cam}/cgi-bin/configManager.cgi?action=getConfig&name=Network"
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    # print(url_hosts)
    if page.status_code == 200:
        print("успешно")
    else:
        print("Ошибка")
    m = {}
    for i in page.text.split("\r\n"):
        k = i.split("=")
        if k != ['']:
            m[k[0]] = k[1]
    f = open("./date_cam/"+m["table.Network.eth0.IPAddress"] + ".txt", 'w')
    f.write(str(m))
    f.close()


def dahua_snapshot(cam, headers):
    print(f'Сохранени снапшота сети камеры {cam} в файл')
    s = requests.session()
    url_hosts = f"http://{cam}/cgi-bin/snapshot.cgi"
    # print(url_hosts)
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    with open(f'./scrin/{cam}.jpg', 'wb') as handler:
        handler.write(page.content)
    if page.status_code == 200:
        print(f'Снапшот создан')
    else:
        print(f'Снапшот не создан')
