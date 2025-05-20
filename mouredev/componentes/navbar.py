import reflex as rx
import mouredev.styles.styles as styles
from mouredev.styles.styles import Espacio as Espacio
from mouredev.componentes.ant_component import float_button


def navbar() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.text("N", style={"color": styles.Color.Primary.value}),
                rx.text("S", style={"color": styles.Color.Rojo.value}),
                rx.text("R", style={"color": styles.Color.Secondary.value}),
                spacing="0",
                style=styles.navbar_title_style
               
                
            ),
        ),
        #float_button(),
        position="sticky",         # Hace que el navbar sea sticky
        top="0",                   # Define la posición desde la parte superior
        z_index="999",
        bg=styles.Color.Content.value,  # Asegura que esté por encima de otros elementos
    )