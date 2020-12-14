# Сервис записи клиентов
![Python version](https://img.shields.io/badge/python-3.7%2B-blue)
[![Build Status](https://travis-ci.com/KazakovDenis/booking-service.svg?branch=main)](https://travis-ci.com/KazakovDenis/booking-service)

[Техническое задание](https://github.com/KazakovDenis/booking-service/blob/main/task.txt)  

## Использованный технологический стек
* Python, Javacript
* Django 3.1.4
* Docker

## Запуск сервиса
* Для запуска в docker-контейнере необходимо:  
  
    1). добавить следующие данные в переменные окружения:  
    ```
    export BOOKING_SECRET="ваш_секретный_ключ"
    ```
    2). запустить сервис  
    ```
    docker-compose up -d --build
    ```
    3). проверить работу сервиса: http://localhost:8000/

## Описание работы
- При первом запуске сервиса создаётся суперпользователь с именем и паролем "admin". 
  Пароль необходимо сменить либо создать нового пользователя.
- На главной странице:
  - при выборе врача, подгружается его расписание с текущего дня и далее
  - при выборе даты строится список доступного для записи на приём времени
  - данные, вводимые в *input*-элементы, валидируются как на клиентской, так и на серверной части
  - совокупно данные валидируются на бекенде при отправке формы