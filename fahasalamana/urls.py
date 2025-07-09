# fahasalamana/urls.py (assuming 'fahasalamana' is your app name)

from django.urls import path
from .views import * # Izany no antony tsy mila 'views.pejy_fandraisana' intsony

urlpatterns = [
    path('', fandraisana, name='fandraisana'), # Anaran'ny 'name' natao 'home' mba hifanaraka amin'ny template
                                            # fa ny anaran'ny view dia 'pejy_fandraisana'
    # Zava-maniry
    path('zavamaniry/', zavamaniry_list_view, name='zavamaniry_list'),
    path('zavamaniry/<int:pk>/', zavamaniry_detail_view, name='zavamaniry_detail'),

    # Mpitsabo
    #path('mpitsabo/', mpitsabo_list_view, name='mpitsabo_list'),

    # Auth & Inscription
    path('fisoratana/mpampiasa/', fisoratana_mpampiasa, name='fisoratana_mpampiasa'),
    path('fidirana/mpampiasa/', fidirana_mpampiasa, name='fidirana_mpampiasa'),
    path('mpitsabo/fisoratana/', fisoratana_mpitsabo, name='fisoratana_mpitsabo'),
    path('mpitsabo/fidirana/', fidirana_mpitsabo, name='fidirana_mpitsabo'),
    path('mpitsabo/pejy/', pejy_mpitsabo, name='pejy_mpitsabo'),

    # Hafatra
    path('hafatra/', pejy_hafatra, name='pejy_hafatra'),
    path('hafatra/<int:mpandray_id>/', hafa_hafatra, name='hafa_hafatra'),

    # --- ROUTES Ho an'ny Fandraisana sy Antsipiriany (Sosokevitra sy Aretina) ---
    path('sosokevitra/<int:pk>/', antsipiriany_sosokevitra, name='sosokevitra_detail'), # Antsipiriany Sosokevitra
    path('aretina/', lisitra_aretina, name='aretina_list'), # Lisitry ny Aretina
    path('aretina/<int:pk>/', aretina_detail, name='aretina_detail'), # Antsipiriany Aretina
    path('fanafody/', fanafody_list, name='fanafody_list'), # Lisitry ny Fanafody

    # --- Fanampiny (mifototra amin'ny teo aloha) ---
    path('mpitsabo/list_for_mpampiasa/', mpitsabo_list_for_mpampiasa, name='mpitsabo_list_for_mpampiasa'),
    path('mpampiasa/list_for_mpitsabo/', mpampiasa_list_for_mpitsabo, name='mpampiasa_list_for_mpitsabo'),
    path('deconnexion/', deconnexion_mpampiasa, name='deconnexion'),
    
    path('indexa/', indexa, name='indexa'),
    path('bot/', valina_boty, name='bot'),

]