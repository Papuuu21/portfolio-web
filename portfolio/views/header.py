import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.media import social_media
from portfolio.data import Data

def header(data: Data) -> rx.Component:
    return rx.hstack(
            rx.avatar(
                src = data.avatar,
                size = Size.BIG.value,
            ),
            rx.vstack(
                heading(
                    data.name, 
                    True,
                ),
                heading(
                    data.skill,
                ),
                rx.text(
                    rx.icon(
                        "sun",
                        color = "yellow",
                    ),
                data.location,
                weight = "bold",
                display = "inherit",   #* Para que este en una línea con el icono
                ),
            social_media(data.media),
            spacing = Size.SMALL.value,
            ),
        spacing = Size.SMALL.value,
        )