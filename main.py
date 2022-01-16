import kivy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout 
import random
kivy.require('2.0.0')


class MyRoot(BoxLayout):

    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)

    def generate_number(self):
        self.result_label.text = str(random.randint(0,1000))


class NeuralRandom(App):

    def build(self):
        return MyRoot()



neuralRandom = NeuralRandom()

neuralRandom.run()




