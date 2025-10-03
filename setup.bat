@echo off
echo Установка зависимостей и запуск миграций...

REM URL репозитория
set repo_url=https://github.com/kirasuperkira/task_git
set repo_name=git

echo Клонирование репозитория...

REM Проверка существования папки с проектом
if exist "%repo_name%" (
    echo Папка "%repo_name%" уже существует. Используется существующая версия
    cd "%repo_name%"
) else (
    REM Клонирование репозитория
    git clone %repo_url%
    
    if errorlevel 1 (
        echo ОШИБКА: Не удалось клонировать репозиторий
        exit /b 1
    )
    
    cd "%repo_name%"
)

REM Проверка наличия req.txt
if not exist "req.txt" (
    echo ОШИБКА: файл не найден
    pause
    exit /b 1
)

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