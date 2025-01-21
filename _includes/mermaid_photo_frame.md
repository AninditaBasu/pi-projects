<div class="mermaid">
flowchart LR
    A(Connect the touch display to Raspberry Pi) --> B(Fix the heat sinks on Raspberry Pi)
    B --> C(Prepare your laptop)
    C --> D(Download an operating system to the microSD card)
    D --> E(Write the Python code on Raspberry Pi)
	
	click A "https://aninditabasu.github.io/pi-projects/topics/pi_3b_attach_display.html"
	click B "https://aninditabasu.github.io/pi-projects/topics/pi_3b_attach_heatsink.html"
	click C "https://aninditabasu.github.io/pi-projects/topics/set_up_laptop.html"
	click D "https://aninditabasu.github.io/pi-projects/topics/pi_3b_install_os.html"
	click E "https://aninditabasu.github.io/pi-projects/topics/python_photo_frame.html"
	
	classDef boxstyle fill:white,stroke:#2c3e50,stroke-width:3px,font-family: monospace;
    class A,B,C,D,E boxstyle;
</div>