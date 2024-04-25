import requests

question = input("Введите ваш вопрос: ")
url = "https://yesno.wtf/api"
params = {"question": question}
response = requests.get(url, params=params)

if response.status_code == 200:
    answer = response.json()["answer"]
    print(f"Ответ на Ваш вопрос: {answer}")
else:
    print("При получении ответа произошла ошибка.")


