from Survey import AnonimSurvey
import tkinter

question = "Какой язык вы хотите изучать первым"
my_survey = AnonimSurvey(question)

#показывает вопрос и сохраняет ответ
my_survey.show_question()
print("Введите 'q'  для окончания работы программы \n")
while True:
    response = input("Язык: \n")
    if response == 'q':
        break
    my_survey.store_response(response)

#Показать результаты
print("\n Спасибо за участие в этом опросе")
my_survey.show_results()