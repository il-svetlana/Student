import time

class UrTube:

    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        flag = False

        for user in self.users:
            if user.nickname == nickname:
                flag = True

                if user.password == hash(password):
                    self.current_user = user
                    print(f'Пользователь {user.nickname} авторизован')
                else:
                    print('Пароль не совпадает.')

        if not flag:
            print(f'Пользователь {nickname} не зарегистрирован.')

    def register(self, obj_user):
        if obj_user in self.users:
            print('Пользователь с таким ником уже зарегистрирован.')
        else:
            self.users.append(obj_user)
            self.current_user = obj_user
            print(f'Пользователь {obj_user.nickname} успешно зарегистрирован.')
            print(f'Пользователь {obj_user.nickname} авторизован')

    def log_out(self):
        print(f'Пользователь {self.current_user.nickname} вышел из системы.')
        self.current_user = None

    def add(self, *args):
        for i in args:
            if not i in self.videos:
                self.videos.append(i)

    def get_videos(self, find_word):
        flag = False
        if find_word:
            print(f'По вашему запросу "{find_word}" найдены видео: ')
            for i in self.videos:
                if find_word.upper() in i.title.upper():
                    flag = True
                    print(i.title, ' ')
            if not flag:
                print('Совпадений не обнаружено.')
        else:
            print('Параметры поиска не заданы')

    def list_users(self):
        print('Список зарегистрированных пользователей: ')
        for user in ur.users:
            print(user.nickname)
        print('')

    def watch_video(self, name_video):
        flag = False

        for video in self.videos:
            if video.title == name_video:
                flag = True

                if not self.current_user:
                    print('Для просмотра видео авторизуйтесь в системе.')
                elif video.adult_mode == True and self.current_user.age <= 18:
                    print('Данное видео не предназначено дял просмотра лицами младше 18 лет.')
                else:
                    print(f'Видео "{video.title}" найдено. Просмотр: ')

                    for timing in range(video.time_now, video.duration):
                        print(video.time_now)
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео.')

        if not flag:
            print('Видео не найдено')
# ---------------
class Video:

    def __init__(self, title, duration, adult_mode = False, time_now = 0):

    # duration - продолжительность, секунды
    # time_now - секунда остановки
    # adult_mode  - ограничение по возрасту

        if title:
            self.title = title
        else:
            print('Ошибка. Объект класса Video не был создан')
            return None

        if duration != 0:
            if isinstance(duration, int):
                self.duration = duration
            elif duration.isnumeric():
                self.duration = duration
            else:
                print('Ошибка. Объект класса Video не был создан')
                print(f'Значение duration для объекта {title} класса Video некорректно.')
                return None
        else:
            print('Ошибка. Объект класса Video не был создан')
            print(f'Значение duration для объекта {title} класса Video некорректно.')
            return None

        self.adult_mode = adult_mode
        self.time_now = time_now

    def __getattr__(self, title):
        if not title:
            return None
# ---------------
class User:

    def __init__ (self, nickname, password, age):
        if nickname:
            self.nickname = nickname
        else:
            print('Ошибка. Объект класса User не был создан')
            return None

        if password:
            self.password = hash(password)
        else:
            print('Ошибка. Объект класса User не был создан')
            return None

        if age != 0:
            if isinstance(age, int):
                self.age = age
            elif age.isnumeric():
                self.age = age
            else:
                print('Ошибка. Объект класса User не был создан')
                print(f'Значение age для объекта {nickname} класса User некорректно.')
                return None
        else:
            print('Ошибка. Объект класса User не был создан')
            print(f'Значение age для объекта {nickname} класса User некорректно.')
            return None

    def __getattr__(self, nickname):
        if not nickname:
            return None
# ---------------
# Базовые значения

ur = UrTube()
video001 = Video('Stationeers глазами новичка', 12)
video002 = Video('Стрельба в ТЦ!', 5, adult_mode = True)
video003 = Video('Как Assembler стал главной фишкой Stationeers', 17)
user1 = User('Deuterium', 204710, 31)
user2 = User('Millenius', 186749, 15)

# Поиск
ur.add(video001, video002, video003)
ur.get_videos('stationeers')
print('')

# Регистрация пользователей
ur.register(user1)
ur.log_out()
ur.register(user2)
ur.log_out()
print('')
ur.list_users()

# Авторизация пользователя
ur.log_in(user1.nickname, user1.password)

# Просмотр видео
ur.watch_video(video002.title)



