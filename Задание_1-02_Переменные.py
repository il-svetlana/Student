quant_complete_HW = 12
quant_wasted_hours = 1.5
course_name = 'Python'
time_exercise = 0

time_exercise = quant_wasted_hours / quant_complete_HW

print('Курс:', course_name, ', всего задач: ', quant_complete_HW, ', затрачено часов: ', quant_wasted_hours, ', среднее время выполнения: ', time_exercise, ' часа.')

# из рекомендованной статьи на Хабре, в конце урока о строках
# через format:
# print('Курс: {}, всего задач: {}, затрачено часов: {}, среднее время выполнения: {} часа.'.format(course_name, quant_complete_HW, quant_wasted_hours, time_exercise))