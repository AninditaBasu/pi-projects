<div class="mermaid">
flowchart LR
    A(Install rclone on the laptop) --> B(Install rclone on Raspberry Pi)
    B --> C(Connect rclone to your cloud storage)
    C --> D(Write a bash script to upload videos to cloud storage)
	D --> E(Create a cron job to automatically run this bash script)
	
	classDef boxstyle fill:white,stroke:#2c3e50,stroke-width:3px,font-family: monospace;
    class A,B,C,D,E boxstyle;
</div>