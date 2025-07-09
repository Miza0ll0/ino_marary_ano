from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Mpampiasa

from django.contrib.auth import logout 


from .models import Aretina, ZavaManiry, Fitsaboana, Mpitsabo, Hafatra,Mpampiasa
from .forms import FandraisanaMpampiasaForm, FidiranaMpampiasaForm, FandraisanaMpitsaboForm


def fandraisana(request):
    zavamaniry = ZavaManiry.objects.all()
    sosokevitra_list = list(Sosokevitra.objects.all())
    random.shuffle(sosokevitra_list)
    random_sosokevitra = sosokevitra_list[:4]  # tu peux ajuster le nombre

    return render(request, 'fandraisana.html', {
        'zavamaniry': zavamaniry,
        'random_sosokevitra': random_sosokevitra
    })



def zavamaniry_list_view(request):
    zavamaniry_list = ZavaManiry.objects.all().order_by('-daty_nampidirana')
    return render(request, 'zavamaniry_list.html', {'zavamaniry_list': zavamaniry_list})


def zavamaniry_detail_view(request, pk):
    zavamaniry = get_object_or_404(ZavaManiry, pk=pk)
    fitsaboana_list = Fitsaboana.objects.filter(zava_maniry=zavamaniry).select_related('aretina')
    return render(request, 'zavamaniry_detail.html', {
        'zavamaniry': zavamaniry,
        'fitsaboana_list': fitsaboana_list,
    })



def fisoratana_mpampiasa(request):
    if request.method == 'POST':
        form = FandraisanaMpampiasaForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('fandraisana')
    else:
        form = FandraisanaMpampiasaForm()
    return render(request, 'fisoratana_mpampiasa.html', {'form': form})


def fidirana_mpampiasa(request):
    if request.method == 'POST':
        form = FidiranaMpampiasaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('fandraisana')
    else:
        form = FidiranaMpampiasaForm()
    return render(request, 'fidirana_mpampiasa.html', {'form': form})


def fisoratana_mpitsabo(request):
    if request.method == 'POST':
        form = FandraisanaMpitsaboForm(request.POST, request.FILES)
        if form.is_valid():
            mpitsabo = form.save()
            login(request, mpitsabo.mpampiasa)
            return redirect('fandraisana')
    else:
        form = FandraisanaMpitsaboForm()
    return render(request, 'fisoratana_mpitsabo.html', {'form': form})


def fidirana_mpitsabo(request):
    if request.method == 'POST':
        form = FidiranaMpampiasaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and hasattr(user, 'mpitsabo'):
                login(request, user)
                return redirect('pejy_mpitsabo')
            else:
                form.add_error(None, "Tsy mpitsabo voasoratra ity kaonty ity")
    else:
        form = FidiranaMpampiasaForm()
    return render(request, 'fidirana_mpitsabo.html', {'form': form})


@login_required
def pejy_mpitsabo(request):
    if not hasattr(request.user, 'mpitsabo'):
        return redirect('fandraisana')
    return render(request, 'fandraisana.html')


@login_required
def pejy_hafatra(request):
    if hasattr(request.user, 'mpitsabo'):
        mpandray_hafatra = Hafatra.objects.filter(mpandray=request.user).order_by('-daty')
        return render(request, 'mpitsabo_hafatra.html', {
            'hafatra': mpandray_hafatra,
            'mpitsabo': True
        })
    else:
        mpitsabo_list = Mpitsabo.objects.all()
        return render(request, 'mpampiasa_hafatra.html', {
            'mpitsabo_list': mpitsabo_list,
            'mpitsabo': False
        })


