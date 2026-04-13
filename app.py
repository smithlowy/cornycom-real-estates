import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Cornycom Real Estates"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # URL of your LIVE Render Django API
    API_URL = "https://cornycom-real-estates.onrender.com/api/plots/"

    # UI Elements
    search_input = ft.TextField(
        label="Search by District (e.g., Mukono)", 
        expand=True,
        on_submit=lambda e: perform_search(search_input.value)
    )
    
    results_column = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def perform_search(district_name=None):
        results_column.controls.clear()
        results_column.controls.append(ft.ProgressBar())
        page.update()

        try:
            params = {}
            if district_name:
                params['district'] = district_name
            
            # Using your live Render URL
            response = requests.get(API_URL, params=params, timeout=10)
            
            if response.status_code == 200:
                plots = response.json()
                results_column.controls.clear()

                if not plots:
                    results_column.controls.append(ft.Text("No plots found in this area.", size=16))
                else:
                    for plot in plots:
                        # Logic to handle missing map links safely
                        map_url = plot.get('google_maps_link') or "https://www.google.com/maps"
                        
                        results_column.controls.append(
                            ft.Card(
                                content=ft.Container(
                                    padding=15,
                                    content=ft.Column([
                                        # Added Image display from your API URL
                                        ft.Image(
                                            src=plot['main_image'], 
                                            width=400, 
                                            height=200, 
                                            fit=ft.ImageFit.COVER,
                                            border_radius=10
                                        ),
                                        ft.Text(f"📍 {plot['district']} - {plot['village']}", size=18, weight="bold"),
                                        ft.Text(f"📏 Dimensions: {plot['dimensions']}"),
                                        ft.Text(f"💰 Price: {plot['price']} UGX", color="green", weight="bold"),
                                        ft.Text(f"📝 {plot['description']}", italic=True),
                                        ft.ElevatedButton(
                                            "View on Google Maps", 
                                            icon=ft.Icons.MAP,
                                            on_click=lambda e, url=map_url: page.launch_url(url)
                                        )
                                    ])
                                )
                            )
                        )
            else:
                results_column.controls.clear()
                results_column.controls.append(ft.Text(f"Server Error: {response.status_code}", color="red"))

        except requests.exceptions.ConnectionError:
            results_column.controls.clear()
            results_column.controls.append(ft.Text("Error: Could not connect to the cloud server. Check your internet!", color="red", size=18))
        except Exception as e:
            results_column.controls.clear()
            results_column.controls.append(ft.Text(f"An error occurred: {e}", color="red"))
        
        page.update()

    # Layout Setup
    page.add(
        ft.Row([
            # Using a generic real estate icon since we are live
            ft.Icon(name=ft.Icons.LANDSCAPE, color="green", size=40),
            ft.Text("Cornycom Land Search", size=25, weight="bold")
        ]),
        ft.Row([
            search_input,
            ft.IconButton(icon=ft.Icons.SEARCH, on_click=lambda e: perform_search(search_input.value))
        ]),
        ft.Divider(),
        results_column
    )

    # Load all plots on startup from Render
    perform_search()

ft.app(target=main)