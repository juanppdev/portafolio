import reflex as rx
from portafolio.views.navbar import navbar
from portafolio.views.header import header
from portafolio.views.certifications import Certifications
from portafolio.data.Certification import Certificado
from portafolio.views.projects import projects
from portafolio.views.technologies import Technologies
from portafolio.views.footer import footer

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                Certifications(Certificado),
                projects(),
                Technologies(),
                max_width="950px",
                width="100%",
                padding="20px"
            )
        ),
        footer(),
    )


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="teal",
    )
)
app.add_page(index)
