


from .models import SubcategoryModel, CategoryModel
from django_filters import rest_framework as filters



class CategoryFilter(filters.FilterSet):
    class Meta:
        model =CategoryModel
        fields =['category_name'    ]


class SubCategoryFilter(filters.FilterSet):
    class Meta:
        model =SubcategoryModel
        fields =['category',  'subcategory_name', "subcategory_state", "price"]