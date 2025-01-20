1.  Make sure your laptop is connected to the internet.
1.  Plug the microSD card into your laptop, and format it by running SD Card Formatter. Use the Overwrite option to format; this option takes longer but ensures that everything on the SD card is wiped clean and the card formatted.
1.  Run the Raspberry Pi Imager wizard and download Raspberry Pi's operating system to it. All Raspberry Pi run on  operating systems that are based on the open-source Debian operating system. This tutorial uses an operating system that's based on {{page.baseos}} and made for {{page.pimodel}}. Begin the download process by selecting the model as **{{page.pimodel}}** and the operating system as **{{page.pios}}**.
1.  On the page for OS customisation, click **Edit settings**. These settings are used for configuring the operating system for your use. If prompted for loading Wi-Fi credentials from your host computer, respond in the affirmative. Then, specify the values for at least the following parameters. It's also a good idea to note down these values somewhere for easy reference, because you'll need these values later:
    -  On the **General** page:
        -  **hostname**, which is a name you call your Raspberry Pi by. This is the name that'll be displayed when you search for your Raspberry Pi on the network.
	    -  **username** and **password**, which are the credentials that you'll use when logging in to Raspberry Pi remotely. The user that you specify here will have administrator privileges to your Raspberry Pi.
	    -  **Wireless LAN**, which should be prepopulated because you asked the Wi-Fi credentials to be loaded already.
	    -  **Locale settings**, for your time zone, keyboard preferences, and other such locale-related things.
	-  On the **Services** page, select the **Enable SSH** box and the option for password authentication.
    -  On the **Options** page, select all the options.
1.  Click **Save** and, when prompted for applying these settings, answer in the affirmative. Click **Yes** again, and then wait for the operating system to be copied on to the microSD card.
1.  When the process is complete, take the microSD card out of the laptop port.	
