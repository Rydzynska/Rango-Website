from django.test import TestCase
from rango.models import Category, Page
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify



class CategoryModelTests(TestCase):
    def test_string_representation(self):
        """
        Ensure relevant str representation is displayed
        """
        cat = Category(name='First category', views=-1, likes=0)
        cat.save()
        self.assertEqual(str(cat), cat.name)

    def test_ensure_views_are_positive(self):
        """
        ensure_views_are_positive should results True for categories
        where views are zero or positive
        """
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views>=0), True)

    def test_slug_line_creation(self):
        """
        Check if the appropriate slug line is created
        """
        cat = Category(name='Random Title For Category', views=5, likes=0)
        cat.save()
        self.assertEqual(cat.slug, 'random-title-for-category')



class PageModelTest(TestCase):
    def test_string_representation(self):
        new_page = Page(title='New Page', url='www.ww.ww', views=0)
        self.assertEqual(str(new_page), new_page.title)


def add_category(name, views, likes):
        new_cat = Category.objects.get_or_create(name=name)[0]
        new_cat.views = views
        new_cat.likes = likes
        new_cat.save()
        return new_cat

class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        If no category exists, an appropriate message
        is displayes.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'There are no categories present.')
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        """
        Check if the added categories are displayed
        """
        add_category('Interesting', 1, 2)
        add_category('Boring', 1, 1)
        add_category('Great', 5, 5)

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Great')

        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 3)

    def test_url(self):
        cat_name = 'This is my test category'
        add_category(cat_name, 1, 1)
        slug = slugify(cat_name)

        url = '/rango/category/{slug}/'.format(slug=slug)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='rango/category.html')

    def test_invalid_url(self):
        response = self.client.get('invalid/')
        self.assertEqual(response.status_code, 404)




