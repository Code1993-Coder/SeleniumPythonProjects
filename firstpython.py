class Program():


    def __init__(self):
        print('This will get executed first')



    def test_program(self):
        print('This will get executed after constructor is initialised')





prog=Program()
prog.test_program()
