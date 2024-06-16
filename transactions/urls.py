from django.urls import path

from transactions.views import TransactionListView, TransactionFilterView

urlpatterns = [
    path('my_transactions/', TransactionListView.as_view()),
    path('filter/', TransactionFilterView.as_view())
]
