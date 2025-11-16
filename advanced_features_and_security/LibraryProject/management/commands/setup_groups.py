from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Setup default groups and permissions"

    def handle(self, *args, **kwargs):
        # Define groups
        groups_permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_edit", "can_create"],
            "Admins": ["can_view", "can_edit", "can_create", "can_delete"],
        }

        for group_name, perm_codes in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_code in perm_codes:
                try:
                    permission = Permission.objects.get(codename=perm_code)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stderr.write(f"Permission {perm_code} not found.")

        self.stdout.write("Groups and permissions setup completed.")

