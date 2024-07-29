# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def submit_report(client, address, date):
    # Initialize Chrome driver instance
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))


    driver.minimize_window()

    try:
        # Navigate to the URL
        driver.get('https://system.markinform.com.ua/auth')

        # Find the input elements by their name attributes
        login_input = driver.find_element(By.NAME, 'user')
        password_input = driver.find_element(By.NAME, 'pass')

        # Input text into the input fields
        login_input.send_keys('yegorov1995')
        password_input.send_keys('yegorov1995')
        login_input.submit()
        time.sleep(1)
        # Navigate to the report submission page
        link_xpath = "//a[contains(text(), 'Долучити звіт')]"
        link_element = driver.find_element(By.XPATH, link_xpath)
        link_element.click()
        time.sleep(1)
        # Wait for and select the first dropdown
        wait = WebDriverWait(driver, 10)
        dropdown_one = wait.until(EC.presence_of_element_located((By.ID, 'repcli')))
        dropdown_select_one = Select(dropdown_one)
        dropdown_select_one.select_by_visible_text(client)
        time.sleep(1)
        # Wait for and select the second dropdown
        dropdown_thoo = wait.until(EC.presence_of_element_located((By.ID, 'repshop')))
        dropdown_select_thoo = Select(dropdown_thoo)
        dropdown_select_thoo.select_by_visible_text(address)
        time.sleep(2)
        # Input the correct date
        date_input = driver.find_element(By.NAME, 'date')
        date_input.clear()
        # date_correct = '2023-11-12'
        date_input.send_keys(date_correct)
        # Upload the image
        file_input_img = driver.find_element(By.NAME, 'picta[]')
        file_path = r'C:\Users\Alex\PycharmProjects\pythonProject\image.jpg'  # Replace with the actual path to your image file
        file_input_img.send_keys(file_path)
        time.sleep(1)

        # Click the submit button
        submit_button = driver.find_element(By.NAME, 'sub')
        submit_button.click()

    finally:
        # Close the driver
        driver.quit()

def epicentr():
    # list_client = ['Хімекспрес', 'Мікрофільтр']

    # list_client = ['Сіді Груп', 'Терра-Пак']

    # list_client = ['Терра-Пак']

    list_client = ['Терра-Пак', 'Флагман УТК', 'ДарПак', 'УкрХімТех', 'Сіді Груп', 'Лайт Груп', 'АТ Укртойс', 'ЗОЗ ЮА', 'Кантрі Трейд Компані']
    address = 'Епіцентр, м.Бровари вул.Київська 253'
    for index in range(0, len(list_client)):
        client = list_client[index]
        print(f"Index: {index}, Client: {client}")
        submit_report(client, address, date_correct)


def ashan_hot():
    # list_client = ['Поларіс-С']

    list_client = ['Аміго І С', 'Імпортплюс']

    # list_client = ['Аміго І С', 'Імпортплюс', 'Карапуз', 'Біофарма', 'Діст Сістем', 'Сіді Груп',
    #                 'КС Маркет', 'Брати Самонови']

    address = 'Ашан, м.Київ вул.Г.Хоткевича 1Б(ТРЦ Проспект)'
    for index in range(0, len(list_client)):
        client = list_client[index]
        print(f"Index: {index}, Client: {client}")
        submit_report(client, address, date_correct)

def ashan_zdo():
    list_client = ['Поларіс-С']
    # list_client = ['Аміго І С', 'Імпортплюс']

    # list_client = ['Поларіс-С', 'Аміго І С', 'Імпортплюс', 'Карапуз', 'Біофарма', 'Діст Сістем', 'Сіді Груп',
    #                 'КС Маркет', 'Брати Самонови']
    address = 'Ашан, м.Київ вул.Здолбунівська 17'
    for index in range(0, len(list_client)):
        client = list_client[index]
        print(f"Index: {index}, Client: {client}")
        submit_report(client, address, date_correct)

