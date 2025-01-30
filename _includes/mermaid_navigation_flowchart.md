<div class="mermaid">
flowchart LR
    A(Prepare your laptop) --> B(Prepare a Raspberry Pi 3B)
	A --> C(Prepare a Raspberry Pi 4)
    B --> D(Set up a photo frame)
    C --> E(Set up hourly chimes)
	A --> F(Prepare a Raspberry Pi Zero 2W)
	F --> G(...under construction: surveillance...)
    C --> H(...under construction: cloud storage...)
	
	click A "https://aninditabasu.github.io/pi-projects/topics/set_up_laptop.html"
	click D "https://aninditabasu.github.io/pi-projects/topics/photo_frame.html"
	click E "https://aninditabasu.github.io/pi-projects/topics/clock_chime.html"
	
	classDef boxstyle fill:white,stroke:#2c3e50,stroke-width:3px,font-family: monospace;
    class A,B,C,D,E boxstyle;
</div>