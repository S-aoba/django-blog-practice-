from .models import Category

def common(requesu):
    category_data = Category.objects.all()
    context = {
        'category_data': category_data
    }
    return context
