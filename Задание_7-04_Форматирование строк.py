class Team:
    def __init__(self, name, num, time=0, tasks=0):
        self.__name = name
        self.num = num
        self.time = time
        self.tasks = tasks

    def get_name(self):
        return self.__name

    def set_score_tasks(self, new_time, new_tasks):
        self.time += new_time
        self.tasks += new_tasks


team1 = Team('"Мастера кода"', 5)
team2 = Team('"Волшебники данных"', 6)

# Использование %:
print('В команде %s участников: %i' % (team1.get_name(), team1.num))
print('В команде %s участников: %i' % (team2.get_name(), team2.num), '\n')

# Использование format():
team1.set_score_tasks(1552.512, 40)
team2.set_score_tasks(2153.31451, 42)

print('Команда {name} решила задач: {tasks}'.format
      (name=team1.get_name(), tasks=team1.tasks))
print('Команда {name} решила задач: {tasks}'.format
      (name=team2.get_name(), tasks=team2.tasks), '\n')

# Использование f-строк:

print(f'Команды решили {team1.tasks} и {team2.tasks} задач.')

if team1.tasks > team2.tasks or team1.tasks == team2.tasks and team1.time > team2.time:
    result = f'Победа команды {team1.get_name()}!'
elif team1.tasks < team2.tasks or team1.tasks == team2.tasks and team1.time < team2.time:
    result = f'Победа команды {team2.get_name()}!'
else:
    result = 'Ничья!'

tasks_total = team1.tasks + team2.tasks
time_avg = round((team1.time + team2.time) / tasks_total, 2)

print(f'Результат битвы: {result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу.')