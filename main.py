class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка оценки')

    def count_grade(self):
        grade_all = [grade for value in self.grades.values() for grade in value]
        if len(grade_all) > 0:
            grade_sum = sum(grade_all) / len(grade_all)
        else:
            grade_sum = f"Ошибка оценки"
        return grade_sum

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\
            \nСредняя оценка за домашние задания: {self.count_grade()}\
            \nКурсы в процессе изучения: {", ".join(course for course in self.courses_in_progress)}\
            \nЗавершенные курсы: {", ".join(course for course in self.finished_courses)}'
        return res

    def __lt__(self, other):
        if isinstance(other, Student) and isinstance(self.count_grade(), float) and isinstance(other.count_grade(), float):
            return self.count_grade() < other.count_grade()
        else:
            return f'Ошибка сравнения'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def count_grade(self):
        grade_all = [grade for value in self.grades.values() for grade in value]
        if len(grade_all) > 0:
            grade_sum = sum(grade_all) / len(grade_all)
        else:
            grade_sum = f"Сперва оцените преподователя"
        return grade_sum

    def __str__(self):
        about = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_grade()}'
        return about

    def __lt__(self, other):
        if isinstance(other, Lecturer) and isinstance(self.count_grade(), float) and isinstance(other.count_grade(), float):
            return self.count_grade() < other.count_grade()
        else:
            return f'Ошибка сравнения'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка оценки')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def student_gr(lst, course):
    all_g = []
    for student in lst:
        for grade in student.grades[course]:
            all_g.append(grade)
    if len(all_g) > 0:
        return sum(all_g) / len(all_g)
    else:
        return f'Сперва добавте оценки'


def lector_gr(lst, course):
    all_g = []
    for lecturer in lst:
        for grade in lecturer.grades[course]:
            all_g.append(grade)
    if len(all_g) > 0:
        return sum(all_g) / len(all_g)
    else:
        return f'Сперва добавьте оценки'


best_student = Student('Андрей', 'Андреевич', 'Мужик')
best_student.courses_in_progress += ['Python', 'С++']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('Владислав', 'Владиславович', 'Мужик')
best_student2.courses_in_progress += ['Python', 'С++']
best_student2.finished_courses += ['Введение в программирование']

best_lecturer = Lecturer('Анна', 'Иванова')
best_lecturer.courses_attached += ['Python', 'С++']

best_lecturer2 = Lecturer('Виктория', 'Гелеова')
best_lecturer2.courses_attached += ['Python']

cool_reviewer = Reviewer('Геннадий', 'Бруталович')
cool_reviewer.courses_attached += ['Python', 'С++']

cool_reviewer.rate_hw(best_student, 'С++', 1)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'С++', 2)
cool_reviewer.rate_hw(best_student, 'Python', 6)

cool_reviewer.rate_hw(best_student2, 'С++', 3)
cool_reviewer.rate_hw(best_student2, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'С++', 7)
cool_reviewer.rate_hw(best_student2, 'Python', 9)

best_student.rate_lecturer(best_lecturer, 'Python', 2)
best_student.rate_lecturer(best_lecturer, 'Python', 5)
best_student.rate_lecturer(best_lecturer2, 'Python', 6)
best_student.rate_lecturer(best_lecturer2, 'Python', 3)

print(best_student)
print(best_student2)
print(best_lecturer)
print(best_lecturer2)
print(cool_reviewer)
print(best_lecturer > best_lecturer2)
print(best_student < best_student2)
print(student_gr([best_student, best_student2], 'С++'))
print(lector_gr([best_lecturer, best_lecturer2], 'Python'))