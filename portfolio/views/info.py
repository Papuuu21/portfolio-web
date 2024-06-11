import reflex as rx 
from portfolio.styles.styles import Size, EmSize
from portfolio.components.heading import heading
from portfolio.components.info_details import info_details
from portfolio.data import Info

def info(title: str, info: list[Info]) -> rx.Component:
    return rx.flex(
        heading(title),
        rx.vstack(
            *[
                info_details(item)
                for item in info
            ],
        spacing=Size.DEFAULT.value,
        width = "100%",
        ),
        spacing=Size.DEFAULT.value,
        width = "100%",    
    )