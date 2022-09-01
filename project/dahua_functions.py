import requests
from requests.auth import HTTPDigestAuth

def dahua_name(srv, headers, name):
    s = requests.session()
    url_hosts = "http://{}/cgi-bin/configManager.cgi?action=setConfig&ChannelTitle[0].Name={}".format(srv, name)
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print("Имя успешно изменено")
    else:
        print("Ошибка изменения имени")


def dahua_network(srv, headers, seting):
    s = requests.session()
    url_hosts = f"http://{srv}/cgi-bin/configManager.cgi?action=setConfig"
    for key, value in seting.items():
        url_hosts += f'&{key}={value}'
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print("Eспешно изменены сетевые настройки")
    else:
        print("Ошибка изменения сетевые настроек")



def dahua_video(srv, headers, video):
    s = requests.session()
    url_hosts = f"http://{srv}/cgi-bin/configManager.cgi?action=setConfig"
    for key, value in video.items():
        url_hosts += f'&{key}={value}'
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print("Eспешно изменены настройки видео")
    else:
        print("Ошибка изменения настроек видео")

def dahua_ntp(srv, headers, ntp_cam):
    s = requests.session()
    url_hosts = f"http://{srv}/cgi-bin/configManager.cgi?action=setConfig"
    for key, value in ntp_cam.items():
        url_hosts += f'&{key}={value}'
    print(url_hosts)
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print("Eспешно изменены настройки ntp")
    else:
        print("Ошибка изменения настроек ntp")


def dahua_add_user(srv, headers, user_name, user_pass, group="user"):
    s = requests.session()
    url_hosts = f"http://{srv}/cgi-bin/userManager.cgi?action=addUser&user.Name={user_name}&user.Password={user_pass}" \
                f"&user.Group={group}&user.Sharable=true&user.Reserved=false"
    print(url_hosts)
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print(f'Пользователь {user_name} создан')
    else:
        print(f'Пользователь {user_name} не создан')


def dahua_get_network(srv, headers):
    s = requests.session()
    url_hosts = f"http://{srv}/cgi-bin/configManager.cgi?action=getConfig&name=Network"
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
    f = open("./cofig/"+m["table.Network.eth2.IPAddress"] + ".txt", 'w')
    f.write(str(m))
    f.close()

def dahua_snapshot(srv, headers):
    s = requests.session()
    url_hosts = f"http://{srv}/cgi-bin/snapshot.cgi"
    print(url_hosts)
    page = s.get(url=url_hosts, auth=HTTPDigestAuth(headers['login_username'], headers['login_password']))
    if page.status_code == 200:
        print(f'Снапшот создан')
    else:
        print(f'Снапшот не создан')
