import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas


# page 1
radio_id = [
    ["i9", "i12", "i15", "i18"],
    ["i25", "i28", "i31", "i34", "i37"],
    ["i44", "i47", "i50", "i53"],
    ["i60", "i63", "i66", "i69", "i72"],
    ["i79", "i82"],
    ["i89", "i92", "i95", "i98"],
    ["i105", "i108", "i111"],
    ["i118", "i121", "i124", "i127"],
    ["i137", "i140", "i143", "i146"],
    ["i153", "i156", "i159", "i162", "i165"],
]

# # page2
# radio_id_2 = [
#     ["i5", "i8", "i11", "i14", "i17"],
#     ["i24", "i27", "i30", "i33", "i36"],
#     ["i43", "i46", "i49", "i52", "i55"],
#     ["i62", "i65", "i68", "i71", "i74"],
#     ["i81", "i84", "i87", "i90", "i93"],
# ]
# checkbox_id = [
#     ["i39", "i42", "i45", "i48", "i51"]
# ]

# numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

total_form = int(input("how many form you want to fill\n>> "))
driver = webdriver.Chrome(service=Service('/Users/dhvippatel/Chromedriver/chromedriver'))
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSc-7ti8xN4mfmfqhdCfCbj1V8fuQ5z9l"
           "--nZds482KdveQF0g/viewform?usp=sf_link")

for count in range(total_form):
    name_file = pandas.read_csv("name.csv")
    names = list(name_file["name"])
    NAME = random.choice(names)

    # NUMBER_RANGE = random.randint(2, 3)
    # num = ""
    # for _ in range(NUMBER_RANGE):
    #     num = num + random.choice(numbers)
    # fake_email = NAME + num + "@gmail.com"

    time.sleep(1)

    text_field = driver.find_elements(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                         '/div/div[1]/div/div[1]/input')
    text_field[0].send_keys(NAME)
    time.sleep(2)

    for radio_group in radio_id:
        radio_button = driver.find_element(by=By.ID, value=random.choice(radio_group))
        radio_button.click()
        time.sleep(2)

    # for checkbox_group in checkbox_id:
    #
    #     for _ in range(3):
    #         selecting_times = random.choice(checkbox_group)
    #         checkbox_button = driver.find_element(by=By.ID, value=selecting_times)
    #         checkbox_button.click()
    #         time.sleep(1)
    #     time.sleep(2)
    #
    # next_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    # next_button.click()

    # time.sleep(3)
    # # page 2
    # for radio_group in radio_id_2:
    #     radio_button = driver.find_element(by=By.ID, value=random.choice(radio_group))
    #     radio_button.click()
    #     time.sleep(2)

    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    another_response = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    print(f"[| {count} |]")