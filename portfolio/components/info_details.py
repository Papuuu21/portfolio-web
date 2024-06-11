import reflex as rx 
from portfolio.styles.styles import Size, IMAGE_HEIGHT, EmSize
from portfolio.components.icon_badge import icon_badge
from portfolio.components.icon_button import icon_button
from portfolio.data import Info

def info_details(info: Info) -> rx.Component:
    return rx.flex(
        rx.hstack(
            icon_badge(info.icon),
            rx.vstack(
                rx.text.strong(info.title), 
                rx.text(info.subtitle),
                rx.text(
                    info.description,
                    size =  Size.SMALL.value,
                    color_scheme = "gray"
                ),
                rx.cond(
                    info.technologies,
                    rx.flex(
                    *[
                        rx.badge(
                            rx.box(class_name = technology.icon),
                            technology.name,
                            color_scheme= "gray",
                        )
                        for technology in info.technologies
                    ],
                wrap = "wrap",
                spacing = Size.SMALL.value,                    
                ),
                ),
                rx.hstack( 
                    rx.cond(
                        info.url != "",
                    icon_button(
                        "link",
                        info.url,
                    ),
                    ),
                    rx.cond(
                        info.github != "",
                    icon_button(
                        "github",
                        info.github,
                    ),
                    ),
                ),
            spacing = Size.SMALL.value,
            width = "100%", 
            ),
        spacing = Size.DEFAULT.value,
        width = "100%", 
        ),
        rx.cond(
            info.image != "",
            rx.image(
                    src = info.image,
                    height = "100px",
                    width = "25%",
                    border_radius = EmSize.DEFAULT.value,
                    object_fit = "cover", #* Para que el image se ajuste al tamaño del card                   
                ),
        ),
                rx.vstack(
                    rx.cond(
                        info.date != "",
                        rx.badge(info.date),
                    ),
                    rx.cond(
                        info.certificate != "",
                        icon_button(
                            "shield-check",
                            info.certificate,
                            solid =  True,
                            ),
                        ),
        spacing=Size.SMALL.value,
        ),
    flex_direction = ["column-reverse", "row"],
    width = "100%",
    spacing=Size.SMALL.value,
    )