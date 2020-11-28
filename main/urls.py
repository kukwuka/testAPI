from django.urls import path

from .views import PollListView , PollDetailView , Asked_PoolsListView ,Asked_PoolsCreateView

urlpatterns = [
	path("poll/" , PollListView.as_view()),
	path("poll/<int:pk>/" , PollDetailView.as_view()),
	path("userpoll/<int:pk>" , Asked_PoolsListView.as_view()),
	path("ask/" , Asked_PoolsCreateView.as_view())
]