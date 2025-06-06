"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

# 安全性配置
from app.config.setting import BaseConfig


class DevelopmentSecure(BaseConfig):
    """
    开发环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:openvpn@localhost:3306/openvpn'

    SQLALCHEMY_ECHO = False

    # 对线程池中的线程进行一次连接的回收，如果这个值是-1代表永不回收
    SQLALCHEMY_POOL_RECYCLE = 1200

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'


class ProductionSecure(BaseConfig):
    """
    生产环境安全性配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:openvpn@localhost:3306/openvpn'

    SQLALCHEMY_ECHO = False

    # 对线程池中的线程进行一次连接的回收，如果这个值是-1代表永不回收
    SQLALCHEMY_POOL_RECYCLE = 1200

    SECRET_KEY = '\x88W\xf09\x91\x07\x98\x89\x87\x96\xa0A\xc68\xf9\xecJJU\x17\xc5V\xbe\x8b\xef\xd7\xd8\xd3\xe6\x95*4'


"""
    :初始参数设置
    :vpn服务器地址 VPN_ADDRESS
    :vpn服务器端口 VPN_PORT
"""
VPN_ADDRESS = '127.0.0.1'
VPN_PORT = '11940'
