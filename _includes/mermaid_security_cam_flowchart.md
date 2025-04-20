<div class="mermaid">
flowchart LR
    A(Prepare your laptop) --> B(Install an operating system on Raspberry Pi)
    B --> C(Attach the camera to Raspberry Pi)
	C --> D(Write the Bash code on Raspberry Pi)
    D --> E("Refine the project (optional)")
	
	click A "https://aninditabasu.github.io/pi-projects/topics/set_up_laptop.html"
	click B "https://aninditabasu.github.io/pi-projects/topics/pi_zero_install_os.html"
	click D "https://aninditabasu.github.io/pi-projects/topics/bash_security_camera.html"
	click E "https://aninditabasu.github.io/pi-projects/topics/security_camera_refine.html"
	
	classDef boxstyle fill:white,stroke:#2c3e50,stroke-width:3px,font-family: monospace;
    class A,B,C,D,E boxstyle;
</div>