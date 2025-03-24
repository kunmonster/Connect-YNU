# Connect-YNU

将YNU校园网portal认证页面逻辑使用python脚本实现,用于本人linux平台自动断线重连(实际上MAC地址认证的话重新dhcp就行),用户只需要输入账号密码即可.

### 使用方法
--- 
1. 将fuckynu.py中的USERNAME="" 与 PASSWORD=""填充.

2. 
```bash
python fuckynu.py ip地址
```

注意: 传参的ip地址是dhcp到的前域地址,也就是未认证之前的ip地址，嫌麻烦的用户可以直接使用python获取,因为我用的linux平台,所以直接使用ip命令得到了,没在这里实现python获取.



如果跟我一样linux用户，可以直接使用check_and_reauth.sh脚本(较为粗糙,面向本机编程),该sh脚本检测是否有网,如果没有,拿到地址传给py脚本进行auth.


### 不足
---

由于js和python的整型不太一样导致位运算结果不一致,所以脚本中部分直接调用js代码,需要js2py模块(难得折腾).

### 声明
---
本脚本只用于YNU认证登录,仅供交流学习,请勿用于他用!
