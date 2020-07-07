
### 一、需求
公司使用`openvpn`开源系统构建了一整套满足公司vpn需求的产品。2016年开始仅仅搭建了`openvpn`的裸服务端，通过简单的创建、删除和解绑脚本来维护系统。
**痛点：**
- 使用人员需要一定的Linux基础
- 脚本操作容易出错，导致证书丢失
- 操作交互不友好，体验差
- 登入信息无法查询
- 解绑MAC、注销用户不方便
- 没有开放的API调用
- 流程不优，人力资源浪费

`需要一套针对openvpn的内容管理系统，操作简单、维护方便、交互体验好、有日志查询、权限管控、开放API等功能，同时提供插件扩展。`

### 二、选型设计
经过筛选，选择前后端分离，全部通过API交互，方便后续前后端系统的重构。
**前端选择：**`VUE`
**后端选择：**`FLASK`
**数据库：**`Mysql`
**语言环境：**`Python`

基于现有的开源框架Lin-cms二次开发，快速实现业务系统上线。


### 三、安装
#### CentOS 7
`yum install python3-pip`
`python -m venv venv`
`pip install -r requirements.txt`