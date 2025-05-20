import reflex as rx
from enum import Enum
from .color import Color as Color
from .color import TextColor as TextColor
from .fonts import Font as Font, Fontweight as Fontweight
 


#constants
Max_width= "600px"

STYLESHEETS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;700&display=swap",
    "https://fonts.googleapis.com/css?family=Comfortaa:wght@500&display=swap",
]

#Sizes

class Espacio(Enum):
    Espacio_0="0px !important"
    Espacio_1="0.8em"
    Espacio_2="1em"
    Espacio_navbar="1.5em"
    Espacio_3="2em"

Style_base = {
    "font_family": Font.default.value,
    "font_weight": Fontweight.light.value,
   "background_color": Color.Background.value,
    rx.button: {
         "width":"100%",
         "height": "100%",
         "display": "block",
         "padding": Espacio.Espacio_1.value,
         "border_radius":Espacio.Espacio_2.value,
         "background_color": Color.Content.value,
         "color": TextColor.header.value,
         "_hover": {
            "background_color": Color.Secondary.value,
         }

    },
    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
   
}

navbar_title_style = dict(
    font_family=Font.Logo.value,
    font_weight=Fontweight.medio.value,
    font_size=Espacio.Espacio_navbar.value
)


button_name_style = dict(
    font_family=Font.Title.value,
    font_weight=Fontweight.bold.value,
    font_size=Espacio.Espacio_2.value,
    color=TextColor.header.value,
)
button_body_style = dict(
    font_family=Font.default.value,
    font_weight=Fontweight.light.value,
    font_size=Espacio.Espacio_1.value,
    color=TextColor.body.value,
)
title_style = dict(
    font_family=Font.Title.value,
    font_weight=Fontweight.bold.value,
    width="100%",
    padding_top=Espacio.Espacio_2.value,
    color=TextColor.header.value,
)