import sys
import requests as r
import hashlib
import re
import json
import hmac
import js2py

base = "http://202.203.208.5"

api = {
    'getToken':'/cgi-bin/get_challenge',
    'login':'/cgi-bin/srun_portal'
}

def hmac_md5(password, token):
    """
    计算 HMAC-MD5 哈希
    :param password: 消息（字符串或字节数据）
    :param token: 密钥（字符串或字节数据）
    :return: 十六进制格式的哈希值
    """
    if isinstance(password, str):
        password = password.encode("utf-8")  
    if isinstance(token, str):
        token = token.encode("utf-8") 

    hmac_md5_hash = hmac.new(token, password, hashlib.md5)
    return hmac_md5_hash.hexdigest()
def sha1(s):
    m = hashlib.sha1()
    m.update(s.encode('utf-8'))
    return m.hexdigest()

def get_token(user_name,ip):
    """
    从服务器获取token,原api使用jsonp,此处模拟
    """
    if user_name == "" or ip == "":
        raise ValueError("user name is empty") 
    res = r.get(base+api['getToken'],params= {"callback":"jQuery111307456654444444444","username":USERNAME,"ip":ip})
    pattern = re.compile(r'\((.*)\)')
    res = re.search(pattern,res.text).group(1)
    json_res = json.loads(res)
    token = json_res['challenge']
    if token is None:
        print("geting token error!")
        exit(0)
    return token

def encode_userInfo(info,token):
    """
    参数中有将user_info进行base64编码,因为python和js的位运算结果可能不同,所以此处不再对原编码方法重写,直接调用js
    """
    with open('encry.js', 'r',encoding='utf-8') as file:
        js_code = file.read()
    js_context = js2py.EvalJs()
    js_context.execute(js_code)
    encode_result = js_context.encryt(info, token)
    return encode_result


def get_all_params():
    """
    构造所有用于认证的参数
    """
    user_info = {
        "username": USERNAME,
        "password": PASSWORD,
        "ip": IP,
        "acid": AC_ID,
        "enc_ver": ENC
    }


    token = get_token(user_name=USERNAME,ip=IP)
    md5_passwd = hmac_md5(PASSWORD, token)
    encoded_user = encode_userInfo(user_info,token)

    all_str = token + USERNAME
    all_str += token + md5_passwd
    all_str += token + AC_ID
    all_str += token + IP
    all_str += token + N_STR
    all_str += token + TYPE
    all_str += token + encoded_user
        
    return {
        "callback":"jQuery111307456654444444444",
        "action": 'login',
        "username": USERNAME,
        "password": '{MD5}' + md5_passwd,
        "os": OS,
        "name": OS_NAME,
        "double_stack": 0,
        "chksum": sha1(all_str),
        "info": encoded_user,
        "ac_id": AC_ID,
        "ip": IP,
        "n": N_STR,
        "type":TYPE
        }


def send_auth():
    res = r.get(base+api['login'],params=get_all_params())
    pattern = re.compile(r'\((.*)\)')
    res = re.search(pattern,res.text).group(1)
    json_res = json.loads(res)
    
    if json_res['error'] != 'ok':
        print("auth fail:"+json_res['error'])
    else :
        print("auth done")


"""
此处包含所有参数,用户只需指定用户名(学号),密码即可,ip地址使用脚本获取
"""


USERNAME=""
PASSWORD = ""
ENC = 'srun_bx1'
AC_ID = '0'
N_STR = "200"
TYPE = '1'
OS = "Windows 10"
OS_NAME = "Windows"




"""
    本脚本没有对用户输入进行校验,请用户自行保证自己的输入正确
"""


if __name__ == '__main__':
    # 本脚本主要用于linux运行,如有windows需求,请在下面获取当前IP地址,并且填充到IP
    IP=""
    if len(sys.argv) > 1:
        IP = sys.argv[1]
    send_auth()
