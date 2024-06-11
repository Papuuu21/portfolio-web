import reflex as rx 
from portfolio.styles.styles import MAX_WIDTH, Size, EmSize , BASE_STYLE, STYLE_SHEETS
from portfolio.views.header import header
from portfolio.views.footer import footer
from portfolio.views.about import about
from portfolio.views.info import info
from portfolio.views.tech_stacks import tech_stacks
from portfolio.views.extra import extra
from portfolio import data

DATA = data.data

def index() -> rx.Component:
    return rx.center(
        #rx.theme_panel(),
        rx.vstack(
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stacks(DATA.technologies),
            rx.divider(),
            info("Experiencia", DATA.experience),
            rx.divider(),
            info("Proyectos", DATA.projects),
            rx.divider(),
            info("Formación", DATA.training),
            rx.divider(),
            extra(DATA.extras),
            rx.divider(),
            footer(DATA),
            spacing=Size.LARGE.value,
            padding_y = EmSize.BIG.value,
            max_width = MAX_WIDTH,
            width = "100%",
        ),
    ) 


app = rx.App(
    stylesheets= STYLE_SHEETS,
    style = BASE_STYLE,
    theme = rx.theme(
        appearance = "dark",
        accent_color = "blue",
    )
)

title = DATA.title
description = DATA.description
image = DATA.image

app.add_page(
    index,
    title = title,
    description = description,
    image = image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image}
    ]

    )
