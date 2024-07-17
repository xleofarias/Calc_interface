import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora Básica"
    page.window.width = 350 # Largura
    page.window.height = 550 # Altura
    page.window.bgcolor = ft.colors.GREY_200
    page.window.center()

    resultado = ft.Container(ft.Column(controls=[ft.Text(value="0", size= 30)], spacing= 0), alignment=ft.alignment.top_right, padding= ft.Padding(left=0, top=0, right= 20, bottom=0))

    botoes = ft.Container(content= ft.Column(controls=[
        ft.Row(
            controls=[
                ft.ElevatedButton(text="%", width= 75, height= 50),
                ft.ElevatedButton(text="CE", width= 75, height= 50),
                ft.ElevatedButton(text="C", width= 75, height= 50),
                ft.ElevatedButton(text="X", width= 75, height= 50)
            ], spacing= 2
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="¹/x", width= 75, height= 50),
                ft.ElevatedButton(text="x²", width= 75, height= 50),
                ft.ElevatedButton(text="²√", width= 75, height= 50),
                ft.ElevatedButton(text="៖", width= 75, height= 50)
            ], spacing= 2
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="7", width= 75, height= 50),
                ft.ElevatedButton(text="8", width= 75, height= 50),
                ft.ElevatedButton(text="9", width= 75, height= 50),
                ft.ElevatedButton(text="*", width= 75, height= 50),
            ], spacing= 2
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="4", width= 75, height= 50),
                ft.ElevatedButton(text="5", width= 75, height= 50),
                ft.ElevatedButton(text="6", width= 75, height= 50),
                ft.ElevatedButton(text="-", width= 75, height= 50),
            ], spacing= 2
        ),
        ft.Row(
            controls=[
                ft.ElevatedButton(text="1", width= 75, height= 50),
                ft.ElevatedButton(text="2", width= 75, height= 50),
                ft.ElevatedButton(text="3", width= 75, height= 50),
                ft.ElevatedButton(text="+", width= 75, height= 50),
            ], spacing= 2
        ),
        ft.Row(
             controls=[
                ft.ElevatedButton(text="+/-", width= 75, height= 50),
                ft.ElevatedButton(text="0", width= 75, height= 50),
                ft.ElevatedButton(text=",", width= 75, height= 50),
                ft.ElevatedButton(text="=", width= 75, height= 50)
            ], spacing= 2
        ),
        ], spacing=2)
    )

    page.add(
        resultado, botoes
    )

    page.update()

ft.app(target=main)