import random

students_keys = ['girl', 'is18', 'glasses', 'brownEyes', 'darkHair', 'siblings', 'pet', 'fromSPb', 'iphone', 'tushavin', 'coffe', 'homefood', 'watch', 'nameVowel', 'pizza', 'smoke', 'heightOver175', 'partner', 'winterOrSpring', 'gaming', 'campus', 'movies', 'anime']
students = [
    {
        "name": "Бабаев Руслан",
        "girl": False,
        "is18": True,
        "glasses": False,
        "brownEyes": True,
        "darkHair": True,
        "siblings": True,
        "pet": True,
        "fromSPb": False,
        "iphone": False,
        "tushavin": False,
        "coffe": False,
        "homefood": False,
        "watch": False,
        "nameVowel": False,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": True,
        "winterOrSpring": True,
        "gaming": False,
        "campus": False,
        "movies": False,
        "anime": True,
    },
    {
        "name": "Шестаков Максим Олегович",
        "girl": False,
        "is18": True,
        "glasses": True,
        "brownEyes": False,
        "darkHair": True,
        "siblings": True,
        "pet": True,
        "fromSPb": False,
        "iphone": True,
        "tushavin": True,
        "coffe": True,
        "homefood": True,
        "watch": True,
        "nameVowel": False,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": True,
        "winterOrSpring": True,
        "gaming": False,
        "campus": False,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Боженко Мария Александровна",
        "girl": True,
        "is18": False,
        "glasses": True,
        "brownEyes": True,
        "darkHair": True,
        "siblings": False,
        "pet": True,
        "fromSPb": True,
        "iphone": True,
        "tushavin": True,
        "coffe": True,
        "homefood": False,
        "watch": False,
        "nameVowel": False,
        "pizza": False,
        "smoke": False,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": False,
        "gaming": False,
        "campus": False,
        "movies": True,
        "anime": True,
    },
    {
        "name": "Шишминцев Дмитрий Владимирович",
        "girl": False,
        "is18": True,
        "glasses": True,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": True,
        "iphone": True,
        "tushavin": True,
        "coffe": False,
        "homefood": False,
        "watch": False,
        "nameVowel": False,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": True,
        "winterOrSpring": True,
        "gaming": False,
        "campus": False,
        "movies": False,
        "anime": False,
    },
    {
        "name": "Затикян Сергей Арменович",
        "girl": False,
        "is18": True,
        "glasses": True,
        "brownEyes": True,
        "darkHair": True,
        "siblings": True,
        "pet": True,
        "fromSPb": True,
        "iphone": True,
        "tushavin": True,
        "coffe": True,
        "homefood": True,
        "watch": True,
        "nameVowel": False,
        "pizza": True,
        "smoke": True,
        "heightOver175": True,
        "partner": True,
        "winterOrSpring": False,
        "gaming": False,
        "campus": False,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Шаллиева Вера Владимировна",
        "girl": True,
        "is18": False,
        "glasses": True,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": True,
        "iphone": False,
        "tushavin": True,
        "coffe": False,
        "homefood": False,
        "watch": False,
        "nameVowel": False,
        "pizza": False,
        "smoke": False,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": False,
        "gaming": False,
        "campus": False,
        "movies": True,
        "anime": True,
    },
    {
        "name": "Смирнов Игорь Иванович",
        "girl": False,
        "is18": True,
        "glasses": False,
        "brownEyes": True,
        "darkHair": True,
        "siblings": False,
        "pet": False,
        "fromSPb": False,
        "iphone": False,
        "tushavin": True,
        "coffe": False,
        "homefood": True,
        "watch": True,
        "nameVowel": True,
        "pizza": True,
        "smoke": False,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": True,
        "gaming": True,
        "campus": True,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Абдулов Илья Александрович",
        "girl": False,
        "is18": True,
        "glasses": True,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": False,
        "fromSPb": False,
        "iphone": True,
        "tushavin": False,
        "coffe": False,
        "homefood": True,
        "watch": False,
        "nameVowel": True,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": False,
        "winterOrSpring": False,
        "gaming": True,
        "campus": False,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Кремпольская Екатерина Александровна",
        "girl": True,
        "is18": True,
        "glasses": True,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": False,
        "iphone": False,
        "tushavin": False,
        "coffe": False,
        "homefood": True,
        "watch": False,
        "nameVowel": True,
        "pizza": False,
        "smoke": False,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": True,
        "gaming": False,
        "campus": False,
        "movies": False,
        "anime": True,
    },
    {
        "name": "Касьяненко Вера Михайловна",
        "girl": True,
        "is18": False,
        "glasses": False,
        "brownEyes": True,
        "darkHair": True,
        "siblings": True,
        "pet": True,
        "fromSPb": True,
        "iphone": False,
        "tushavin": True,
        "coffe": True,
        "homefood": True,
        "watch": True,
        "nameVowel": False,
        "pizza": True,
        "smoke": False,
        "heightOver175": False,
        "partner": True,
        "winterOrSpring": True,
        "gaming": False,
        "campus": False,
        "movies": True,
        "anime": True,
    },
    {
        "name": "Язев Григорий",
        "girl": False,
        "is18": False,
        "glasses": False,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": True,
        "iphone": False,
        "tushavin": True,
        "coffe": False,
        "homefood": False,
        "watch": False,
        "nameVowel": False,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": False,
        "winterOrSpring": True,
        "gaming": False,
        "campus": False,
        "movies": False,
        "anime": True,
    },
    {
        "name": "Алексеев Тимофей Юрьевич",
        "girl": False,
        "is18": False,
        "glasses": False,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": False,
        "iphone": True,
        "tushavin": False,
        "coffe": True,
        "homefood": True,
        "watch": True,
        "nameVowel": False,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": False,
        "winterOrSpring": False,
        "gaming": False,
        "campus": True,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Горлов Игорь",
        "girl": False,
        "is18": True,
        "glasses": False,
        "brownEyes": False,
        "darkHair": True,
        "siblings": True,
        "pet": True,
        "fromSPb": False,
        "iphone": False,
        "tushavin": False,
        "coffe": False,
        "homefood": True,
        "watch": False,
        "nameVowel": True,
        "pizza": True,
        "smoke": False,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": True,
        "gaming": True,
        "campus": True,
        "movies": True,
        "anime": True,
    },
    {
        "name": "Садовая Анастасия Романовна",
        "girl": True,
        "is18": False,
        "glasses": False,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": False,
        "iphone": False,
        "tushavin": False,
        "coffe": True,
        "homefood": True,
        "watch": True,
        "nameVowel": True,
        "pizza": False,
        "smoke": False,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": True,
        "gaming": False,
        "campus": True,
        "movies": False,
        "anime": False,
    },
    {
        "name": "Надери Мариам Шаховна ",
        "girl": True,
        "is18": True,
        "glasses": True,
        "brownEyes": False,
        "darkHair": True,
        "siblings": True,
        "pet": True,
        "fromSPb": True,
        "iphone": False,
        "tushavin": True,
        "coffe": False,
        "homefood": True,
        "watch": False,
        "nameVowel": False,
        "pizza": False,
        "smoke": False,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": True,
        "gaming": False,
        "campus": False,
        "movies": False,
        "anime": True,
    },
    {
        "name": "Оншин Дмитрий Николаевич",
        "girl": False,
        "is18": True,
        "glasses": False,
        "brownEyes": False,
        "darkHair": True,
        "siblings": True,
        "pet": False,
        "fromSPb": True,
        "iphone": True,
        "tushavin": False,
        "coffe": True,
        "homefood": True,
        "watch": True,
        "nameVowel": False,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": True,
        "winterOrSpring": True,
        "gaming": True,
        "campus": False,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Петрова Наталья Глебовна ",
        "girl": True,
        "is18": True,
        "glasses": True,
        "brownEyes": False,
        "darkHair": False,
        "siblings": False,
        "pet": False,
        "fromSPb": True,
        "iphone": True,
        "tushavin": False,
        "coffe": False,
        "homefood": True,
        "watch": True,
        "nameVowel": False,
        "pizza": False,
        "smoke": False,
        "heightOver175": True,
        "partner": True,
        "winterOrSpring": True,
        "gaming": False,
        "campus": False,
        "movies": False,
        "anime": False,
    },
    {
        "name": "Кабдулвахитов Эмир Ержанович ",
        "girl": False,
        "is18": True,
        "glasses": True,
        "brownEyes": True,
        "darkHair": True,
        "siblings": True,
        "pet": False,
        "fromSPb": False,
        "iphone": True,
        "tushavin": True,
        "coffe": True,
        "homefood": False,
        "watch": False,
        "nameVowel": True,
        "pizza": True,
        "smoke": True,
        "heightOver175": True,
        "partner": False,
        "winterOrSpring": False,
        "gaming": True,
        "campus": True,
        "movies": True,
        "anime": True,
    },
    {
        "name": "Авокадо Ева Сергеевна",
        "girl": True,
        "is18": False,
        "glasses": True,
        "brownEyes": False,
        "darkHair": True,
        "siblings": False,
        "pet": True,
        "fromSPb": False,
        "iphone": False,
        "tushavin": True,
        "coffe": False,
        "homefood": True,
        "watch": False,
        "nameVowel": True,
        "pizza": True,
        "smoke": False,
        "heightOver175": False,
        "partner": True,
        "winterOrSpring": False,
        "gaming": True,
        "campus": False,
        "movies": False,
        "anime": False,
    },
    {
        "name": "Царёв Александр Сергеевич",
        "girl": False,
        "is18": True,
        "glasses": False,
        "brownEyes": False,
        "darkHair": False,
        "siblings": False,
        "pet": False,
        "fromSPb": True,
        "iphone": True,
        "tushavin": True,
        "coffe": False,
        "homefood": False,
        "watch": False,
        "nameVowel": True,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": False,
        "winterOrSpring": False,
        "gaming": True,
        "campus": False,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Адрат Олеся Александровна ",
        "girl": True,
        "is18": True,
        "glasses": False,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": True,
        "iphone": True,
        "tushavin": False,
        "coffe": False,
        "homefood": True,
        "watch": False,
        "nameVowel": True,
        "pizza": False,
        "smoke": False,
        "heightOver175": True,
        "partner": True,
        "winterOrSpring": False,
        "gaming": False,
        "campus": False,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Комелин Глеб Александрович",
        "girl": False,
        "is18": True,
        "glasses": False,
        "brownEyes": False,
        "darkHair": True,
        "siblings": True,
        "pet": True,
        "fromSPb": False,
        "iphone": True,
        "tushavin": True,
        "coffe": True,
        "homefood": True,
        "watch": False,
        "nameVowel": False,
        "pizza": False,
        "smoke": True,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": False,
        "gaming": True,
        "campus": True,
        "movies": False,
        "anime": False,
    },
    {
        "name": "Миляев Дмитрий Дмитриевич",
        "girl": False,
        "is18": True,
        "glasses": True,
        "brownEyes": False,
        "darkHair": False,
        "siblings": False,
        "pet": True,
        "fromSPb": False,
        "iphone": True,
        "tushavin": False,
        "coffe": True,
        "homefood": True,
        "watch": False,
        "nameVowel": False,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": True,
        "winterOrSpring": False,
        "gaming": False,
        "campus": False,
        "movies": True,
        "anime": False,
    },
    {
        "name": "Телунц Эдуард Рубенович",
        "girl": False,
        "is18": True,
        "glasses": False,
        "brownEyes": True,
        "darkHair": True,
        "siblings": True,
        "pet": False,
        "fromSPb": False,
        "iphone": False,
        "tushavin": False,
        "coffe": False,
        "homefood": True,
        "watch": False,
        "nameVowel": True,
        "pizza": True,
        "smoke": False,
        "heightOver175": True,
        "partner": False,
        "winterOrSpring": False,
        "gaming": False,
        "campus": True,
        "movies": False,
        "anime": False,
    },
    {
        "name": "Белисов Глеб",
        "girl": False,
        "is18": True,
        "glasses": False,
        "brownEyes": True,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": False,
        "iphone": True,
        "tushavin": True,
        "coffe": True,
        "homefood": True,
        "watch": False,
        "nameVowel": False,
        "pizza": False,
        "smoke": False,
        "heightOver175": False,
        "partner": False,
        "winterOrSpring": False,
        "gaming": True,
        "campus": True,
        "movies": False,
        "anime": True,
    },
    {
        "name": "Конопля Алексей Константинович ",
        "girl": False,
        "is18": False,
        "glasses": True,
        "brownEyes": False,
        "darkHair": False,
        "siblings": True,
        "pet": True,
        "fromSPb": True,
        "iphone": True,
        "tushavin": True,
        "coffe": False,
        "homefood": False,
        "watch": False,
        "nameVowel": True,
        "pizza": False,
        "smoke": True,
        "heightOver175": True,
        "partner": False,
        "winterOrSpring": True,
        "gaming": True,
        "campus": False,
        "movies": True,
        "anime": True,
    },
]

