from locust import HttpUser, task, between

class FlaskAppUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def visit_home(self):
        self.client.get("/")

    @task(2)
    def visit_homepage(self):
        self.client.get("/home")

    @task(1)
    def trigger_error(self):
        self.client.get("/error")

    @task(1)
    def trigger_404(self):
        self.client.get("/randompage")