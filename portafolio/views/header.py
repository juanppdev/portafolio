import reflex as rx
import portafolio.Constants as const

def header() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.image(
                src="/img/perfil.jpg",
                width="200px",
                height="auto",
                border_radius="150px 150px",
                border="5px solid #555",
            ),
            width="100%",
        ),
        rx.vstack(
            rx.text(
                "Juan Pablo Patiño Lopez",
                margin="auto",
                weight="bold",
                size="6",
                color_scheme="cyan",
            ),
            rx.text(
                "A los 25 años, descubrí mi pasión por la programación a través de la plataforma de aprendizaje Platzi mientras navegaba por la web. Desde entonces, me he inmerso en este mundo en constante evolución, explorando nuevas tecnologías y conceptos diariamente. Aunque mi enfoque inicial fue en la creación de páginas web, he ampliado mis horizontes explorando diferentes lenguajes y disciplinas.",
                size="5",
                weight="bold"
            ),
                rx.hstack(
                    rx.icon("map-pinned", size=18),
                    rx.text(
                        "Stade, Deutschland (Germany)",
                        size="3",
                        weight="medium",
                    ),
                    align="center"
                ),
            rx.desktop_only(
                rx.hstack(
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.text.kbd("Correo Electronico", size="7"),
                            ),
                            rx.popover.content(
                                rx.flex(
                                    rx.text("juanppdev@gmail.com"),
                                    direction="column",
                                    spacing="3",
                                ),
                            ),
                        ),
                    rx.link(rx.text.kbd(rx.flex(rx.icon("linkedin"), "Linkedin", spacing="2", align="center"), size="7"), is_external=True, href=const.LINKEDIN),
                    rx.link(rx.text.kbd(rx.flex(rx.icon("github"), "Github", spacing="2", align="center"), size="7"), is_external=True, href=const.GITHUB),
                    rx.link(rx.text.kbd(rx.flex(rx.icon("scroll-text"), "Curriculum", spacing="2", align="center"), size="7"), is_external=True, href="/lebenslauf.pdf"),
                ),
                width="100%",
                spacing="4",
                align="center",
            ),
            rx.mobile_and_tablet(
                rx.grid(
                        rx.popover.root(
                            rx.popover.trigger(
                                rx.text.kbd("Correo Electronico", size="6"),
                                margin_top="15px"
                            ),
                            rx.popover.content(
                                rx.flex(
                                    rx.text("juanppdev@gmail.com"),
                                    direction="column",
                                ),
                            )
                        ),
                    rx.link(rx.text.kbd(rx.flex(rx.icon("linkedin"), "Linkedin", align="center"), size="6"), is_external=True, href="https://www.linkedin.com/in/juanppdev/"),
                    rx.link(rx.text.kbd(rx.flex(rx.icon("github"), "Github", align="center"), size="6"), is_external=True, href="https://github.com/juanppdev"),
                    rx.link(rx.text.kbd(rx.flex(rx.icon("scroll-text"), "Curriculum", align="center"), size="6"), is_external=True, href="/lebenslauf.pdf"),
                    spacing="4"
                ),
                width="100%",
                align="center",
                columns="2",
            ),
        ),
        width="100%",
        align_items="center",
        spacing="4",
        margin_top="130px"
    )