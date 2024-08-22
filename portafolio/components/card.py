import reflex as rx

def card(icon: str, title: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.image(
                icon,
                width="24px"
            ),
            rx.heading(title, size="2", text_align="center"),
            spacing="3",
            width="100%",
            align="center"
        ),
        size="1",
        width="100%",
        background_color="#00befd28",
        color="#52e1fee5"
    )