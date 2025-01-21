<div class="mermaid">
%%{init: {"themeVariables": {"background": "#bdc3c7", "primaryColor": "#2c3e50", "fontFamily": "monospace", "lineWidth": 2}}}%%
erDiagram
    get_image_files {
        string directory
        List~string~ image_files
        List~string~ image_extensions
        List~string~ result
    }

    digital_photo_frame {
        string local_dir
        string usb_dir
        List~string~ images
        tkinterTk root
        tkinterLabel label
    }

    update_image {
        int index
    }

    digital_photo_frame ||--|| get_image_files : Calls
    digital_photo_frame ||--o{ update_image : Defines
    update_image ||--o{ Imageopen : Uses
    update_image ||--o{ ImageTkPhotoImage : Converts
    update_image ||--o{ tkLabel : Updates
</div>