class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        pass


        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score


Bob = Student("Bob", 26, ["FE","BE"],20.90)
print(Bob)
print(Bob.__dict__)
# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
