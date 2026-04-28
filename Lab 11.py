#QUESTION 1
class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
    def get_name(self):
        return self.name
    def get_major(self):
        return self.major
    def set_name(self, new_name):
        self.name = new_name
    def set_major(self, new_major):
        self.major = new_major
    def __str__(self):
        string = f"Student Name: {self.name}. Student Major: {self.major}."
        return string
    
student1 = Student("Rebekah", "Math & Statistics")
#print(student1)

#QUESTION 2
class Course:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.students = 0
    def get_name(self):
        return self.name
    def get_number(self):
        return self.number
    def add_student(self, student_num):
        self.students += student_num
    def show_enrollment(self):
        return self.students
    def __str__(self):
        course_str = f"{self.number}: {self.name} with {self.students} students enrolled."
        return course_str
    
course1 = Course("Introduction to Astronomy", "AST101")
#print(course1)

#QUESTION 11
import time
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
    def get_title(self):
        return self.title
    def get_artist(self):
        return self.artist
    def set_title(self, new_title):
        self.title = new_title
    def set_artist(self, new_artist):
        self.artist = new_artist
    def play(self):
        print(f"❚❚ {self.title} • {self.artist}", end = "\r")
        time.sleep(self.duration)
        print(f"▶ {self.title} • {self.artist}")
        

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def play(self):
        print(f"Playing: '{self.name}'")
        for song in self.songs:
            song.play()

song1 = Song("You Know What They Do to Guys Like Us in Prison", "My Chemical Romance ", 5)
song2 = Song("Our Lawyer Made Us Change the Name of this Song So We Wouldn't Get Sued", "Fall Out Boy ", 5)
song3 = Song("Lying is the Most Fun a Girl Can Have Without Taking Her Clothes Off", "Panic! At The Disco ", 5)

#print(song1.play())

playlist1 = Playlist("Rebekah's Playlist")
playlist1.add_song(song1)
playlist1.add_song(song2)
playlist1.add_song(song3)

playlist1.play()
