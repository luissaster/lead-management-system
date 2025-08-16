from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from django.db.models import Q
from .forms import LeadForm
from .models import Lead
from decouple import config
import requests

# Create your views here.

def lead_create_view(request):
    # Cria uma instância do nosso formulário
    form = LeadForm()

    if request.method == 'POST':
        # Preenche o formulário com os dados enviados pelo usuário
        form = LeadForm(request.POST)

        if form.is_valid():
            # Salva os dados no banco de dados, criando um novo Lead
            lead = form.save()

            # --- INÍCIO: Lógica do Webhook ---

            try:
                webhook_url = config('N8N_WEBHOOK_URL')

                # Prepara os dados para enviar
                payload = {
                    'nome': lead.nome,
                    'email': lead.email,
                    'criado_em': lead.criado_em.isoformat(),
                    'telefone': lead.telefone,
                    'empresa': lead.empresa,
                    'observacoes': lead.observacoes,
                }

                # Envia a requisição POST e captura a resposta
                response = requests.post(webhook_url, json=payload, timeout=5)

                # Imprime os detalhes da resposta nos logs do Docker
                # docker-compose logs challenge_web
                print("--- RESPOSTA DO N8N ---")
                print(f"Status Code: {response.status_code}")
                try:
                    print(f"JSON Body: {response.json()}")
                except requests.exceptions.JSONDecodeError:
                    print(f"Body (não é JSON): {response.text}")
                print("-----------------------")

            except requests.exceptions.RequestException as e:
                # Tratamento de erro aqui, mas irei apenas imprimir no log
                print(f"Erro ao enviar webhook para o n8n: {e}")

            # --- FIM: Lógica do Webhook ---

            return redirect('success_page')

    # Se a requisição for GET (primeiro acesso à página) ou o formulário for inválido,
    # renderiza a página com o formulário.
    context = {
        'form': form
    }
    return render(request, 'leads/lead_form.html', context)

def success_view(request):
    return render(request, 'leads/success.html')

def lead_list_view(request):
    queryset = Lead.objects.all().order_by('-criado_em')
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(nome__icontains=query) | Q(email__icontains=query)
        )

    paginator = Paginator(queryset, 10) # 10 leads por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'leads/lead_list.html', {'page_obj': page_obj})

def lead_detail_view(request, pk):
    from .models import Lead
    lead = get_object_or_404(Lead, pk=pk)
    return render(request, 'leads/lead_detail.html', {'lead': lead})

def dashboard_view(request):
    total_leads = Lead.objects.count()
    leads_today = Lead.objects.filter(criado_em__date=timezone.now().date()).count()
    leads_this_month = Lead.objects.filter(criado_em__year=timezone.now().year, criado_em__month=timezone.now().month).count()

    # Estatísticas por status
    leads_novo = Lead.objects.filter(status='NOVO').count()
    leads_em_andamento = Lead.objects.filter(status='EM_ANDAMENTO').count()
    leads_concluido = Lead.objects.filter(status='CONCLUÍDO').count()
    leads_perdido = Lead.objects.filter(status='PERDIDO').count()

    context = {
        'total_leads': total_leads,
        'leads_today': leads_today,
        'leads_this_month': leads_this_month,
        'leads_new': leads_novo,
        'leads_in_progress': leads_em_andamento,
        'leads_closed': leads_concluido,
        'leads_lost': leads_perdido,
    }
    
    return render(request, 'leads/dashboard.html', context)