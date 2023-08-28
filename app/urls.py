from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyPasswordChangeForm

urlpatterns = [
    path("", views.home),
    path("product-detail/<int:id>", views.product_detail, name="product-detail"),
    path("cart/", views.add_to_cart, name="add-to-cart"),
    path("buy/", views.buy_now, name="buy-now"),
    path("profile/", views.profile, name="profile"),
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    path("categories-page/<int:id>", views.categories_page, name="categories_page"),
    path(
        "categories-page-filtered/<str:data>/<int:id>",
        views.filter_price,
        name="categories_page_filtered",
    ),
    # path('login/', views.login_page, name='login'),
    # authentication paths
    path("registration/", views.customerregistration, name="customerregistration"),
    path(
        "login/",
        auth_view.LoginView.as_view(
            template_name="app/login.html", authentication_form=AuthenticationForm
        ),
        name="login",
    ),
    path("logout/", auth_view.LogoutView.as_view(next_page="login"), name="logout"),
    path(
        "changepassword/",
        auth_view.PasswordChangeView.as_view(
            template_name="app/changepassword.html", form_class=MyPasswordChangeForm,
            success_url='/password_change_done/'
        ),
        name="changepassword",
    ),
    path(
        "password_change_done/",
        auth_view.PasswordChangeDoneView.as_view(
            template_name="app/passwordchangedone.html",
            
        ),
        name='password_change_done'
    ),
    path("checkout/", views.checkout, name="checkout"),
    # path('base/', views.base_file, name='base_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
