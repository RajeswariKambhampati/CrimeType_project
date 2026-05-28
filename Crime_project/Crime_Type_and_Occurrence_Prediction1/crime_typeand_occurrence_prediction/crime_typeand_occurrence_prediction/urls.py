"""crime_typeand_occurrence_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from Remote_User import views as remoteuser
from crime_typeand_occurrence_prediction import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


def index_view(request):
    from django.shortcuts import render
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
    path('login/', remoteuser.login, name="login"),
    path('logout/', remoteuser.logout_user, name="logout"),
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('Search_DataSets/', remoteuser.Search_DataSets, name="Search_DataSets"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path('Add_DataSet_Details/', remoteuser.Add_DataSet_Details, name="Add_DataSet_Details"),
    path('serviceproviderlogin/', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('serviceprovider_logout/', serviceprovider.serviceprovider_logout, name="serviceprovider_logout"),
    path('View_Remote_Users/', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    path('charts/<str:chart_type>/', serviceprovider.charts, name="charts"),
    path('charts1/<str:chart_type>/', serviceprovider.charts1, name="charts1"),
    path('likeschart/<str:like_chart>/', serviceprovider.likeschart, name="likeschart"),
    path('Find_Crime_Type_Ratio/', serviceprovider.Find_Crime_Type_Ratio, name="Find_Crime_Type_Ratio"),
    path('train_model/', serviceprovider.train_model, name="train_model"),
    path('Predict_Crime_Type/', serviceprovider.Predict_Crime_Type, name="Predict_Crime_Type"),
    path('Download_Trained_DataSets/', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
