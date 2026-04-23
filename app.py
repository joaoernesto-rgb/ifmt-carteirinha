{% extends 'base.html' %}
{% block title %}Acesso Negado{% endblock %}
{% block content %}
<div class="text-center py-5">
  <h1 class="display-1 text-danger">403</h1>
  <h4>Acesso Negado</h4>
  <p class="text-muted">Você não tem permissão para acessar esta página.</p>
  <a href="{{ url_for('index') }}" class="btn btn-ifmt">Voltar ao início</a>
</div>
{% endblock %}
