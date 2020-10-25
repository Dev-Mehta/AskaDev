from django.urls import path
from . import views
urlpatterns = [
	path('', views.OverView.as_view()),
	path('list/user-profile', views.UserProfileListView.as_view()),
	path('list/programming-language', views.ProgrammingLanguageListView.as_view()),
	path('trending/questions/', views.TrendingQuestionListView.as_view()),
	path('trending/developers', views.TrendingDeveloperListView.as_view()),
	path('question/<str:url>/', views.QuestionDetailView.as_view()),
	path('can-login/', views.CanLogin.as_view()),
	path('get-profile/', views.GetUserProfile.as_view()),
	path('get-language/', views.GetLanguage.as_view()),
	path('register/', views.RegisterUser.as_view()),
	path('get-questions/', views.GetQuestionsByUser.as_view()),
]