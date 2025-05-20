from operator import le
from turtle import pos
import reflex as rx
from mouredev.componentes.link_button import link_button
from mouredev.componentes.title import title
def link() -> rx.Component:
    return rx.vstack(
        title("Mis redes sociales"),
        link_button(
            "Facebook",
            "Mi perfil de facebook",
            "/icons/fbw.svg",
            url="https://www.facebook.com/nestorsantanarodr%C3%ADguez"),
        link_button(
            "Instagram",
            "Mi página de instagram",
            "/icons/ig.svg",
            url="https://www.instagram.com/nesty_sr/"),
        link_button(
            "Github",
            "Mi perfil de github",
            "/icons/git.svg",
            url="https://github.com/Nestorsr1115"),
        link_button(
            "Linkedin",
            "Mi perfil de linkedin",
            "/icons/linkedin.svg",
            url="https://www.linkedin.com/in/nestor-santana-rodr%C3%ADguez-997712344/overlay/about-this-profile/?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base%3BvuVbT7M1RUury8hQduK7sw%3D%3D"),
        title("Contacto"),
        link_button(
            "Email",
            "nestorsr1115@gmail.com",
            "/icons/email.svg",
            url="mailto:nestorsr1115@gmail.com",
            
        ),
        link_button(
            "WhatsApp",
            "(+506)88878598",
            "/icons/wasap.svg",
            url="https://wa.me/qr/NTHAAEC7Y27IB1"),

       
        align_items="center",      # Centra los elementos horizontalmente dentro del vstack
        width="100%",
            
    ),
