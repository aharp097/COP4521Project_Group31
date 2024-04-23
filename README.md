# COP4521Project_Group31

Things to install - 
sudo apt install redis-server
redis-cli ping # checks if it works, responds with pong if it does
pip install channels channels_redis
pip install uvicorn # this command could work instead sudo apt install uvicorn
export DJANGO_SETTINGS_MODULE=skechwime.settings
uvicorn skechwime.asgi:application --host 0.0.0.0 --port 8000 --log-level debug
