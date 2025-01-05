class myclass:
    __privatevar=27
    def __privatemeth(self):
        print("I am inside aaa private emthod")
    def hello(self):
        self.__privatemeth()
        print("the priate variable",self.__privatevar)
obj1=myclass()
obj1.hello()