@login_required
def hafa_hafatra(request, mpandray_id):
    mpandray = get_object_or_404(Mpampiasa, id=mpandray_id)


    if request.method == 'POST':
        votoaty = request.POST.get('votoaty')
        if votoaty:
            Hafatra.objects.create(
                mpandefa=request.user,
                mpandray=mpandray,
                votoaty=votoaty
            )
        return redirect('hafa_hafatra', mpandray_id=mpandray_id)

    hafatray = Hafatra.objects.filter(
        Q(mpandefa=request.user, mpandray=mpandray) |
        Q(mpandefa=mpandray, mpandray=request.user)
    ).order_by('daty')

    Hafatra.objects.filter(mpandefa=mpandray, mpandray=request.user, vakina=False).update(vakina=True)

    return render(request, 'hafa_hafatra.html', {
        'hafatra': hafatray,
        'mpandray': mpandray
    })

@login_required
def mpitsabo_list_for_mpampiasa(request):
    mpitsabo_list = Mpitsabo.objects.all()
    return render(request, 'mpitsabo_list_for_mpampiasa.html', {
        'mpitsabo_list': mpitsabo_list
    })

@login_required
def mpampiasa_list_for_mpitsabo(request):
    if not hasattr(request.user, 'mpitsabo'):
        return redirect('fandraisana')
    
    # Récupérer les mpampiasa qui ont envoyé un message à ce mpitsabo
    mpampiasa_ids = Hafatra.objects.filter(mpandray=request.user).values_list('mpandefa', flat=True).distinct()
    mpampiasa_list = Mpampiasa.objects.filter(id__in=mpampiasa_ids)
    
    return render(request, 'mpampiasa_list_for_mpitsabo.html', {
        'mpampiasa_list': mpampiasa_list
    })


def deconnexion_mpampiasa(request):
    logout(request)
    return redirect('fandraisana') 

from django.shortcuts import render
from .models import Aretina

def lisitra_aretina(request):
    aretina = Aretina.objects.all()
    return render(request, 'aretina_lisitra.html', {'aretina': aretina})

from django.shortcuts import render, get_object_or_404
from .models import Aretina

def aretina_detail(request, pk):
    aretina = get_object_or_404(Aretina, pk=pk)
    return render(request, 'aretina_mpitsony.html', {'aretina': aretina})

from django.shortcuts import render
from .models import Fanafody

def fanafody_list(request):
    fanafody = Fanafody.objects.all()
    return render(request, 'fanafody_lisitra.html', {'fanafody': fanafody})

from django.shortcuts import render, get_object_or_404
from .models import Sosokevitra
import random

def antsipiriany_sosokevitra(request, pk):
    sosokevitra = get_object_or_404(Sosokevitra, pk=pk)
    # Amboary ity andalana ity: toe_javatra fa tsy toe-javatra
    toe_javatra = {
        'sosokevitra': sosokevitra
    }
    return render(request, 'sosokevitra_mpitsony.html', toe_javatra)
# fahasalamana/views.py

from django.shortcuts import render, get_object_or_404
from .models import Sosokevitra # Ataovy azo antoka fa mbola misy ity raha mampiasa Sosokevitra ianao
import random # Ataovy azo antoka fa mbola misy ity raha mampiasa Sosokevitra kisendrasendra ianao

# ... (ireo fiasa views hafa) ...



import requests
from django.http import JsonResponse
from django.shortcuts import render
from . import config  # ← importe ton fichier config.py

def indexa(request):
    return render(request, 'index.html')

def valina_boty(request):
    question = request.GET.get("message", "")

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {config.OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": config.REFERER_URL,
                "X-Title": config.APP_NAME,
            },
            json={
                "model": config.MODEL,
                "messages": [
                    {"role": "system", "content": config.SYSTEM_PROMPT},
                    {"role": "user", "content": question}
                ]
            }
        )

        data = response.json()

        if "choices" in data:
            reply = data["choices"][0]["message"]["content"]
        else:
            reply = "Miala tsiny, tsy azoko tsara ilay fanontaniana."

    except Exception as e:
        reply = f"Error: {str(e)}"

    return JsonResponse({"reply": reply})