questions = {"girl": "Студент девушка?",
        "is18": "Студенту есть 18?",
        "glasses": "Студент носит очки?",
        "brownEyes": "У студента карие глаза?",
        "darkHair": "У студента черные волосы?",
        "siblings": "У студента есть брат или сестра?",
        "pet": "У студента есть домашнее животное?",
        "fromSPb": "Студент из Санкт-Петербурга?",
        "iphone": "У студента есть Iphone?",
        "tushavin": "Студент учится у Тушавина?",
        "coffe": "Студенту нравится кофе больше чем чай?",
        "homefood": "Студенту нравится больше домашняя еда чем фастфуд?",
        "watch": "Студент носит часы?",
        "nameVowel": "Полное имя студента начинается с гласной?",
        "pizza": "Студент любит пиццу больше чем суши?",
        "smoke": "Студент курит?",
        "heightOver175": "Студент ростом выше 175 см?",
        "partner": "У студента есть вторая половинка?",
        "winterOrSpring": "Студент родился зимой или весной?",
        "gaming": "Студент играет в CS GO или в Dota 2?",
        "campus": "Студент живет в общежитии?",
        "movies": "Студент предпочитает больше фильмы чем сериалы?",
        "anime": "Студент смотрит аниме?"}



while (len(students) > 1):
    random_question = random.randint(0, len(questions) - 1)
    print(questions[students_keys[random_question]])
    answer = input()
    if (answer == "да") or (answer == "Да"):
        truth_of_answer = True
    elif (answer == "нет") or (answer == "Нет"):
        truth_of_answer = False

    i = 0
    while (i < len(students)):
        if students[i][students_keys[random_question]] != truth_of_answer:
            students.pop(i)
        else:
            i += 1
    questions.pop(students_keys[random_question])
    students_keys.pop(random_question)


if len(students) == 0:
    print("Студента с введенными характеристиками не существует")
else:
    print(students[0]["name"])









