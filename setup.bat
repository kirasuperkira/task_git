@echo off
echo Установка зависимостей и запуск миграций...

REM Создаём виртуальное окружение, если его нет
if not exist venv (
    python -m venv venv
)

REM Активируем виртуальное окружение и устанавливаем зависимости
call venv\Scripts\activate
pip install -r req.txt

REM Применяем миграции
python manage.py migrate

REM Запускаем тесты
python manage.py test

echo Готово!
pause