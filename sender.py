import requests
file = {'answer': open('answer.json', 'rb')}
req = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=96912ca70fb8769ed3e504a21425e3c382d53604', files=file)

print(req.json())
