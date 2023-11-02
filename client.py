import requests
body = {
    
    "sex_0male_1female":1,
    "episode_number":1,
    "hospital_outcome_1alive_0dead":1
}
response = requests.post(url = 'http://127.0.0.1:8000/score',
              json = body)
print (response.json())
# output: {'score': 0.866490130600765}


