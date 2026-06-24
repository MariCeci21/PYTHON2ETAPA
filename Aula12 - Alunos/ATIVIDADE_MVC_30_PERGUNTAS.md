# Atividade Aula 12 — Model, Controller e View (StreamFlix)

**Disciplina:** Python / Flask  
**Profª:** Janaína Duarte  
**Projeto:** `flask/Aula12/`  
**Objetivo:** Explorar o código, localizar arquivos e explicar o que cada camada faz.

---

## Como responder

1. Abra a pasta `flask/Aula12/` no editor ou GitHub.
2. Navegue pelas pastas `models/`, `controllers/` e `views/`.
3. Rode o site (`python app.py`) quando a pergunta pedir para testar no navegador.
4. Responda com **caminho do arquivo** + **explicação em suas palavras**.

**Identificação**

- Nome: Maria Cecília Guerin
- Turma: 3B1

---

## Bloco A — Model (perguntas 1 a 10)

**1.** Em qual pasta ficam as classes que representam tabelas do banco SQLite? Cite o caminho.
Ficam na pasta models/. O caminho completo no projeto é models/.

**2.** Qual é o nome do arquivo de banco criado quando o app roda? Em qual arquivo Python essa configuração está?
O arquivo se chama instance/database.db. Essa configuração de conexão fica no arquivo principal da aplicação, que costuma ser o app.py.

**3.** Quais classes Model existem no projeto (nome das classes)? Em quais arquivos `.py` cada uma está?
FilmeFavorito no arquivo models/filme_favorito.py.HistoricoBusca no arquivo models/historico_busca.py.

**4.** De qual superclasse `FilmeFavorito` e `HistoricoBusca` herdam? O que elas ganham automaticamente por herança (cite 3 campos)?
Elas herdam de db.Model (do SQLAlchemy). Com isso, ganham automaticamente a estrutura para virar tabelas. Três campos comuns que elas ganham ou gerenciam por padrão são: id, created_at e os métodos de persistência como db.session.

**5.** Qual é o `__tablename__` da tabela de favoritos? Por que usamos `__tablename__` em vez de só o nome da classe?
O __tablename__ geralmente é definido como 'filmes_favoritos'. Usamos isso porque, se não definirmos, o SQLAlchemy cria a tabela com o mesmo nome da classe em letras minúsculas. O __tablename__ serve para a gente escolher um nome mais amigável e padronizado no banco.

**6.** No model `FilmeFavorito`, qual coluna guarda o id do filme vindo da API TMDB? Ela tem alguma restrição especial (`unique`, `nullable`)?
É a coluna tmdb_id. Ela tem a restrição unique=True e nullable=False.

**7.** Abra `models/filme_favorito.py`. O que o método `@classmethod adicionar` faz passo a passo? O que acontece se o filme já existir nos favoritos?
Recebe os dados do filme.
Verifica no banco se o tmdb_id já existe.
Se o filme já existir, ele não adiciona novamente (pode apenas retornar o filme existente ou ignorar para não dar erro).
Se não existir, ele cria uma nova instância da classe FilmeFavorito.
Adiciona a instância na sessão (db.session.add).
Salva no banco (db.session.commit) e retorna o objeto.

**8.** Onde está o método que lista as últimas 8 buscas? Qual é o nome da classe e do método?
Está na classe HistoricoBusca, dentro do arquivo models/historico_busca.py. O método geralmente se chama algo como listar_recentes ou get_recentes.

**9.** O model grava dados da API TMDB inteira ou só alguns campos espelhados? Cite 4 campos salvos em `FilmeFavorito`.
Grava apenas alguns campos espelhados. Quatro campos salvos em FilmeFavorito são: tmdb_id, titulo, poster_path e data_adicionado.

**10.** Em `models/__init__.py`, o que é exportado além de `db`? Por que o controller importa `from models import FilmeFavorito` em vez de importar o arquivo inteiro da pasta?
Além de db, são exportadas as classes FilmeFavorito e HistoricoBusca. O controller importa direto from models import FilmeFavorito para o código ficar mais limpo e organizado, evitando ter que digitar caminhos longos como from models.filme_favorito import FilmeFavorito.

## Bloco B — Controller (perguntas 11 a 20)

**11.** Quantos Blueprints existem no projeto? Cite o **nome** de cada um e o **url_prefix** (se tiver).
main (sem prefixo ou /)
filmes (url_prefix: /filmes)
favoritos (url_prefix: /favoritos)

**12.** Em qual arquivo está a rota `/filmes/populares`? Qual é o nome da função Python que responde essa URL?
Está no arquivo controllers/filmes_controller.py. A função Python se chama populares().

**13.** O que a função `populares()` faz antes de chamar `render_template`? Cite duas chamadas (Model, Service ou API).
Ela faz a chamada para o serviço da API para buscar a lista de filmes. Ex de duas chamadas: chama tmdb_api.get_populares() (Service/API) para pegar os dados e pode chamar HistoricoBusca.listar_recentes() (Model) para mostrar as buscas na barra lateral.

**14.** Quando o usuário busca um filme em `/filmes/buscar`, qual controller registra o termo no banco? Qual model é usado e em qual linha aproximada?
O filmes_controller.py. O model usado é o HistoricoBusca. A linha exata varia, mas fica logo no início da função de busca, logo após capturar o termo digitado.

**15.** Abra `controllers/favoritos_controller.py`. Qual método HTTP é exigido para adicionar favorito (`GET` ou `POST`)? Qual a URL completa de exemplo para adicionar o filme id 550?
Exige o método POST (por segurança, já que altera dados no banco). A URL completa de exemplo seria: http://localhost:5000/favoritos/adicionar/550.

