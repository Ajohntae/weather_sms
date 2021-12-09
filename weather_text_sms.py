
#date time import #pytext now import date

python3 -m venv env
.gitignore

source env/bin/activate

pip install pytextnow
pip install pythonweather
pip install asyncio


textnowclient = pytextnow.Client("username", sid_cookie="sid", csrf_cookie="csrf" )

from datetime import date
todaydate = date.today()

import python_weather, asyncio, pytextnow



async def getweather():
    client = python_weather.client(format=python_weather.IMPERIAL)

weather = await client.find("New York City")

#form and send text message

if todaytime == 06:00
client.send_sms("number",'This is your morning reminder sent bright & early at', todaytime,'it is currently', weather.current.temperature , 'degrees outside!')

await client.close()

