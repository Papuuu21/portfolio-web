import reflex as rx 
from portfolio.styles.styles import Size, EmSize
from portfolio.components.heading import heading
from portfolio.data import Technology

def tech_stacks(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Tecnologías"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name = technology.icon,
                        font_size = "16px",  #* se tiene que poner a mano los font sizes de los iconos
                        ),
                    rx.text(technology.name),
                size = "1"
        )
            for technology in technologies
            ],
        wrap = "wrap",
        spacing = Size.SMALL.value,                    
        ),
    spacing = Size.SMALL.value,
    )