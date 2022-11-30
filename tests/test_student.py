from school_schedule.student import Student

# unit tests
def test_student_initialization():
    # Arrange
    samara = {'name': "Samara",
              'grade': "junior",
              'classes': [
                  "Pre-Calc",
                  "English III",
                  "World History",
                  "Gym",
                  "Chemistry",
                  "Music Composition"
              ]
              }
    
    # Act
    ada_std = Student(samara['name'], samara['grade'], samara['classes'])
    
    # Assert
    assert len(ada_std.classes) == 6
    assert ada_std.name == 'Samara'
    assert ada_std.grade == 'junior'
    assert 'Pre-Calc' in ada_std.classes

def test_instance_method_add_classes():
    # arrange
    samara = {'name': "Samara",
              'grade': "junior",
              'classes': [
                  "Pre-Calc",
                  "English III",
                  "World History",
                  "Gym",
                  "Chemistry",
                  "Music Composition"
              ]
              }

    # Act
    ada_std = Student(samara['name'], samara['grade'], samara['classes'])
    ada_std.add_classes('Software Engineering')

    # Assert
    assert 'Software Engineering' in ada_std.classes
       

def test_instance_method_get_num_classes():
    # arrange
    samara = {'name': "Samara",
              'grade': "junior",
              'classes': [
                  "Pre-Calc",
                  "English III",
                  "World History",
                  "Gym",
                  "Chemistry",
                  "Music Composition"
              ]
              }

    # Act
    ada_std = Student(samara['name'], samara['grade'], samara['classes'])
    ada_std.get_num_classes()

def test_instance_method_summary():
    
    
