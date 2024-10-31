Эта ветка (`docker`) содержит настройку простого HTTP-сервера на Python в Docker. Сервер слушает указанный порт и возвращает ответ "200 OK" для проверки работоспособности на маршруте `/healthz`.

## Структура проекта

- **Dockerfile**: Определяет Docker-образ для HTTP-сервера на Python.
- **main.py**: Код HTTP-сервера на Python, который обрабатывает запросы на `/healthz` и отвечает "200 OK".
- **README.md**: Документация проекта.
- 
## Предварительные требования

- Установленный Docker. Если Docker не установлен - https://docs.docker.com/get-docker/

## Использование

### Клонирование репозитория

```
  git clone -b docker https://github.com/bobkovIBAS/DevOpsTask.git
  cd DevOpsTask
```
### Сборка Docker-образа
```
  docker build -t python_server .
```
### Запуск Docker-контейнера

```
  docker run -d -p 8000:8000 python_server
```
### Посмотр всех работающих контейнеров
```
  docker ps -a
```
### Тестирование сервера
Либо зайти по ссылке http://localhost:8000/healthz, либо прописав команду `curl http://localhost:8000/healthz`

## Пример успешного выполнения:
![image](https://github.com/user-attachments/assets/e448286e-fc19-46c9-b380-f8347ab55756)
![image](https://github.com/user-attachments/assets/3e903009-dd09-4857-9b6c-9e79242fb936)
![image](https://github.com/user-attachments/assets/fef8de7f-6888-451b-8d98-eb588b0f1145)
![image](https://github.com/user-attachments/assets/9208405c-2da3-444c-94a9-07514915e739)

