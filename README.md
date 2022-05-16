# Vacuum bot

This small webserver enables any person to easily move a vacuum cleaner remotely. You can attach a camera/mobile to it in order for the user to see around (video-call needs to be done separately). Note that this is only the frontend service, you need a backend that can move the vacuum already.

<img width="398" alt="Screenshot 2022-05-16 at 12 16 11" src="https://user-images.githubusercontent.com/5374768/168581148-bd04b52f-582c-4ccb-a576-d7f9d32dffeb.png">

<img width="375" alt="Screenshot 2022-05-16 at 12 16 37" src="https://user-images.githubusercontent.com/5374768/168581231-df8a8933-5be0-4aae-ba14-6a475e70b421.png">

## How it works

The webserver sends move commands to my Home Assistant which is turn connected to my Eufy Vacuum. However, you should modify the `vacuum_control.py` to suit whatever API you have available.

## Requirements

- python3 (`pip install -r requirements.txt`).
- Webserver should be accessible from the internet (I used my computer with port forwarding).
- API available to control the vacuum cleaner.