def sid_varus():
    client = 'Сі Джі Трейд'

    list_address = ['Варус, м.Київ №533 вул.Драгаманова 40Г', 'Варус, м.Київ №510 вул.А.Малишка 3', 'Варус, м.Київ №518 пр-т Бажана 38']
    for index in range(0, len(list_address)):
        address = list_address[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)
def ble_comfi():
    client = 'Блейк Груп'
    # 'Фокстрот, м.Київ пр-т Визволителів 17',
    list_address = ['Фокстрот, м.Київ вул.Гната Хоткевича 1-В (ТРК Проспект)', 'Фокстрот, м.Київ вул.Здолбунівська 17 (ТЦ Rive Gauche)', 'Comfy, м.Київ вул.Гната Хоткевича 1В (ТРК Проспект)']
    for index in range(0, len(list_address)):
        address = list_address[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)

def mar_prod():
    client = 'Марко Продукт'
    list_address = ['Сільпо, м.Київ пр-т П.Тичини 1В', 'Сільпо, м.Бровари вул.Київська 241', 'Варус, м.Київ №533 вул.Драгаманова 40Г', 'Варус, м.Київ №510 вул.А.Малишка 3', 'Сільпо, м.Бровари вул.Київська 156', 'Сільпо, м.Київ вул.Мишуги 4']# 'Варус, м.Київ №518 пр-т Бажана 38', 'Сільпо, м.Бровари вул.Київська 241', 'Сільпо, м.Бровари вул.Київська 156']
    for index in range(0, len(list_address)):
        address = list_address[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)
def sid_silpo():
    client = 'Сі Джі Трейд'

    list_address = ['Сільпо, м.Київ вул.Мишуги 4', 'Сільпо, м.Бровари вул.Київська 241', 'Сільпо, м.Київ вул.Ревуцького 12/1А', 'Сільпо, м.Київ вул.Драгоманова 10', 'Сільпо, м.Бровари вул.Київська 241', 'Сільпо, м.Бровари вул.Київська 156']
    for index in range(0, len(list_address)):
        address = list_address[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)


def gra_varus():
    client = 'Еко-Гранула'
    # list_adres = ['Варус, м.Київ №533 вул.Драгаманова 40Г', 'Варус, м.Київ №518 пр-т Бажана 38', 'Варус, м.Київ №529 вул.Ревуцького 40/2', 'Варус, м.Бровари №508 вул.Героїв України 16', 'Варус, м.Київ №510 вул.А.Малишка 3']
    list_adres = ['Варус, м.Київ №533 вул.Драгаманова 40Г', 'Варус, м.Київ №529 вул.Ревуцького 40/2', 'Варус, м.Київ №518 пр-т Бажана 38', 'Варус, м.Київ №502 пр-т М.Бажана 10А', 'Варус, м.Бровари №521 вул.Київська 239', 'Варус, м.Київ №510 вул.А.Малишка 3', 'Варус, м.Бровари №508 вул.Героїв України 16', 'Варус, м.Бровари №506 вул.Чорних Запорожців 72']
    for index in range(0, len(list_adres)):
        address = list_adres[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)

def dis_var():
    client = 'Діст Сістем'
    list_adres = ['Варус, м.Бровари №521 вул.Київська 239', 'Варус, м.Бровари №508 вул.Героїв України 16', 'Варус, м.Бровари №506 вул.Чорних Запорожців 72']

    for index in range(0, len(list_adres)):
        address = list_adres[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)
