from locust import HttpUser,task

 
class QuickstartUser(HttpUser):

    # def on_start(self):
    #     response=self.client.post('/loginurl',data={"username":"yechi","password":'sdgfg'}).json()
    #     self.client.headers={'Authorization': f"Bearer {response.get('access',None)}"}
    # @task
    # def postlist(self):
    #     self.client.get("/blog/api/v1/post/")
    @task
    def postdetail(self):
        self.client.get("/blog/api/v1/post/9/")
        # aaaaaaaaaaaaa