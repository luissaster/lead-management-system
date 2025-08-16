from django.shortcuts import render, redirect
from .forms import LeadForm

import requests
from decouple import config

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

                # Prepara os dados para enviar como JSON
                payload = {
                    'nome': lead.nome,
                    'email': lead.email,
                    'criado_em': lead.criado_em.isoformat()
                }

                # Envia a requisição POST e captura a resposta
                response = requests.post(webhook_url, json=payload, timeout=5)

                # Imprime os detalhes da resposta nos logs do Docker
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