from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class Container(BoxLayout):
    operation = None
    number = ''

    writeTextId = ObjectProperty()
    outPutTextId = ObjectProperty()

    result = 0

    def selectOperationOne(self, num, op):
        if op == 'clear':
            self.result = 0
            self.number = ''
            self.operation = None
            self.outPutTextId.text = '0'
            self.writeTextId.text = '' 
            return
        if op == 'Del':
            self.operation = None
            self.writeTextId.text = '' 
            print(self.result)
        if op == '=':
            print(self.result)
            self.outPutTextId.text = str(self.result)
            self.number = ''
            self.operation = None 
        if num == '':
            return
        if op == '*':
            self.result *= float(num)
        if op == None :
            self.result += float(num)
        if op == '+':   
            self.result += float(num)
        if op == '-':
            self.result -= float(num)
        if op == '/':
            self.result /= float(num)
        if op == '%':
            self.result = (float(num) * self.result) / 100
        if op == 'square':
            self.result = self.result ** float(num)

    def change_operation(self, op):
        print(op)
        if op == 'Del':
            self.selectOperationOne('', 'Del')
            return
        if op == 'clear':
            self.selectOperationOne('', 'clear')
            return
        self.selectOperationOne(self.number, self.operation)
        self.operation = op
        
        if self.operation == '=':
            self.selectOperationOne(self.number, self.operation)
        self.writeTextId.text = op
        self.number = ''


    def change_num(self, num):
        if self.number == '':
            self.number = num
            self.writeTextId.text = self.number
        else :
            self.number += num
            self.writeTextId.text = self.number
        
    pass

class MyApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MyApp().run()