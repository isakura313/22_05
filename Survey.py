class AnonimSurvey():
    """Собирает ответы, какой язык человек хочет учить первым """

    def __init__(self, question):
        """ Содержит вопрос и подготавливает список для ответов"""
        self.question = question
        self.responses = []
        #сохранение в JSON
        #сохранение в БД

    def show_question(self):
        """Показать вопрос"""
        print(self.question)

    def store_response(self, new_response):
        """ Сохраняет ответ"""
        self.responses.append(new_response)

    def show_results(self):
        """Показывает все ответы, которые были даны"""
        print("Результаты опроса: ")
        for response in self.responses:
            print(f"-{response}")
