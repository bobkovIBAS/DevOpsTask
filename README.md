Эта ветка (`monitoring`) содержит конфигурационные файлы для настройки мониторинга доступности веб-сайта `https://ptsecurity.com` с использованием Prometheus и Blackbox Exporter

## Структура проекта

- **prometheus.yml**: Конфигурация для Prometheus
- **blackbox.yml**: Конфигурация для Blackbox Exporter
- **README.md**: Документация проекта.

## Предварительные требования

### Установленный Prometheus и Blackbox Exporter.

Если Prometheus и Blackbox Exporter ещё не установлены, скачайте их с официальных источников:

- https://prometheus.io/download/
- https://github.com/prometheus/blackbox_exporter/releases

### Запуск Prometheus и Blackbox Exporter

```
./prometheus --config.file=prometheus.yaml

./blackbox_exporter --config.file=blackbox.yaml
```
### Пример успешного выполнения:
![image](https://github.com/user-attachments/assets/b852ebe3-1f01-49cb-bcb5-6f55dc47f4c1)
![image](https://github.com/user-attachments/assets/793fbacd-6326-458e-a73c-3c269b86ab2b)
