from django.test import TestCase
from .models import Line2
from django.db import models

class Line2TestCase(TestCase):

    def setUp(self):
        self.create_lines()

    def create_lines(self):
        lines = ["Hatchback", "Suvs", "Sedan"]
        for line in lines:
            new_line = Line2(name = line)
            new_line.save()

    def test_delete_line(self):
        self.assertEqual(len(Line2.objects.all()), 3)
        line = Line2.objects.get(pk = 1)
        line.delete()
        self.assertIsNotNone(line.deleted_at)
        self.assertEqual(len(Line2.objects.all()), 2)
    
    def test_deleted_line(self):
        line = Line2.objects.get(pk = 1)
        line.delete()
        with self.assertRaises(Line2.DoesNotExist):
            Line2.objects.get(pk = 1)

    def test_get_deleted_items(self):
        line = Line2.objects.get(pk = 1)
        line.delete()
        deleted_lines = Line2.objects.get_deleted()
        self.assertEqual(len(deleted_lines), 1)
    
    def test_get_items_without_deleted(self):
        line = Line2.objects.get(pk = 1)
        line.delete()
        lines = Line2.objects.all()
        self.assertEqual(len(lines), 2)
        self.assertEqual(line.name,  "Hatchback")
    
    def test_get_items_with_deleted(self):
        line = Line2.objects.get(pk = 1)
        line.delete()
        all_lines = Line2.objects.all_with_deleted()
        self.assertEqual(len(all_lines), 3)
    
    def test_filter_items_without_deleted(self):
        line = Line2.objects.get(pk = 1)
        line.delete()
        lines = Line2.objects.filter(name__contains="S")
        self.assertEqual(len(lines), 2)