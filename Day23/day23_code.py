from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

class TempConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        self.input = TextInput(hint_text='Enter temperature', multiline=False)
        self.add_widget(self.input)

        self.spinner = Spinner(
            text='Choose conversion',
            values=('Celsius to Fahrenheit', 'Fahrenheit to Celsius')
        )
        self.add_widget(self.spinner)

        self.result_label = Label(text='Result will appear here')
        self.add_widget(self.result_label)

        convert_btn = Button(text='Convert')
        convert_btn.bind(on_press=self.convert)
        self.add_widget(convert_btn)

    def convert(self, instance):
        try:
            temp = float(self.input.text)
            if self.spinner.text == 'Celsius to Fahrenheit':
                result = (temp * 9/5) + 32
                self.result_label.text = f"{temp}°C = {result:.2f}°F"
            elif self.spinner.text == 'Fahrenheit to Celsius':
                result = (temp - 32) * 5/9
                self.result_label.text = f"{temp}°F = {result:.2f}°C"
            else:
                self.result_label.text = "Please select a conversion type"
        except ValueError:
            self.result_label.text = "Invalid input. Enter a number."

class TemperatureConverterApp(App):
    def build(self):
        return TempConverter()

if __name__ == '__main__':
    TemperatureConverterApp().run()
