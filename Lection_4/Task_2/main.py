# Система собирает информацию с датчиков, в ней есть модуль логирования, который заносит в журнал все обращения к датчикам. В системе есть модуль, 
# выполняющий обращения для получения данных с датчиков и модуль генерации html-представления. Запуск системы осуществляется из головного модуля

# Модули:
# data_provider - сбор информации с датчиков
# logger - логирование
# user_interface - UI
# html_creater - HTML-генератор
# main - главный модуль

# Прописать набор методов для каждого модуля
# 1. get_temperature, get_pressure, get_wind_speed
# 2. temperature_logger, pressure_logger, wind_speed_logger
# 3. temperature_view, pressure_view, wind_speed_view
# 4. html_creater
# 5. start_button
# +xml_generator

import html_creater as hc
import xml_generator as xg
import data_provider as dp

# print(hc.create())
# print(xg.create())

hc.new_create(xg.new_create(dp.data_collection()))