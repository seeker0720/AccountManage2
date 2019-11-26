### AccountManage2

_**基于Python的web框架Django的账户管理网站**_

#### 部署教程

##### 登陆MySQL数据库执行以下命令

```bash
CREATE USER 'admin2'@'localhost' IDENTIFIED BY 'AccountManage123!@#';
CREATE DATABASE `accountdb2` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci */;
GRANT all ON accountdb2.* TO 'admin2'@'localhost';
FLUSH PRIVILEGES;
exit
```

##### 创建虚拟环境

在 `AccountManage2` 目录下执行以下命令

```bash
virtualenv AM_env2
```

##### 激活虚拟环境并安装依赖的包

```bash
.\AM_env2\Scripts\activate

pip install -r requirements.txt
```

##### 迁移数据、创建管理员账户

```bash
cd AccountManage
python manage.py makemigratitons
python manage.py makemigrate
python manage.py createsuperuser
```

##### 启动项目
```bash
python manage.py runserver
```

