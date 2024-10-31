Эта ветка (`ansible`) содержит Ansible плейбуки для настройки сервера с установкой PostgreSQL и других необходимых компонентов.

## Структура проекта

- **inventory.yaml**: Файл с информацией о серверах и переменных, необходимых для подключения Ansible к удалённым узлам.
- **main.yaml**: Основной Ansible плейбук, выполняющий настройку системы и установку PostgreSQL.
- **vars.yaml**: Файл переменных, содержащий параметры конфигурации PostgreSQL и другие настройки.
- **README.md**: Документация проекта.

## Предварительные требования на debian сервере 
Необходимо зайти под рутом и установить ssh 
```
    su -
    apt install ssh
```
Поменять строки в файле /etc/ssh/sshd_config
```
    PermitRootLogin yes
    PasswordAuthentication yes
```
После этого перезапустить ssh 
```
    systemctl restart sshd
```

## Предварительные требования на главном сервере

Установить ansible 
```
    sudo apt update
    sudo apt install ansible -y
```
Установить ssh и sshpass

```
    sudo apt install ssh
    sudo apt install sshpass
```
Клинировать репозиторий 
```
    git clone -b ansible https://github.com/bobkovIBAS/DevOpsTask.git
    cd DevOpsTask
```
Запустить плейбук 
```
    ansible-playbook -i inventory.yaml main.yaml
```
Важно обратить внимание , что все нужные переменные установлены в файле inventory.yaml


