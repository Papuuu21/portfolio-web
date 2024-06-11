import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.icon_button import icon_button
from portfolio.data import Data
from portfolio.data import Media

def social_media(data: Media) -> rx.Component:
    return rx.flex(
        icon_button(
            "mail",
            f"{data.email}",
            data.email,
            False,
        ),
        rx.hstack(
            icon_button(
                "file-text",
                data.cv,
                "Curriculum",
            ),
            icon_button(
                "github",
                data.github,
            ),
            icon_button(
                "Linkedin",
                data.likedin,
            ),
        spacing = Size.SMALL.value,  
        ),
    spacing = Size.SMALL.value, 
    flex_direction = ["column", "column", "row"]  #* primer y segundo dato pantallas gr y med, 3º dato pq
    )