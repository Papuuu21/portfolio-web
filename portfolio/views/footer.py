import reflex as rx 
from portfolio.styles.styles import Size
from portfolio.components.heading import heading
from portfolio.components.media import social_media
from portfolio.data import Data

def footer(data: Data) -> rx.Component:
    return rx.vstack(
        rx.text(
            "© 2024 Pablo DeAlva - Created with only Python and framework Reflex.dev",
            weight = "bold",
        ),
    social_media(data.media),
    spacing=Size.SMALL.value,
    )