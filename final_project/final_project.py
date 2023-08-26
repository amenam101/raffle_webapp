import reflex as rx
import pandas as pd
import secrets


class State(rx.State):
    """The app state."""

    # Variables
    raffle_file: list[str]
    participants_number: str = "0"
    winner_number: str = "?"
    winner_name: str = "?"
    data = pd.DataFrame()

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Manejo de la subida de archivos.

        Actualiza las variables:
            - raffle_file
            - data
            - participants_number

        Ejemplo de archivo:
            id;Nombre
            1;Juan
            2;Pedro
            3;Maria
            4;Luis
            5;Ana
            6;Jose
            7;Carlos
            8;Laura
            9;Marta
            10;Jorge


        Args:
            files: Archivos subidos
        """
        for file in files:
            upload_data = await file.read()
            outfile = f"./assets/{file.filename}"

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Actualiza las variables
            self.raffle_file.append(file.filename)
            self.data = pd.read_csv(outfile, sep=";", encoding="ISO-8859-1")
            self.participants_number = str(self.data.shape[0])

    def handle_reset(self):
        """Handle the reset of the app."""
        self.raffle_file = []
        self.participants_number = "?"
        self.winner_number = "?"
        self.winner_name = "?"

    def raffle(self, numero: str):
        """
        Función que genera un nÃ®mero aleatorio entre 0 y el numero de participantes
        """
        number = secrets.randbelow(10000)
        self.winner_number = str(self.data["id"][number % int(numero)])
        self.winner_name = str(self.data["Nombre"][number % int(numero)])


COLOR = "rgb(107,99,246)"


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            # Título
            rx.heading("Mi web de sorteos", font_size="2em"),
            # Indicaciones
            rx.box(
                "Sube un archivo ",
                rx.code(".csv", font_size="1em"),
                " y haz tu sorteo! [id] [Nombre]",
            ),
            # Box para subir los archivos
            rx.upload(
                rx.vstack(
                    rx.button(
                        "Select File",
                        color=COLOR,
                        bg="white",
                        border=f"1px solid {COLOR}",
                    ),
                    rx.text(
                        "Arrastra tu archivo .csv aqui o haz clic en este área para seleccionarlo. "
                    ),
                ),
                multiple=True,
                accept={
                    "application/csv": [".csv"],
                },
                max_files=1,
                disabled=False,
                on_keyboard=True,
                border=f"1px dotted {COLOR}",
                padding="0.8em",
            ),
            # Botones para subir y resetear archivos
            rx.responsive_grid(
                rx.button(
                    "Upload",
                    on_click=lambda: State.handle_upload(rx.upload_files()),
                ),
                rx.button(
                    "Reset",
                    on_click=lambda: State.handle_reset(),
                ),
                columns=[2],
                spacing="1px",
            ),
            # Mostrar el nombre del archivo subido
            rx.responsive_grid(
                rx.foreach(
                    State.raffle_file,
                    lambda raffle_file: rx.vstack(
                        rx.text(raffle_file),
                    ),
                ),
                columns=[1],
                spacing="1px",
            ),
            # Mostrar cantidad de participantes
            rx.box(
                "Hay ",
                State.participants_number,
                " participantes",
            ),
            # Botón para hacer el sorteo
            rx.button(
                "Iniciar el sorteo",
                on_click=lambda: State.raffle(State.participants_number),
                color=COLOR,
                bg="white",
                border=f"1px solid {COLOR}",
            ),
            # Mostrar al ganador
            rx.box(
                "El ganador es el numero ",
                State.winner_number,
            ),
            rx.box(
                "Felicidades ",
                State.winner_name,
                " !!!",
                font_size="2em",
            ),
            spacing="0.5em",
            font_size="1.8em",
            padding_top="5%",
            padding_bottom="5%",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, title="Sorteo")
app.compile()
