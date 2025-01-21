<div class="mermaid">
%%{init: {"themeVariables": {"background": "#bdc3c7", "primaryColor": "#2c3e50", "fontFamily": "monospace", "lineWidth": 2}}}%%
classDiagram
    class get_image_files {
        +image_extensions: Set[str]
        +image_files: List[str]
        +directory: str
        +return: List[str]
    }
    
    class digital_photo_frame {
        +local_dir: str
        +usb_dir: str
        +images: List[str]
        +root: tk.Tk
        +label: tk.Label
        +update_image(index: int): void
        +run: void
    }
    
    get_image_files --> digital_photo_frame : Used by
    digital_photo_frame ..> update_image : Defines
    digital_photo_frame --> tkinter.Tk : Creates root
    digital_photo_frame --> tkinter.Label : Creates label
    digital_photo_frame --> Image.open : Uses
    digital_photo_frame --> ImageTk.PhotoImage : Uses
    update_image --> Image.open : Opens image
    update_image --> ImageTk.PhotoImage : Converts to PhotoImage
    update_image --> tk.Label.config : Updates label
</div>