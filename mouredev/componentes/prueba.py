import reflex as rx 

def prueba() -> rx.Component:
    return rx.hstack(
        rx.text("Hola mundo"),
    )