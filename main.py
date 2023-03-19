"""The HTTP POST method sends data to the server."""
from requests import post


def send_data(url, proxies, data, cookies):
    return post(url,
                proxies=proxies,
                data=data,
                cookies=cookies,
                timeout=10)


if __name__ == "__main__":
    proxy = {
        'http': 'http://localhost:8080'
    }
    URL = 'http://localhost/login.php'
    headers = {"Host": "localhost",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
                         "image/avif,image/webp,*/*;q=0.8",
               "Accept-Language": "pl,en-US;q=0.7,en;q=0.3",
               "Accept-Encoding": "gzip, deflate",
               "Content-Type": "application/x-www-form-urlencoded",
               "Content-Length": "51",
               "Origin": "http://localhost"}
    data_raw = {"login": "bee",
            "password": "bug",
            "security_level": 0,
            "form": "submit"}
    cookies = {"csrftoken": "RDSUJqIJ7Z7gYe62lIgbpQXeIDJZDlFJG0R4f78alSSl1aSp20NJPUkOXtJ3PAld",
               "security_level": "0",
               "PHPSESSID": "ef8slb99vhcnncvsdc0ncj3ge7"}
    print(send_data(URL, proxy, data_raw, cookies))
