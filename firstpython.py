class Program():


    def __init__(self):
        print('This will get executed first')



    def test_program(self):
        print('This will get executed after constructor is initialised')


    def test_program(self):
        print('This will override test program')





prog=Program()
prog.test_program()
