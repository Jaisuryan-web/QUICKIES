from nicegui import ui

ui.header().style('padding: 12px').add(
    ui.label('💬 QuickNotes').classes('text-2xl font-bold')
)

# Main container
notes_container = ui.column().classes('w-full items-center p-4 gap-2')

# Footer
ui.footer().style('padding: 10px; text-align:center').add(
    ui.label('Built with NiceGUI • YourName')
)

if __name__ == '__main__':
    ui.run(title='QuickNotes')
