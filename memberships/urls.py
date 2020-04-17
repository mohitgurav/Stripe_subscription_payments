from django.urls import path

from .views import MembershipSelectView, payment_view, update_transaction_records, cancel_subscription, profile_view

urlpatterns = [
    path('', MembershipSelectView.as_view(), name='select'),
    path('payment/', payment_view, name='payment'),
    path('update-transactions/<subscription_id>/',
         update_transaction_records, name='update-transactions'),
    path('profile/', profile_view, name='profile'),
    path('cancel/', cancel_subscription, name='cancel')
]
