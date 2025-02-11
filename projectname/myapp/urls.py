from django.urls import path
from .views import get_products,save_product ,CustomerListCreateView,LoginView,ProtectedView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'customers', CustomerViewSet)

"""include (Used in urls.py) – Includes URL configurations from another file.
exclude (Used in QuerySets) – Excludes certain records from the database query."""
urlpatterns = [
    # path('', home, name='home'),
    path('products/', get_products, name='get_products'),
    path('save_product/', save_product, name='save_product'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('Protected/', ProtectedView.as_view(), name='Protected'),
]