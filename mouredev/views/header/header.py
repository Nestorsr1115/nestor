import reflex as rx
import mouredev.styles.styles as styles

def header() -> rx.Component:
        return rx.vstack(
            rx.hstack(
                rx.dialog.root(
                rx.dialog.trigger(
                    rx.avatar(
                        
                        border_radius="50%",
                        src="perfil.jpg",
                        padding="2px",
                        border="1px solid",
                        border_color=styles.Color.Primary.value,
                        style={
                            "color": styles.TextColor.body.value,
                            "background-color": styles.Color.Content.value,
                            "cursor": "pointer",
                        },
                    ),
                ),
                rx.dialog.content(
                    rx.dialog.title("Foto de Perfil"),
                    rx.dialog.description(
                        rx.image(
                            src="perfil.jpg",
                            alt="Foto de perfil ampliada",
                            style={
                                "max_width": "300px",
                                "height": "auto",
                                "display": "block",
                                "margin_left": "auto",
                                "margin_right": "auto",
                            }
                        ),
                    ),
                    rx.flex(
                    rx.dialog.close(
                        rx.button("Cerrar")
                    ),
                    justify="end",
                    margin_top="16px",
                ),
            ),
                rx.heading(
                    "Nestor Santana Rodríguez",
                    size="3",
                    color=styles.TextColor.body.value,
                ),
                align_items="flex-start",
            ),
          
            
            align_items="center",
            width="100%",
            margin_y="0px",
        ),
          rx.text(
                "Soy un desarrollador web con experiencia en Python, así como en el desarrollo de aplicaciones web con Reflex, amante de la tecnología y la programación y siempre en búsqueda de nuevos retos.",
               color=styles.TextColor.body.value,
            ),           
        )
        