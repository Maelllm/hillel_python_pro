class Teachers:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def course(self, course):
        self.course = course
        self.course_set = set()
        self.course_set.add(self.course)

    def age(self,
            age):  # Not grate with open-closed principle,
        # because if required to change range of age it needs to be 'opened'
        if 25 <= age < 60:
            self.age = age
        else:
            return 'Not allowed to teach'

    def candidate_list(self, candidate):  # Wrong with dependency inversion principle,
        # because this method depends on Candidates
        self.candidate_list = []
        if isinstance(candidate, CandidateTeacher):
            self.candidate_list.append(candidate)
        else:
            return 'Required valid candidate'


class CandidateTeacher(
    Teachers):  # We violate the interface segregation principle as well as Liskov substitution principle,
    # because not all methods in Teachers must be on Candidates and this functional may not be required by client
    def __init__(self, name, age):
        super().__init__(name, age)

    def mentor(self, mentor):
        if isinstance(mentor, Teachers):
            self.mentor = mentor
        else:
            return 'Mentor must be current Teacher'


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.profile = {}

    def grade(self, subject, grade):
        self.profile.update({subject: grade})

    def profile(self):
        return self.profile


class Group:
    def __init__(self, name):
        self.name = name
        self.students_list = []

    def add_students(self, student):
        self.students_list.append(student)
        pass

    def show_students(self):
        name_list = []
        for i in self.students_list:
            name_list.append(i.name)
        return name_list

    def average_grade(self):  # Wrong with single responsibility principle. It's better to create a new class
        # with method like that
        vault = []
        for i in self.students_list:
            vault.append(sum(i.profile.values()) / len(i.profile.values()))
        return sum(vault) / len(vault)
