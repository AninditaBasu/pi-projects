<div class="mermaid">
flowchart LR
    A(Prepare your laptop) --> B(Install an operating system on Raspberry Pi)
    B --> C(Write the Bash code on Raspberry Pi)
    C --> D("Refine the project (optional)")
	
	click A "https://aninditabasu.github.io/pi-projects/topics/set_up_laptop.html"
	click B "https://aninditabasu.github.io/pi-projects/topics/pi_zero_install_os.html"
	
	classDef boxstyle fill:white,stroke:#2c3e50,stroke-width:3px,font-family: monospace;
    class A,B,C,D boxstyle;
</div>