def sum_fora():
    client = 'Сумський завод продтоварів'
    # list_adres = ['Фора, м.Бровари вул.Грушевського 17', 'Фора, м.Бровари вул.Шевченка 10В', 'Фора, м.Бровари вул.С.Москаленка 39', 'Фора, м.Бровари вул.Онікієнка 20/2', 'Фора, м.Бровари вул.Незалежності 7', 'Фора, м.Бровари вул.Київська 92', 'Фора, м.Бровари вул.Київська 4', 'Фора, м.Бровари вул.Броварської Сотні 12', 'Фора, м.Київ пр-т Броварський 51', 'Фора, м.Київ вул.Ревуцького 26', 'Фора, м.Київ вул.Драгоманова 19', 'Фора, м.Київ вул.Горлівська 124/143']
    # list_adres = ['Фора, м.Бровари вул.Шевченка 10В', 'Фора, м.Бровари вул.С.Москаленка 39', 'Фора, м.Бровари вул.Онікієнка 20/2', 'Фора, м.Бровари вул.Незалежності 7', 'Фора, м.Київ пр-т Броварський 51', 'Фора, м.Київ вул.Ревуцького 26', 'Фора, м.Київ вул.Драгоманова 19','Фора, м.Бровари вул.С.Москаленка 39', ]
    list_adres = ['Фора, м.Київ вул.Драгоманова 19', 'Фора, м.Київ вул.Ревуцького 26',
                  'Фора, м.Бровари вул.Грушевського 17',
                  'Фора, м.Київ пр-т Броварський 51', 'Фора, м.Бровари вул.Київська 4',
                  'Фора, м.Бровари вул.Київська 92',
                  'Фора, м.Бровари вул.Онікієнка 20/2', 'Фора, м.Київ вул.Вереснева 24']
    for index in range(0, len(list_adres)):
        address = list_adres[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)


def sum_var():
    client = 'Сумський завод продтоварів'
    list_adres = ['Варус, м.Київ №512 Харківське шосе 160', 'Варус, м.Київ №533 вул.Драгаманова 40Г', 'Варус, м.Київ №529 вул.Ревуцького 40/2', 'Варус, м.Київ №518 пр-т Бажана 38', 'Варус, м.Київ №502 пр-т М.Бажана 10А', 'Варус, м.Бровари №521 вул.Київська 239', 'Варус, м.Київ №510 вул.А.Малишка 3']
    for index in range(0, len(list_adres)):
        address = list_adres[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)

def nat_fora():
    client = 'Натурпро'
    list_adres = ['Фора, м.Бровари вул.Київська 4']
    # list_adres = ['Фора, м.Бровари вул.Київська 4', 'Фора, м.Бровари вул.Шевченка 10В', 'Фора, м.Бровари вул.С.Москаленка 39']
    for index in range(0, len(list_adres)):
        address = list_adres[index]
        print(f"Index: {index}, address: {address}")
        submit_report(client, address, date_correct)

def eco_log():
    client = 'Еко Логічно'
    # list_adres = ['Сільпо, м.Київ вул.Драгоманова 10', 'Новус, м.Київ №7024 вул.Тростянецька 1А', 'Сільпо, м.Бровари вул.Київська 156', 'Сільпо, м.Бровари вул.Київська 241', 'Новус, м.Бровари №1079 вул.Київська 253']
    # list_adres =['Сільпо, м.Київ пр-т П.Тичини 1В', 'Новус, м.Київ №7031 пл.Дарницька 1', 'Новус, м.Київ №7022 вул.Будівельників 40', 'Новус, м.Київ №1038 вул.Гната Хоткевича 1А', 'Новус, м.Бровари №1079 вул.Київська 253']
    list_adres = ['Сільпо, м.Київ вул.Березнева 12А', 'Сільпо, м.Київ пр-т П.Тичини 1В', 'Сільпо, м.Київ вул.Драгоманова 10', 'Сільпо, м.Бровари вул.Київська 156', 'Сільпо, м.Бровари вул.Київська 241']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)

