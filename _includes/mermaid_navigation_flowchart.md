<div class="mermaid">
flowchart LR
    A(Prepare your laptop) --> B(Prepare a Raspberry Pi 3B)
	A --> C(Prepare a Raspberry Pi 4)
    B --> D(Set up a photo frame)
    C --> E(Set up hourly chimes)
	A --> F(Prepare a Raspberry Pi Zero 2W)
	F --> E
	F --> G(Set up a security system)
    C --> H(...under construction: cloud storage...)
	F --> I(...under construction: car dashcam...)
	
	click A "https://aninditabasu.github.io/pi-projects/topics/set_up_laptop.html"
	click B "https://aninditabasu.github.io/pi-projects/topics/pi_3b_install_os.html"
	click C "https://aninditabasu.github.io/pi-projects/topics/pi_4_install_os.html"
	click D "https://aninditabasu.github.io/pi-projects/topics/photo_frame.html"
	click E "https://aninditabasu.github.io/pi-projects/topics/clock_chime.html"
	click F "https://aninditabasu.github.io/pi-projects/topics/pi_zero_install_os.html"
	click G "https://aninditabasu.github.io/pi-projects/topics/security_camera.html"
	
	classDef boxstyle fill:white,stroke:#2c3e50,stroke-width:3px,font-family: monospace;
    class A,B,C,D,E,F,G boxstyle;
</div>