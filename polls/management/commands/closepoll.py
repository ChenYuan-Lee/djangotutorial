from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser: ArgumentParser):
        # Positional args
        parser.add_argument("poll_ids", nargs="+", type=int)

        # Named (optional) args
        parser.add_argument(
            "--delete",
            action="store_true",
            help="delete polls instead of closing it",
        )

    def handle(self, *args, **options):
        for poll_id in options["poll_ids"]:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            if options["delete"]:
                poll.delete()
                
                self.stdout.write(
                    self.style.SUCCESS('Successfully deleted poll "%s"' % poll_id)
                )
            else:
                if not poll.is_open:
                    raise CommandError('Poll "%s" is already closed' % poll_id)
            
                poll.is_open = False
                poll.save()

                self.stdout.write(
                    self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
                )
