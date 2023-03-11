# in java --> interface
# <---   Duck Typing.   ---> 

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class Myeditor:
    def execute(self):
        print("Speel check")
        print("convention check")
        print("Compiling")
        print("Running")

class laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()

lap1 = laptop()
lap1.code(ide)

print("==================================")

ide = Myeditor()             

lap1 = laptop()
lap1.code(ide)