import time

from locust import HttpUser, between, task


class DummyUser(HttpUser):
    """Simulates a user for testing purposes."""

    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks

    @task
    def dummy_task(self) -> None:
        """A dummy task that simulates work without making actual requests."""
        # Simulate some processing time
        time.sleep(0.1)

        # Record a successful dummy request
        self.environment.events.request.fire(
            request_type="POST",
            name="dummy_endpoint",
            response_time=100,
            response_length=1024,
            response=None,
            context={},
            exception=None,
        )
