# Connect-YNU
This repo contains the scirpts to connect YNU school network.

本脚本将YNU校园网portal认证页面逻辑使用python脚本实现,用于本人linux平台断线重连(实际上mac认证的话可以redhcp就行),用于只需要输入账号密码即可.

### 使用方法

fuckynu.py中的USERNAME和PASSWORD填充即可

python fuckynu.py ip地址(dhcp到的前域地址,嫌麻烦的用户可以直接使用python获取,因为我用的linux平台,所以直接使用ip命令得到了,没在这里实现pyhon获取)

如果跟我一样linux用户，可以直接使用sh脚本(较为粗糙,面向本机编程),该sh脚本检测是否有网,如果没有拿到地址传给py脚本进行auth


### 不足

由于js和python的整型不太一样导致位运算结果不一致,所以脚本中部分直接调用js代码,需要js2py模块

### 声明

本脚本只用于YNU认证登录,仅供交流学习,请勿用于他用!
