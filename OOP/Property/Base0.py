class Student0:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.gotmarks = self.name + ' obtained ' + self.marks + ' marks.'

class Student1:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks.'

class Student2:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    @property
    def gotmarks(self):
        return self.name + ' obtained ' + self.marks + ' marks.'    

    @gotmarks.setter
    def gotmarks(self, sentence):
        name, rand, marks = sentence.split(' ')
        self.name = name
        self.marks = marks


if __name__ == "__main__":
    #0
    # st = Student0("Aadil", "18")
    # st.name = 'Andzl'
    # print(st.name)
    # print(st.gotmarks)

    #1
    # st = Student1("Aadil", "18")
    # st.name = 'Andzl'
    # print(st.name)
    # print(st.gotmarks())    

    #2
    # st = Student2("Aadil", "18")
    # st.name = 'Andzl'
    # print(st.name)
    # print(st.gotmarks) 
    # st.gotmarks = 'Nadir obtained 12'
    # print(st.gotmarks)
    # print(st.name)







