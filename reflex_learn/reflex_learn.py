"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...
    
class TextfieldControlled(rx.State):
    text: str = "Hello World!"


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.heading("impi", size="8", align="center"),
        
        rx.flex(
            rx.vstack(
                rx.text("First Name"),
                rx.input(
                    placeholder="First Name",
                    name="first_name",
                    value=TextfieldControlled.text,
                    on_change=TextfieldControlled.set_text
                ),
                 rx.text("Last Name"),
                rx.input(
                    placeholder="Last Name",
                    name="last_name",
                ),
                
                rx.input(id="input1"),
    rx.button("Erase", on_click=rx.set_value("input1", "")),
            )
        )
    )


app = rx.App()
app.add_page(index)
