from catalog.models import Product, Category


class ProductsService:

    def __init__(self, **data):
        self.data = data

    def get_products(self):
        category = Category.objects.get(id=self.data.get('category_id'))
        category_ids = self.get_all_child_categories(category)
        queryset = Product.objects.filter(category_id__in=category_ids)
        if self.data.get('price_max'):
            queryset = queryset.filter(price__lte=self.data.get('price_max'))
        if self.data.get('price_min'):
            queryset = queryset.filter(price__gte=self.data.get('price_min'))
        return queryset

    def get_all_child_categories(self, category):
        category_ids = [category.id]
        for child in category.children.all():
            category_ids.extend(self.get_all_child_categories(child))
        return category_ids

    def get_category(self):
        category = Category.objects.get(id=self.data.get('category_id'))
        category_ids = self.get_all_child_categories(category)
        queryset = Category.objects.filter(id__in=category_ids)
        return queryset


