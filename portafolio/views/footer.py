import reflex as rx
import portafolio.Constants as const

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)


def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(rx.icon(icon), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", const.INSTAGRAM),
        social_link("twitter", const.X),
        social_link("Github", const.GITHUB),
        social_link("linkedin", const.LINKEDIN),
        spacing="3",
        justify_content="center",
        width="100%",
    )


def footer() -> rx.Component:
    return rx.el.footer(
            rx.divider(),
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "© 2024, Web Realizada con ❤️ por Juanppdev",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                    ),
                    spacing="2",
                    align="center",
                    justify_content="center",
                    width="100%",
                ),
                socials(),
                width="100%",
            ),
            padding="40px",
        width="100%",
    )