from locust import HttpUser, between, task


class LocalDemoUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def health(self):
        self.client.get("/health", name="/health")
