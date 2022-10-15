years_animals_collection = {2000: 'Дракон',
                            2001: 'Змея',
                            2002: 'Лошадь',
                            2003: 'Овца',
                            2004: 'Обезьяна',
                            2005: 'Петух',
                            2006: 'Собака',
                            2007: 'Свинья',
                            2008: 'Крыса',
                            2009: 'Бык',
                            2010: 'Тигр',
                            2011: 'Заяц'}

input_year = int(input())

for year in range(2000, 2012):
    if not (year - input_year) % 12:
        print(years_animals_collection[year])


