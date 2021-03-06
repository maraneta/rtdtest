from django.core.management.base import BaseCommand, CommandError
from hazard_calculator.tasks import save_ingredient_hazards

class Command(BaseCommand):
    #args = '<poll_id poll_id ...>'
    args = '<document_path>'
    help = 'Imports and saves cas numbers and hazards into the database.'

    def handle(self, *args, **options):
        document_path = args[0]
#         for poll_id in args:
#             try:
#                 poll = Poll.objects.get(pk=int(poll_id))
#             except Poll.DoesNotExist:
#                 raise CommandError('Poll "%s" does not exist' % poll_id)
# 
#             poll.opened = False
#             poll.save()
        save_ingredient_hazards(document_path)
        #self.stdout.write('Successfully closed poll "%s"\n' % poll_id)