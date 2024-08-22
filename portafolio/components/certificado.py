import reflex as rx
from portafolio.data.Certification import Certification

# Aqui es donde se diseña
def certificado(data: Certification) -> rx.Component:
    return rx.card(
    rx.inset(
        rx.image(
            src=data.image,
            width="100%",
            height="auto",
        ),
        side="top",
        pb="current",
    ),
    rx.text(
        data.title,
        size="3"
    ),
    rx.text(
        data.description,
        size="2"
    ),
    width="100%",
)