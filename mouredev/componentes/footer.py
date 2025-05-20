import reflex as rx
import datetime 
import mouredev.styles.styles as styles

def footer() -> rx.Component:
    return rx.vstack(
        # rx.image(src="code.png",
        #          style={
        #              "width":"200px",
        #              "height":"auto",
                     
        #          },
        #          ),
        rx.text(f"©  2023-{datetime.datetime.now().year} Nestor Santana Rodriguez desarrollador web.",
                font_size= styles.Espacio.Espacio_2.value),
        rx.text("Sitio web basado en reflex.",
                font_size= styles.Espacio.Espacio_2.value,
                  margin_top="0px !important",  
                ),
                
       
        align_items="center",      # Centra los elementos horizontalmente dentro del vstack
        width="100%",
        color= styles.TextColor.body.value,
      
    )
