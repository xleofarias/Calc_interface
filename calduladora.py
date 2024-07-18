import flet as ft

class CalcButton(ft.ElevatedButton):
    def __init__(self, text, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand

class DigitButton(CalcButton):
    def __init__(self, text, expand=1):
        CalcButton.__init__(self, text, expand)
        self.bgcolor = ft.colors.WHITE24
        self.color = ft.colors.WHITE

class ActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.ORANGE
        self.color = ft.colors.WHITE

class ExtraActionButton(CalcButton):
    def __init__(self, text):
        CalcButton.__init__(self, text)
        self.bgcolor = ft.colors.BLUE_GREY_100
        self.color = ft.colors.BLACK

def main(page: ft.Page):
    page.title = "Calculadora Básica"
    page.window.width = 340 # Largura
    page.window.height = 480 # Altura
    page.window.bgcolor = ft.colors.GREY_200
    page.theme_mode = "dark"
    page.window.center()

    resultado = ft.Container(ft.Column(controls=[ft.Text(value="0", size= 30,color= ft.colors.WHITE)], spacing= 0), alignment=ft.alignment.top_right, padding= ft.Padding(left=0, top=0, right= 20, bottom=0), border= ft.border.all(2, color=ft.colors.AMBER_ACCENT_700))

    botoes = ft.Container(content= ft.Column(controls=[
        ft.Row(
            controls=[
                ft.ElevatedButton(text="%", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="CE", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="C", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="X", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700)
            ], spacing= 2
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="¹/x", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="x²", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="²√", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="៖", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700)
            ], spacing= 2
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="8", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="9", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="*", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
            ], spacing= 2
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="5", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="6", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="-", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
            ], spacing= 2
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="2", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="3", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="+", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
            ], spacing= 2
        ),
        ft.Row(
             controls=[
                ft.ElevatedButton(text="+/-", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="0", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text=",", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700),
                ft.ElevatedButton(text="=", width= 75, height= 50, color= ft.colors.AMBER_ACCENT_700)
            ], spacing= 2
        ),
        ], spacing=2, horizontal_alignment= ft.CrossAxisAlignment.CENTER, alignment= ft.MainAxisAlignment.CENTER)
    )

    calc = ft.Container(ft.Column(controls=[resultado, botoes], spacing=25), padding= ft.Padding(left= 0, top= 25, right=0, bottom=0))

    page.add(
        calc
    )

    page.update()

ft.app(target=main)