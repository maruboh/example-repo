#Parent class Course
class Course: 
    def __init__ (self, course_name = "Generic Course"):
        self.course_name = course_name

    #Method to print contact details
    def contact_details(self):
        print("Contact us at: info@hyperiondev.com")

    #Method to print head office location
    def head_office(self):
        print("Head office: Cape Town")


#Subclass OOPcourse that inherits from Course
class OOPCourse (Course):
    def __init__(self):
        super().__int__("OOP Fundamentals")
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"


#Method to print description and trainer 
    def trainer_details(self):
        print(f"Course Description: {self.description}")
        print(f"Trainer: {self.trainer}")

#Method to show the course ID
    def show_course_id(self):
        print("Course ID:#12345")


#Create an object of the OOPCPourse class
course_1 = OOPCourse()

#Call the required methods
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
