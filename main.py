from RUZ import Ruz
import ruz
schedule1 = ruz.person_lessons("aalimonov_2@edu.hse.ru")
#print(schedule1)
ruz = Ruz()
#ruz.get_mail('Кофанова', 'Мария', 'Александровна', 'student')
#r = Ruz.get_schedule_by_full_name('Кофанова Мария Александровна')
r = ruz.find_people('Громова Полина')
print(r)