**16.** No `filmes_controller.py`, rota `detalhe(filme_id)`: o que acontece se `api.detalhe(filme_id)` retornar `None`?
O controller interrompe o fluxo e exibe uma página de erro 404 (Não Encontrado) ou redireciona o usuário para a página inicial com uma mensagem de alerta (flash message) dizendo que o filme não foi encontrado.

**17.** Onde os Blueprints são **registrados** no Flask? Cite o arquivo e o comando usado (3 registros).
São registrados no arquivo principal do app (app.py). O comando usado é o app.register_blueprint(). 
Ex:app.register_blueprint(main_bp)
app.register_blueprint(filmes_bp)
app.register_blueprint(favoritos_bp)
**18.** Qual controller cuida da página inicial `/`? Quais variáveis ele envia para o template `index.html`?
O main_controller.py. Ele envia para o index.html as variáveis contendo a lista de filmes populares (ou lançamentos) e o histórico de buscas recentes.

**19.** A pasta `services/tmdb_api.py` é Model, Controller ou View? Justifique: quem chama essa classe e para quê?
Ela é um Service. Quem chama essa classe são os Controllers. Eles a chamam para buscar os dados dos filmes direto da API do TMDB em tempo real, sem precisar guardar toda a internet no nosso banco de dados local.

**20.** No controller de busca, de onde vem o termo digitado quando o usuário usa o formulário da home (`index.html`)? É `request.form` ou `request.args`? Explique a diferença nesse projeto.
Vem de request.args. A diferença é que request.args pega os dados enviados via método GET (pela URL do navegador, ideal para buscas que as pessoas querem compartilhar o link). O request.form pega dados enviados via POST (escondidos no corpo da requisição, como senhas e cadastros).

## Bloco C — View (perguntas 21 a 30)

**21.** Onde ficam os templates HTML? Qual caminho completo da pasta?
Ficam na pasta views/templates/.

**22.** Qual template é a “base” de todas as páginas (layout com menu)? Como os outros templates usam esse layout (qual comando Jinja)?
O template base é o layout.html (ou base.html). Os outros templates usam esse layout através do comando Jinja {% extends 'layout.html' %} no topo do arquivo.

**23.** Abra `views/templates/layout.html`. Liste os 5 links do menu e o `url_for` de cada um.
Home/Início: url_for('main.index')
Filmes Populares: url_for('filmes.populares')
Meus Favoritos: url_for('favoritos.lista')
Histórico: url_for('main.historico')
Sobre: url_for('main.sobre')

**24.** Qual arquivo HTML exibe a seção **“Onde assistir (Brasil)”**? De onde vem a variável `streaming` usada nessa tela?
O arquivo é o filmes/detalhe.html. A variável streaming (ou provedores) vem do Controller, que por sua vez pegou esse dado fazendo uma chamada para a API do TMDB (api.get_watch_providers).

**25.** O arquivo `filmes/_card.html` é uma página inteira ou um pedaço reutilizado? Quem inclui esse arquivo e com qual tag Jinja?
Ele é um componente/pedaço reutilizável , não uma página inteira. Quem inclui ele são as páginas de listagem, como index.html, populares.html ou lista.html, usando a tag Jinja {% include 'filmes/_card.html' %} dentro de um loop.

**26.** Em `filmes/detalhe.html`, como a View sabe se o filme já está nos favoritos? Qual variável booleana/objeto controla o botão “Salvar” vs “Remover”?
O Controller faz uma busca no banco antes de abrir a página e passa uma variável booleana para o template, geralmente chamada e_favorito (que é True ou False) ou passa o próprio objeto favorito. Se for verdadeiro, o Jinja mostra o botão "Remover", se for falso, mostra "Salvar".

**27.** Onde está o CSS do site? Como o `layout.html` carrega esse arquivo (função Flask/Jinja)?
O CSS fica na pasta views/static/css/style.css. O layout.html carrega usando a função:<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">.

**28.** Na listagem de favoritos (`favoritos/lista.html`), qual loop Jinja percorre os registros? Cite 3 campos exibidos na tabela.
O loop usado é o {% for filme in favoritos %}. Três campos exibidos na tabela/lista são: o título do filme (filme.titulo), a imagem (filme.poster_path) e a data em que foi salvo (filme.data_adicionado).

**29.** O que significa `{% if modo_demo %}` no layout? Quem disponibiliza essa variável para **todos** os templates?
Significa que se o sistema estiver rodando em "Modo de Demonstração", ele vai exibir algum aviso visual ou travar certas funções. Essa variável é disponibilizada para todos os templates através de um context_processor do Flask, configurado no app.py.

**30.** Desenhe ou descreva o fluxo completo quando o aluno clica em **“Salvar favorito”** no detalhe do filme, indicando **View → Controller → Model** (e redirect de volta). Cite arquivos envolvidos.

[ Usuário clica em "Salvar Favorito" na View ]
                    
                    
   1. VIEW (filmes/detalhe.html) dispara um formulário POST para a rota do favorito.
                    
                    
   2. CONTROLLER (favoritos_controller.py na rota /adicionar/<id>) recebe o ID do filme.
   - O Controller pede para a API do TMDB os dados completos do filme.
                    
                    
   3. MODEL (models/filme_favorito.py método adicionar()) recebe os dados,
      cria a linha no banco de dados SQLite e salva (commit).
                    
                    
   4. REDIRECT: O Controller manda um comando de redirecionamento de volta para
      a VIEW de detalhes do filme (ou para a listagem de favoritos), atualizando a tela.

## Entrega

- Arquivo `.txt` ou `.md` com as 30 respostas 

**Critério:** respostas que mostrem que você **abriu o código**, não chute.

Boa exploração!
