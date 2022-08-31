

def list_of_servers():
    """
    Получение списка ip адресов? ,без проверки на валидность из ../date/dahua.txt

    """
    servers = []
    try:
        servers = []
        file1 = open("../date/dahua.txt", "r")

        while True:
            line = file1.readline()
            if not line:
                break
            servers.append(line.strip())
    except :
            pass
    return servers
