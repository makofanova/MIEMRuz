from RUZ import Ruz
import ruz
schedule1 = ruz.person_lessons("makofanova@edu.hse.ru")
ruz = Ruz
ruz.get_mail('Кофанова', 'Мария', 'Александровна', 'student')
r = Ruz.get_schedule_by_full_name('Кофанова Мария Александровна')
print(r[0])
