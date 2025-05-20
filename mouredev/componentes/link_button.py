import reflex as rx
import mouredev.styles.styles as styles

def link_button(title: str,body:str,image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width= styles.Espacio.Espacio_3.value,
                    height=styles.Espacio.Espacio_3.value,
                    margin=styles.Espacio.Espacio_2.value
                ),  
                rx.vstack(
                    rx.text(title, style=styles.button_name_style),  # Primer texto arriba
                    rx.text(body, style=styles.button_body_style),  # Segundo texto abajo
                    align_items="star",
                    spacing="0",
                    margin=styles.Espacio.Espacio_0.value
                ),
                align_items="center",  # Centra los elementos verticalmente
                justify_content="flex-start",  # Alinea los elementos al inicio horizontalmente
            ),
        ),
        width="100%",
        href=url,
        is_external=True,
    )


