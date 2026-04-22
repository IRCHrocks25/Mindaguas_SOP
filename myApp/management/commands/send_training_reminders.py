from django.core.management.base import BaseCommand

from myApp.utils.notifications import dispatch_due_reminders


class Command(BaseCommand):
    help = 'Send due SOP training reminders via Resend'

    def handle(self, *args, **options):
        result = dispatch_due_reminders(limit=500)
        self.stdout.write(self.style.SUCCESS(
            f"Processed reminders: {result['processed']} (sent={result['sent']}, failed={result['failed']})"
        ))
