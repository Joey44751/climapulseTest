from django.core.management.base import BaseCommand
from ...models import Vessel
from django.db import transaction, IntegrityError,connection
import threading


class Command(BaseCommand):
    help = "Simulate condition when withdrawing refrigerant from a vessel."

    def handle(self, *args, **kwargs):
        Vessel.objects.all().delete()
        vessel = Vessel.objects.create(name="Test Vessel", content=50.0)
        self.vessel_id = vessel.id
        self.stdout.write("Simulating condition...")
        connection.commit()
        self.run_simulation()

    def run_simulation(self):
        barrier = threading.Barrier(2)
        amount = 10

        def user1():
            barrier.wait()
            with transaction.atomic():
                vessel = Vessel.objects.select_for_update().get(id=self.vessel_id)
                try:
                    if vessel.content >= amount:
                        vessel.content -= amount
                        vessel.save()
                    else:
                        self.stdout.write(
                            f"Cannot withdraw {amount} kg: vessel only has {vessel.content} kg left."
                        )
                except IntegrityError:
                    self.stdout.write("Cannot withdraw: vessel is empty.")

        def user2():
            barrier.wait()
            with transaction.atomic():
                vessel = Vessel.objects.select_for_update().get(id=self.vessel_id)
                try:
                    if vessel.content >= amount:
                        vessel.content -= amount
                        vessel.save()
                    else:
                        self.stdout.write(
                            f"Cannot withdraw {amount} kg: vessel only has {vessel.content} kg left."
                        )
                except IntegrityError:
                    self.stdout.write("Cannot withdraw: vessel is empty.")

        t1 = threading.Thread(target=user1)
        t2 = threading.Thread(target=user2)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        vessel = Vessel.objects.get(id=self.vessel_id)
        self.stdout.write(f"Remaining content: {vessel.content} kg")
