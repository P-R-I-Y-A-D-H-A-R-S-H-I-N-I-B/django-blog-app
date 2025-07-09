from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populate categories"

    def handle(self, *args: Any, **options: Any) -> str | None:
        categories = [
            "Sports",
            "Technology",
            "Entertainment",
            "Politics",
            "Business",
            "Science",
            "Health",
            "Travel",
            "Food"
        ]

        for category in categories:
            Category.objects.get_or_create(name=category)

        self.stdout.write(self.style.SUCCESS("Categories populated successfully"))

