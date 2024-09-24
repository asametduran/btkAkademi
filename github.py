import requests 

class GitHub:
    def __init__(self):
        self.api_url = 'https://api.github.com'
        self.token = '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'

    def getUser(self,username):
        response =  requests.get(self.api_url+'/users/'+username)
        return response.json() #json formatina donusturuyor
    
    def getRepositories(self,username):
        response = requests.get(self.api_url+'/users/'+username+'/repos')
        return response.json() #json format
    def createRepository(self,name):
        requests.post(self.api_url+'/user'+'/repos?access_token='+self.token,json ={
            "name" : "Hello World"
        }
        )
        return response.json() #json format
github = GitHub()    

while True:
    secim = input('1-User\n2-Get Repositories\n3-Create Repository\n4-Exit\n Seçim:')

    if secim =='4':
        break
    else:
        if secim == '1':
            username = input('Kullanıcı Adı: ')
            result = github.getUser(username)
            print(f"name: {result['name']} public repos: {result['public_repos']} followers: {result['followers']}")
        elif secim == '2':
            username = input('Kullanıcı Adı: ')
            result = github.getRepositories(username)
            for repo in result:
                print(repo['name'])
        elif secim == '3':
            name = input('Repository Adı: ')
            result = github.createRepository(name)
            print(result)
        else:
            print("Hatalı Giriş!")
