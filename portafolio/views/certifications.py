import reflex as rx
from portafolio.components.certificado import certificado
from portafolio.data.Certification import Certification

def Certifications(certificados: list[Certification]) -> rx.Component:
    return rx.vstack(
        rx.text("Certificados", size="7"),
        rx.desktop_only(
            rx.grid(
                *[
                    certificado(
                        data
                    )
                    for index, data in enumerate(certificados)
                ],
                columns="2",
                spacing="5",
                width="100%",
            ),
        ),
        rx.mobile_and_tablet(
            rx.grid(
                *[
                    certificado(
                        data
                    )
                    for index, data in enumerate(certificados)
                ],
                columns="2",
                spacing="4",
                width="100%",
                margin_x="auto",
            ),
            margin_y="75px",
            width="100%"
        )
    )