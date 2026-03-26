import flet as ft
import httpx

def main(page: ft.Page):
    page.title = "Under 3.5 Predictor"
    page.theme_mode = ft.ThemeMode.DARK
    results_list = ft.ListView(expand=1, spacing=10, padding=20)
    
    async def fetch_picks(e):
        results_list.controls.clear()
        results_list.controls.append(ft.ProgressBar())
        page.update()
        try:
            # Substitua abaixo pela URL do seu backend quando ele estiver online
            url = "https://v3.football.api-sports.io" # Exemplo
            results_list.controls.clear()
            results_list.controls.append(ft.Text("Conectado com sucesso!", color="green"))
        except Exception as ex:
            results_list.controls.append(ft.Text(f"Erro: {ex}", color="red"))
        page.update()

    page.add(ft.Text("Betting Helper 1.0", size=25), ft.ElevatedButton("Analisar Jogos", on_click=fetch_picks), results_list)

ft.app(target=main)
