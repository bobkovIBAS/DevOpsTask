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
Клонировать репозиторий 
```
    git clone -b ansible https://github.com/bobkovIBAS/DevOpsTask.git
    cd DevOpsTask
```
Запустить плейбук 
```
    ansible-playbook -i inventory.yaml master_playbook.yaml
```
Важно обратить внимание , что все нужные переменные установлены в файле inventory.yaml

## Пример успешного выполнения:
![image](https://github.com/user-attachments/assets/de07f5e6-88fb-4684-bab4-c3bad1803415)
![image](https://github.com/user-attachments/assets/811189c8-d759-4142-9890-687b9208ddfa)

