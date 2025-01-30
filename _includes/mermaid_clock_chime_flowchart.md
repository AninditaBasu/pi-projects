<div class="mermaid">
flowchart LR
    A("Fix the heat sinks on Raspberry Pi (optional)") --> B(Prepare your laptop)
    B --> C(Install an operating system on Raspberry Pi)
    C --> D(Write the Python code on Raspberry Pi)
	
	click A "https://aninditabasu.github.io/pi-projects/topics/pi_4_attach_heatsink.html"
	click B "https://aninditabasu.github.io/pi-projects/topics/set_up_laptop.html"
	click C "https://aninditabasu.github.io/pi-projects/topics/pi_4_install_os.html"
	click C "https://aninditabasu.github.io/pi-projects/topics/python_clock_chime.html"
	
	classDef boxstyle fill:white,stroke:#2c3e50,stroke-width:3px,font-family: monospace;
    class A,B,C,D,E,F boxstyle;
</div>