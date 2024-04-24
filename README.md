#README- Group 31

For this project, we wanted to introduce a drawing app in which multiple people share the same canvas, and handle updates to the canvas in real time. A user must first create an account with any username, and a password that must include both letters and numbers. Once this account is created, the user can login, create or join an existing lobby, and they will be redirected to the lobby screen (where a list of players who are a member of that lobby is displayed). From the lobby screen, players can go to the canvas. At the canvas, users can interact with said canvas, go back to the lobby, or logout. <br>

Here are the libraries we used w/ the commands to install: <br>
Django (self explanatory): python -m pip install Django<br>
Django Channels (to handle WebSockets): pip install channels<br>
pathlib (for settings): pip install pathlib<br>
Fabric.js (for the canvas functionality): npm install fabric --save<br>
Websockets (for real-time updates): pip install websockets<br>
Redis-server (backend): sudo apt install redis-server<br>
redis-cli ping<br>
Channels_redus (websockets-redis-server integration): pip install channels channels_redis<br>
Uvicorn (running app w/ reddis-server): pip install uvicorn # this command could work instead sudo apt install uvicorn<br>
export DJANGO_SETTINGS_MODULE=skechwime.settings<br>
uvicorn skechwime.asgi:application --host 0.0.0.0 --port 8000 --log-level debug<br>

Other resources:<br>
Django Debug Toolbar<br>

Separation of work:<br>
Autumn- HTML templates, views, lobby model<br>
John- Canvas implementation (including relevant section in canvas.html), websockets implementation, canvas model<br>
Edwin- URLs, Testing, Database Troubleshooting<br>
