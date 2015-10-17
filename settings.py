from os.path import join, dirname
import dotenv

dotenv_path = join(dirname(__file__), '.env')

token = dotenv.get_variable(dotenv_path, "SECRET_TOKEN")
nome_fermata = dotenv.get_variable(dotenv_path, "NOME_FERMATA")
client_ticket = dotenv.get_variable(dotenv_path, "CLIENT_TICKET")

firenze = {
	"llLat": 43,
	"llLon": 10,
	"urLat": 44,
	"urLon": 12
}
