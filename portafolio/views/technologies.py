import reflex as rx
from portafolio.components.card import card

def Technologies() -> rx.Component:
    return rx.vstack(
        rx.text("Tecnologias", size="7"),
        rx.box(
            rx.text("Frontend", size="5", text_align="center", padding_bottom="1em"),
            rx.grid(
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg", "HTML"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg", "CSS"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg", "JS"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/bootstrap/bootstrap-original.svg", "BOOTSRAP"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/tailwindcss/tailwindcss-original.svg", "TAILWIND"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain.svg", "REFLEX"),
                columns=rx.breakpoints(
                    xs="2",
                    sm="2",
                    md="3",
                    lg="6",
                ),
                spacing="2",
                margin="auto"
            ),
            width="100%",
            height="50%",
            background_color="#d8f4f609",
            padding="32px",
        ),
        rx.box(
            rx.text("Backend", size="5", text_align="center", padding_bottom="1em"),
            rx.grid(
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/nodejs/nodejs-original.svg", "NODEJS"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mysql/mysql-original-wordmark.svg", "MYSQL"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain.svg", "Python"),
                columns=rx.breakpoints(
                    xs="2",
                    sm="2",
                    md="3",
                    lg="6",
                ),
                spacing="2",
            ),
            width="100%",
            height="50%",
            background_color="#d8f4f609",
            padding="32px"
        ),
        rx.box(
            rx.text("Herramientas", size="5", text_align="center", padding_bottom="1em"),
            rx.grid(
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg", "GIT"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg", "GITHUB"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/vscode/vscode-original.svg", "VSC"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/krakenjs/krakenjs-original.svg", "GITKRAKEN"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/androidstudio/androidstudio-original.svg", "ANDROID STUDIO"),
                card("https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/trello/trello-original.svg", "TRELLO"),
                columns=rx.breakpoints(
                    xs="2",
                    sm="2",
                    md="3",
                    lg="6",
                ),
                spacing="2",
                margin="auto"
            ),
            width="100%",
            height="50%",
            background_color="#d8f4f609",
            padding="32px",
        ),
        width="100%",
    )