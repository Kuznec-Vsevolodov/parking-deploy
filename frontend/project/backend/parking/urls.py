from django.urls import path, include
from .views import PlaceForOwnersListView, PlaceDetailView, SectorDetailView, SectorListView, Parking_placeDetailView, BookingListView, ParkingPlaceListView, WalletDetailView, RegisterView, EventListView, EventDetailView, PlacesListView, SectorsByPlaceView, PlaceRedoDetailView, ParkingPlaceBySectorView
from rest_framework.authtoken import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('red-places/', PlaceForOwnersListView.as_view()),
    path('red-places/<int:pk>/', PlaceRedoDetailView.as_view()),
    path('places/', PlacesListView.as_view()),
    path('places/<int:pk>', PlaceDetailView.as_view()),
    path('sectors/', SectorListView.as_view()),
    path('sectors/<int:pk>/', SectorDetailView.as_view()),
    path('places/sectors/<int:pk>', SectorsByPlaceView.as_view()),
    path('parking_places/', ParkingPlaceListView.as_view()),
    path('parking_places/<int:pk>/', Parking_placeDetailView.as_view()),
    path('sectors/parking_places/<int:pk>/', ParkingPlaceBySectorView.as_view()),
    path('booked_places/', BookingListView.as_view()),
    path('wallets/<int:pk>/', WalletDetailView.as_view()),
    path('register/', RegisterView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('events/', EventListView.as_view()),
    path('events/<int:pk>/', EventDetailView.as_view()),
]