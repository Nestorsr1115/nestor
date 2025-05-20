import reflex as rx
from mouredev.componentes.navbar import navbar
from mouredev.componentes.footer import footer
from mouredev.views.header.header import header
from mouredev.views.link.link import link
from mouredev.componentes.prueba import prueba
import mouredev.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
        rx.vstack(
        header(),
        link(),
        max_width=styles.Max_width,
        width="100%",
        margin_y=styles.Espacio.Espacio_1.value,
        padding=styles.Espacio.Espacio_1.value,          
    ),
    ),
        
     footer(),

)


app = rx.App(
    #stylesheets=styles.STYLESHEETS,
    style=styles.Style_base
)
app.add_page(
    index,
    title="NestorSR | Desarrollador web",
    description="Mi primera web con reflex",
    image="perfil.jpg",
)
app._compile()