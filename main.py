from nicegui import ui

ui.header().style('padding: 12px').add(
    ui.label('💬 QuickNotes').classes('text-2xl font-bold')
)

# Input area
with ui.row().classes('items-center w-full p-4 gap-2'):
    note_input = ui.input('Write a note...').props('outlined').classes('w-2/3')
    add_btn = ui.button('Add Note', on_click=lambda: add_note()).classes('w-1/6')

# Main container for notes
notes_container = ui.column().classes('w-full items-center p-4 gap-2')

ui.footer().style('padding: 10px; text-align:center').add(
    ui.label('Built with NiceGUI • YourName')
)

# Backend data
notes = {}

def add_note():
    text = note_input.value.strip() if note_input.value else ''
    if text:
        notes.append(text)
        note_input.value = ''
        render_notes()

def render_notes():
    notes_container.clear()
    for n in notes:
        with notes_container:
            ui.card().classes('p-4 m-2 w-3/4').add(ui.label(n))

if __name__ == '__main__':
    ui.run(title='QuickNotes')
