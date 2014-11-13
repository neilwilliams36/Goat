__author__ = 'nwilliams1'
from django.test import TestCase
from lists.models import Item, List
from django.core.exceptions import ValidationError
from django.utils.html import escape
from lists.forms import ItemForm, EMPTY_LIST_ERROR


class NewItemTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post('/lists/%d/' % (correct_list.id), data={'text': "A new item for an existing list"})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, "A new item for an existing list")
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post('/lists/%d/' % (correct_list.id), data={'text': "A new item for an existing list"})

        self.assertRedirects(response, '/lists/%d/'%(correct_list.id))

    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()
            #item.save()

    def test_can_save_same_item_to_two_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean() #should not raise error



class ItemModelTest(TestCase):

    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_list_ordering(self):
        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='item1')
        item2 = Item.objects.create(list=list1, text='item2')
        item3 = Item.objects.create(list=list1, text='item3')

        self.assertEqual(list(Item.objects.all()), [item1, item2, item3])

    def test_string_representation(self):
        item = Item(text="some text")
        self.assertEqual(str(item), 'some text')



class NewListTest(TestCase):

    def test_can_save_a_post_request(self):
        self.client.post('/lists/new', data={'text': 'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')


    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'text': 'A new list item'})
        new_list = List.objects.first()
        self.assertRedirects(response, '/lists/%d/'%(new_list.id))

