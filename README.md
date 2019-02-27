## ynoteios-uitest

### 简介
ynoteios-uitest是基于appium编写的有道云笔记iOS自动化测试工具。

### 环境要求

* macOS
* appium 1.7.2+
* python 3.6+ 


### 快速开始

1.安装appium server：


```
    brew install node
    npm install -g appium
```

2.下载项目：

```
    git clone git@github.com:reach950/ynoteios-uitest.git
```

3.安装python库：

```
    pip3 install Appium-Python-Client
    pip3 install pyYAML
```

4.启动appium server：

```
    python3 appium_server.py
```

5.运行测试：

```
    python3 run.py
```

5.result目录查看测试报告


### 报告样式 
![测试报告.png](https://note.youdao.com/yws/api/personal/file/WEB9132e6ae5ffa22b29b9c5b8de34e0f69?method=download&shareKey=12f0fbda0dcf49485157fb4ddeeab388)

### 项目结构：

```
ynoteios-uitest
    
    config －－－－－－－－－－－－－－－－－－－－－－－配置文件
        account.yaml －－－－－－－－－－－－－－－－－－登录账号及密码
        devices.yaml －－－－－－－－－－－－－－－－－－appium driver初始化的配置文件
        mail.yaml －－－－－－－－－－－－－－－－－－发送邮件相关的配置文件
        run_info.yaml －－－－－－－－－－－－－－－－－－运行run.py相关的配置文件

    lib －－－－－－－－－－－－－－－－－－－－－－－工具函数
        appium_driver.py －－－－－－－－－－－－－－－－－－初始化appium driver
        appium_server.py －－－－－－－－－－－－－－－－－－启动appium server
        HTMLTestRunner.py －－－－－－－－－－－－－－－－－－运行用例，生成测试报告
        install_app.py －－－－－－－－－－－－－－－－－－安装app
        send_report.py －－－－－－－－－－－－－－－－－－发送测试报告
        utils.py －－－－－－－－－－－－－－－－－－解析YAML文件等工具
           
    pageobject －－－－－－－－－－－－－－－－－－－－－－－页面对象 

    result －－－－－－－－－－－－－－－－－－－－－－－测试结果

    testcase－－－－－－－－－－－－－－－－－－－－－－－测试用例

    run.py －－－－－－－－－－－－－－－－－－－－－－－执行测试用例入口
```