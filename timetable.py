import requests
import serialize
import settings
import datetime

schedule_url = 'http://www.temporealeataf.it/Mixer/Rest/PublicTransportService.svc/schedule'

client_ticket = settings.client_ticket

today = datetime.datetime.now()
today = today.replace(
		hour=0,
		minute=0,
		second=0,
		microsecond=0
	)

def timetable():
	payload = {
		"nodeID": "FM0122",
		"lat": "43.787796666666665",
		"lon": "11.249808333333334",
		"timezone": "+2",
		"s": serialize.getDynamicPassword(settings.client_ticket),
		"_": 0
	}

	r = requests.get(schedule_url, params=payload)
	try:
		return pretty_print(r.json())
		
	except ValueError:
		return "Non sono riuscito ad ottenere gli orari per i prossimi 30 minuti"

def pretty_print(obj):
	message =  "Linea {number} - direzione {direction}, arrivo {arrival}"
	for i in obj:
		arrival_time = today + datetime.timedelta(
				hours=2,
				milliseconds=int(i['d'])
				)
		formatted =  message.format(
				number=i['n'],
				direction=i['t'],
				arrival= arrival_time.time()
				)
		yield formatted