def sum_sil():
    client = 'Сумський завод продтоварів'
    # list_adres = ['Сільпо, м.Бровари вул.Київська 156', 'Сільпо, м.Київ вул.Драгоманова 10', 'Сільпо, м.Київ вул.Ревуцького 12/1А', 'Сільпо, м.Бровари вул.Київська 241']
    list_adres = ['Сільпо, м.Київ наб.Русанівська 10', 'Сільпо, м.Київ вул.Драгоманова 10']

    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def vol_nov():
    client = 'Волхов'
    # list_adres = ['Сільпо, м.Бровари вул.Київська 156', 'Сільпо, м.Київ вул.Драгоманова 10', 'Сільпо, м.Київ вул.Ревуцького 12/1А', 'Сільпо, м.Бровари вул.Київська 241']
    list_adres = ['Новус, м.Київ №1045 пр-т Броварський 18Д']

    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def vit_sil():
    client = 'Ві та Ві Дизайн'

    # list_adres = ['Сільпо, м.Бровари вул.Київська 241', 'Сільпо, м.Київ вул.Мишуги 4', 'Сільпо, м.Київ Харківське шосе 168', 'Сільпо, м.Київ Харківське шосе 21',  'Офтоп, м.Бровари вул.Київська 241', 'Офтоп, м.Київ Харківське шосе 168']
    list_adres = ['Сільпо, м.Бровари вул.Київська 241', 'Сільпо, м.Київ вул.Ревуцького 12/1А', 'Сільпо, м.Київ вул.Драгоманова 10', 'Сільпо, м.Бровари вул.Київська 156']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def ara_pas():
    client = 'Арахісова паста ТОМ'
    list_adres = ['Сільпо, м.Бровари вул.Київська 241']
    # list_adres = ['Сільпо, м.Київ вул.Ревуцького 12/1А', 'Сільпо, м.Київ вул.Драгоманова 10', 'Сільпо, м.Київ вул.Мишуги 4', 'Сільпо, м.Бровари вул.Київська 156', 'Сільпо, м.Бровари вул.Київська 241']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def sto_sil():
    client = 'Столяр Д.Ю'
    list_adres = ['Новус, м.Київ №7036 вул.М.Гришка 3', 'Новус, м.Київ №7024 вул.Тростянецька 1А', 'Новус, м.Київ №1045 пр-т Броварський 18Д']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def ami_sil():
    client = 'Аміго І С'
    list_adres = ['Новус, м.Київ №7024 вул.Тростянецька 1А']
    # list_adres = ['Сільпо, м.Бровари вул.Київська 241', 'Сільпо, м.Київ Харківське шосе 168',  'Новус, м.Бровари №1079 вул.Київська 253']
    # list_adres = ['Сільпо, м.Бровари вул.Київська 241', 'Новус, м.Київ №7024 вул.Тростянецька 1А', 'Новус, м.Київ №1045 пр-т Броварський 18Д', 'Новус, м.Київ №7036 вул.М.Гришка 3']

    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)

def at_con_sil():
    # client = 'АТ Укртойс'
    client = 'Конюша А.О. ФОП'
    list_adres = ['Сільпо, м.Бровари вул.Київська 241']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def sil_241():
    list_client = ['АТ Укртойс', 'Аміго І С', 'Брати Самонови', 'Сумський завод продтоварів', 'Сі Джі Трейд', 'Еко Логічно', '']

    address = 'Сільпо, м.Бровари вул.Київська 241'
    for index in range(5, 6):
        client = list_client[index]
        print(f"Index: {index}, Client: {client}")
        submit_report(client, address, date_correct)

def nov_250():
    list_client = ['Аміго І С', 'Ві та Ві Дизайн', 'Еко Логічно']
    address = 'Новус, м.Бровари №1079 вул.Київська 253'
    for index in range(1, len(list_client)):
        client = list_client[index]
        print(f"Index: {index}, Client: {client}")
        submit_report(client, address, date_correct)
def sum_eco():
        client = 'Сумський завод продтоварів'
        list_adres = ['Еко, м.Київ вул.О.Пчілки 2Б', 'Еко, м.Київ вул.Крупської 4', 'Еко, м.Київ вул.Драгоманова 29А']
        for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def luc_sil():
    list_client = ['Луцишин А.М.']

    address = 'Сільпо, м.Бровари вул.Київська 156'
    for index in range(0, len(list_client)):
        client = list_client[index]
        print(f"Index: {index}, Client: {client}")
        submit_report(client, address, date_correct)

