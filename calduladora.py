import flet as ft

class CalculaBotao(ft.ElevatedButton):
    def __init__(self, text, width, height, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.width = width
        self.height = height
        self.on_click = button_clicked
        self.data = text

class DigitaBotao(CalculaBotao):
    def __init__(self, text, width, height, button_clicked, expand=1):
        CalculaBotao.__init__(self, text, width, height, button_clicked, expand)
        self.bgcolor = ft.colors.BLACK12
        self.color = ft.colors.WHITE

class AcaoBotao(CalculaBotao):
    def __init__(self, text, width, height, button_clicked):
        CalculaBotao.__init__(self,text, width, height, button_clicked)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class ExtraAcaoBotao(CalculaBotao):
    def __init__(self, text, width, height, button_clicked):
        CalculaBotao.__init__(self, text, width, height, button_clicked)
        self.bgcolor = "#555555"
        self.color = ft.colors.WHITE

class CalculadoraApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value="0", size= 30,color= ft.colors.WHITE, text_align= "end")

        self.content= ft.Column(controls=[
            ft.Row(controls=[ft.Column(
                controls=[
                    ft.Container(content = self.result, width= 300, border= ft.border.all(2, ft.colors.AMBER)
                    )]
                ,spacing= 50, alignment= "end")]
            ),
            ft.Row(
                controls=[
                    ExtraAcaoBotao(text="%", width=75, height= 50, button_clicked= self.button_clicked),
                    ExtraAcaoBotao(text="CE", width=75, height= 50, button_clicked= self.button_clicked),
                    ExtraAcaoBotao(text="C", width=75, height= 50, button_clicked= self.button_clicked),
                    ExtraAcaoBotao(text="X", width=75, height= 50, button_clicked= self.button_clicked)
                ], spacing= 2
            ),
            ft.Row(
                controls=[
                    ExtraAcaoBotao(text="¹/x", width=75, height= 50, button_clicked= self.button_clicked),
                    ExtraAcaoBotao(text="x²", width=75, height= 50, button_clicked= self.button_clicked),
                    ExtraAcaoBotao(text="²√", width=75, height= 50, button_clicked= self.button_clicked),
                    ExtraAcaoBotao(text="៖", width=75, height= 50, button_clicked= self.button_clicked)
                ], spacing= 2
            ),
            ft.Row(
                controls=[
                    DigitaBotao(text="7", width=75, height= 50, button_clicked= self.button_clicked),
                    DigitaBotao(text="8", width=75, height= 50, button_clicked= self.button_clicked),
                    DigitaBotao(text="9", width=75, height= 50, button_clicked= self.button_clicked),
                    AcaoBotao(text="*", width=75, height= 50, button_clicked= self.button_clicked),
                ], spacing= 2

            ),
            ft.Row(
                controls=[
                    DigitaBotao(text="4", width=75, height= 50, button_clicked= self.button_clicked),
                    DigitaBotao(text="5", width=75, height= 50, button_clicked= self.button_clicked),
                    DigitaBotao(text="6", width=75, height= 50, button_clicked= self.button_clicked),
                    AcaoBotao(text="-", width=75, height= 50, button_clicked= self.button_clicked),
                ], spacing= 2
            ),
            ft.Row(
                controls=[
                    DigitaBotao(text="1", width=75, height= 50, button_clicked= self.button_clicked),
                    DigitaBotao(text="2", width=75, height= 50, button_clicked= self.button_clicked),
                    DigitaBotao(text="3", width=75, height= 50, button_clicked= self.button_clicked),
                    AcaoBotao(text="+", width=75, height= 50, button_clicked= self.button_clicked),
                ], spacing= 2
            ),
            ft.Row(
                controls=[
                    AcaoBotao(text="+/-", width=75, height= 50, button_clicked= self.button_clicked),
                    DigitaBotao(text="0", width=75, height= 50, button_clicked= self.button_clicked),
                    AcaoBotao(text=",", width=75, height= 50, button_clicked= self.button_clicked),
                    AcaoBotao(text="=", width=75, height= 50, button_clicked= self.button_clicked)
                ], spacing= 2
            ),
            ], spacing=2, horizontal_alignment= ft.CrossAxisAlignment.CENTER, alignment= ft.MainAxisAlignment.CENTER)

        # calc = ft.Container(ft.Column(controls=[resultado, botoes], spacing=25), padding= ft.Padding(left= 0, top= 25, right=0, bottom=0))

    def button_clicked(self, e):
        data = e.control.data
        print(f"Button clicked with data = {data}")
        if self.result.value == "Error" or data == "C" or data == "CE":
            self.result.value = "0"
            self.reset()

        elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand == True:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value = self.result.value + data

        elif data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif data in ("="):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif data in ("%"):
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif data in ("+/-"):
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page) -> None:
    page.title = "Calculadora Básica"
    page.window.width = 340 # Largura
    page.window.height = 450 # Altura
    page.window.bgcolor = ft.colors.GREY_200
    page.theme_mode = "dark"
    page.window.center()

    calc = CalculadoraApp()
    page.add(calc)

ft.app(target=main)