class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod
    def hello():    #decorator
        print("hello")
    def avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hii",self.name,"your average score is",sum/3)
s1=student("karan",[90,80,70])
s1.avg()
s1.name="IRon man"
s1.avg()
s1.hello()