def him_sil():
    client = 'Хімекспрес'

    list_adres = ['Сільпо, м.Бровари вул.Київська 241', 'Сільпо, м.Київ Харківське шосе 168', 'Сільпо, м.Київ Харківське шосе 144Б']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)

def bra_sam():
    client = 'Брати Самонови'
    list_adres = ['Сільпо, м.Київ вул.Драгоманова 10']
    # list_adres = ['Новус, м.Бровари №1079 вул.Київська 253', 'Сільпо, м.Бровари вул.Київська 156']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
# count =1
# x= 2
# while count < x:
#     count+=1

def dia_rc():
    client = 'Диад–Логістик'
    list_adres = ['Форум, м.Бровари вул.Чорних Запорожців 60, 1-й пов.', 'RC, м.Бровари вул.Київська 288']

    # list_adres = ['Bonus mart, м.Бровари вул.Героїв Небесної Сотні 5, 1-й пов.', 'RC, м.Бровари бул.Незалежності 16А', 'RC, м.Бровари бул.Незалежності 17', 'RC, м.Бровари бул.Незалежності 6', 'RC, м.Бровари вул.Київська 288', 'RC, м.Бровари вул.Москаленка 10А', 'RC, м.Бровари вул.Савченка 1', 'Форум, м.Бровари вул.Москаленка 25/1, 1-й пов.', 'Форум, м.Бровари вул.Чорних Запорожців 60, 1-й пов.']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)

def ugf_sil():
    client = 'ЮГФУД'

    list_adres = ['Сільпо, м.Київ пр-т П.Тичини 1В', 'Сільпо, м.Київ вул.Ревуцького 12/1А']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def vvn_eva():
    client = 'ВВН'

    list_adres = ['EVA, м.Київ пр-т Броварський 33-В']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def stu_sil():
    client = 'Студія Марко'

    list_adres = ['Сільпо, м.Київ вул.Ревуцького 12/1А']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
def sol_nov():
    client = 'Екосолум'
    # , 'Новус, м.Київ №7031 пл.Дарницька 1'
    list_adres = ['Новус, м.Бровари №1079 вул.Київська 253', 'Новус, м.Київ №1038 вул.Гната Хоткевича 1А']
    for index in range(0, len(list_adres)):
            address = list_adres[index]
            print(f"Index: {index}, address: {address}")
            submit_report(client, address, date_correct)
            submit_report(client, address, date_correct)

def meg_mar():
    list_client = ['Еко Логічно', 'Альфа Трейдінг Україна']

    address = 'Мега Маркет, м.Бровари вул.Київська 316'

    for index in range(0, len(list_client)):
        client = list_client[index]
        print(f"Index: {index}, Client: {client}")
        submit_report(client, address, date_correct)

# # Call the function to submit the report
#
# dia_rc()
#
date_correct = '2024-07-30'
#
# eco_log()
#
# vvn_eva()
#
# date_correct = '2024-07-26'
#
# epicentr()
#
# ashan_hot()
#
# ashan_zdo()
#
# sid_varus()
#
sid_silpo()
#
# dis_var()
#
# gra_varus()
#
# sum_fora()
#
# sum_var()
#
# sum_sil()
#
# vol_nov()
#
# ara_pas()
#
# vit_sil()
#
# nat_fora()
#
# ami_sil()
#
# sto_sil()
#
# at_con_sil()
#
# bra_sam()
#
# mar_prod()
#
# sum_eco()
#
# him_sil()
#
# ugf_sil()
#
# stu_sil()
#
# meg_mar()
#
# sil_241()
#
# nov_250()
#
# luc_sil()
#
# ble_comfi()
#
# sol_nov()
#

