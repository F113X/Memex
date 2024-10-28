from textual import events
from textual.app import App, ComposeResult
from textual.widgets import TextArea, Footer, Button

Text = '''hello'''

class ExtendedTextArea(TextArea):
    """A subclass of TextArea with parenthesis-closing functionality."""
    text : str
    prompt_input: "PromptInput"

    def _on_key(self, event: events.Key) -> None:
        if event.character == "(":
            self.insert("()")
            self.move_cursor_relative(columns=-1)
            event.prevent_default()


class TextAreaKeyPressHook(App):
    
    def compose(self) -> ComposeResult:
        yield Footer()
        yield ExtendedTextArea(Text)
        yield Button()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(TextArea.text)



if __name__ == "__main__":
    app = TextAreaKeyPressHook()
    output = app.run()
    print(output)