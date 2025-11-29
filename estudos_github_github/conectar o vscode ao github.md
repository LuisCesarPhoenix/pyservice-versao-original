# Passo a passo para enviar o projeto do VS Code para o GitHub e sincronizar as alterações.

## Pré-requisitos:

```text
a) Conta no GitHub: Se você ainda não tem uma, crie uma conta gratuita em https://github.com
b) Git instalado: O Git é essencial para controlar as versões do seu código. Você pode baixá-lo em https://git-scm.com/
c) VS Code instalado: Certifique-se de ter o Visual Studio Code instalado no seu computador. Você pode baixá-lo em
https://code.visualstudio.com/download
d) Extensão GitHub: Após baixar e instalar o VS Code, instale a extensão "GitHub Pull Requests and Issues" no VS Code para
facilitar a integração com o GitHub.
```

### Passo 1: Criar um repositório no GitHub

a) Acesse sua conta no GitHub e clique no botão "New" (Novo) para criar um novo repositório.<br/>
b) Dê um nome ao seu repositório (por exemplo, "meu-projeto").<br/>
c) Você pode adicionar uma descrição (opcional).<br/>
d) Escolha se o repositório será público ou privado.<br/>
e) Marque a opção "Add a README file" (Adicionar um arquivo README) para criar um arquivo de documentação inicial.<br/>
f) Clique em "Create repository" (Criar repositório).

### Passo 2: Inicializar o Git no repositório local do seu projeto (VS Code)

a) Logue com a sua conta do GitHub no VS Code.<br/>
b) Abra a pasta do seu projeto no VS Code.<br/>
c) Abra o terminal integrado do VS Code (Visualizar > Terminal > New terminal ou CTRL + J).<br/>
- observação: ALT + Z quebra a linha.<br/>
d) No terminal, execute o seguinte comando para inicializar um repositório Git dentro do repositório local do seu projeto:
- git init<br/>
e) dê os seguintes comandos no git:
- config --global user.email "cesarrodriguesgoncalves@hotmail.com" (substitua pelo seu email)
- git config --global user.name "LuisCesarPhoenix" (substitua pelo seu nome de usuário)

Observação:
- O --global define essa configuração para todos os repositórios no seu computador.
- Se quiser configurar apenas para um projeto específico, remova --global e execute dentro da pasta do projeto.

### Passo 3: Conectar o repositório local ao repositório remoto (GitHub)

a) Dentro do repositório que você criou no GitHub, clique no botão verde escrito Code e copie a URL do repositório. A URL (HTTPS
ou SSH) do repositório termina com .git<br/>
b) No terminal do VSCode, execute o seguinte comando:
- git remote add origin https://github.com/LuisCesarPhoenix/curso-youtube-react-next-typescript.git
- substitua pela URL do seu repositório.

### Passo 4: Adicionar e commitar os arquivos

a) Use o comando git add caminhnho-do-arq/diretório/arquivo para adicionar os arquivos do seu projeto à área de preparação do Git.
Exemplo: git add src/controllers/migrationController.js<br/>
b) Use o comando git commit -m "Mensagem inicial do commit" para criar um commit para cada arquivo. Substitua "Mensagem inicial do
commit" por uma mensagem descritiva.
- Exemplo: git commit -m "Corrigida conexão no migrationController.js"

### Passo 5: Enviar os arquivos para o GitHub

- Use o comando git push -u origin nome-da-branch para enviar seus commits para o repositório remoto no GitHub.
- No meu caso eu usei o master, mas você pode substituir.
- Porém o mais indicado é criar uma branch de trabalho para cada atualização e depois de revisar, discutir e mesclar as alterações à branch principal, excluir essa branch temporária.
- Para criar uma branch diferente, antes de fazer um git push, você pode executar o comando git checkout -b nome-da-branch
- Em seguida executa o comando git branch para saber qual branch está sendo usada e depois você executa o comando git push -u origin nome-da-branch.

### Passo 6: Sincronizar alterações futuras

Sempre que você fizer alterações no seu código no VS Code:<br/>
a) Use git add caminhnho-do-arq./diretório/arquivo para adicionar as alterações.<br/>
- Exemplo: git add src/config/mongoConfig.js
b) Use o comando git commit -m "Mensagem descritiva das alterações" para criar um novo commit.<br/>
- Exemplo: git commit -m "Refatorado método queryMongoDB para melhorar reutilização"
c) Use git push -u origin nome-da-branch para enviar seus commits para o repositório remoto no GitHub.

### Dicas adicionais:

```text
-Arquivo .gitignore: Crie um arquivo .gitignore na raiz do seu projeto para ignorar arquivos e pastas que você não quer enviar
para o GitHub (por exemplo, arquivo de configuração de variáveis de ambiente(.env), pastas de dependências,etc).
-Branches: Use branches para desenvolver novas funcionalidades ou corrigir bugs sem afetar a versão principal do seu código.
-Pull requests(Solicitação de pull): Use pull requests para revisar e discutir as alterações antes de mesclá-las à branch
principal.
```

## Quando você altera vários arquivos de uma vez, pode seguir dois caminhos no VS Code para descrever cada alteração de forma clara antes de fazer o commit:

### 1) Fazendo commits para cada arquivo:

a) Usando o Terminal (Manual para cada Arquivo)<br/>
Se quiser descrever alterações separadamente para cada arquivo modificado, pode adicionar os arquivos individualmente e fazer
commits distintos:
- git add src/controllers/migrationController.js
- git commit -m "Corrigida conexão no migrationController.js"
- git add src/config/mongoConfig.js
- git commit -m "Refatorado método queryMongoDB para melhorar reutilização"
- git push

Observação: utilize o comando git status para ver o caminho de cada arquivo alterado.

b) Usando o VS Code (Interface Gráfica)
- Abra o VS Code e clique no ícone do Git (canto esquerdo, terceiro ícone).
- Você verá a lista de arquivos modificados em "Changes".
- Clique com o botão direito no arquivo ou no sinal de +(Stage Changes) do arquivo que quer commitar primeiro.
- Digite uma mensagem de commit específica para aquele arquivo e clique em "Commit".
- Repita o processo para os outros arquivos, adicionando mensagens personalizadas.
- Depois, clique em "Sync Changes" (ou rode git push no terminal) para enviar os commits para o repositório remoto.

### 2 - Fazendo um Commit Único Com Uma Mensagem Detalhada

Se quiser fazer um único commit, mas com uma descrição mais detalhada, pode usar este comando:

git commit -m "Refatoração do código<br/>
Corrigida conexão no migrationController.js<br/>
Melhorada reutilização do queryMongoDB no mongoConfig.js<br/>
Ajustados logs para maior clareza"

git push

```text
****************************************************************************************************************************
```

## Como fazer um versionamento(controle de versões):

### Depois de gerar os commits, você pode executar um dos comandos a seguir:

a) Caso seja uma versão de patch:
- npm version patch
- v1.0.0 versão inicial
- v1.0.1 versão atualizada

A versão patch normalmente é usada para atualizações pequenas, correções, etc...

b) Caso seja uma versão minor:
- npm version minor
- v1.0.0 versão inicial
- v1.1.0 versão atualizada

A versão minor normalmente é usada quando você adiciona alguma funcionalidade ou novo componente.

c) Caso seja uma versão major:
- npm version major
- v1.0.0 versão inicial
- v2.0.0 versão atualizada

A versão major normalmente é usada para atualizações significativas, que normalmente podem modificar dependências e tornar a
aplicação incompatível com algum outro sistema.

Exemplo:<br/>
A aplicação está disponível com packages compatíveis com node 20, porém você adiciona um pacote que depende do node 22,
isso pode acarretar em incompatibilidade com projetos que usam o node 20. Então você atualiza para a versão major.

Depois de fazer um dos 3 versionamentos(npm version patch, npm version minor ou npm version major), você executa o seguinte
comando:
- git push -u origin nome-da-branch --tags

Caso você esteja confiante na atualização, você pode enviar a nova tag direto para o master(ou main):
- git push -u origin master --tags

Caso tenha algum erro, você pode voltar para a versão anterior executando o checkout:<br/>
Exemplo:<br/>
Existem duas versões, a antiga(v1.0.1) e a nova(v1.0.2), caso tenha ocorrido alguma falha na v1.0.2, você executa o
checkout na versão v1.0.1
- git checkout v1.0.1

```text
****************************************************************************************************************************
```

## Como clonar o repositório do Github no VS Code:

### Clonar um repositório do GitHub diretamente no VS Code é uma maneira eficiente de começar a trabalhar em projetos. Aqui estão os passos para realizar essa ação:

1) Abra a Paleta de Comandos:
- No VS Code, pressione Ctrl + Shift + P (Windows/Linux) ou Cmd + Shift + P (Mac) para abrir a Paleta de Comandos.
2) Digite "Git: Clone":
- Na Paleta de Comandos, digite "Git: Clone" e selecione a opção correspondente.
3) Forneça a URL do Repositório:
- Você será solicitado a fornecer a URL do repositório Git que deseja clonar. Cole a URL do repositório GitHub que você copiou
anteriormente.
4) Login no Github:
- Se você estiver logado no github pelo VS code, ele apresentará seus repositórios para clonagem, facilitando o processo.
5) Escolha o Diretório de Destino:
- Selecione a pasta onde você deseja clonar o repositório.
6) Aguarde a Conclusão:
- O VS Code irá lidar com o processo de clonagem. Aguarde até que o processo seja concluído.
- O VS code irá perguntar se você deseja abrir o repositório clonado, clique em abrir.

Dicas adicionais:<br/>

1) Extensão Git:
- O VS Code possui suporte integrado para Git, mas certifique-se de que a extensão Git esteja habilitada.
- Você também pode usar o terminal integrado do VS Code para executar o comando git clone diretamente.
- Para abrir o terminal, pressione Ctrl + j ou Visualizar(...) > Terminal > New terminal(Windows/Linux) ou Cmd + j (Mac).

2) Branches de trabalho:
- É melhor criar branches de acordo com o assunto que você está alterando.
- Criar branches específicas para cada funcionalidade ou correção ajuda a manter o repositório organizado e facilita a revisão de
código.

3) Como mudar de branch:
- git branch (para listar todas as branches existentes)
- git checkout nome-da-branch ou git switch nome-da-branch(para trocar para a branch desejada)

```text
****************************************************************************************************************************
```

## Como fazer um fork:

### Vamos detalhar os passos para fazer um fork e enviar suas alterações usando o VS Code.

```text
Pré-requisitos:

a) Conta no GitHub: Se você ainda não tem uma, crie uma conta gratuita em https://github.com
b) Git instalado: O Git é essencial para controlar as versões do seu código. Você pode baixá-lo em https://git-scm.com/
c) VS Code instalado: Certifique-se de ter o Visual Studio Code instalado no seu computador. Você pode baixá-lo em
https://code.visualstudio.com/download
d) Extensão GitHub: Após baixar e instalar o VS Code, instale a extensão "GitHub Pull Requests and Issues" no VS Code para
facilitar a integração com o GitHub.
```

### 1. Fazer o Fork no GitHub (pelo navegador):

A) Acesse o repositório no GitHub:
- Abra o navegador e vá para o repositório que você deseja fazer o fork.
B) Clique no botão "Fork":
- No canto direito superior da página do repositório, clique no botão "Fork".
- Selecione a sua conta do GitHub onde o fork será criado.
C) Aguarde a criação do fork:
- O GitHub criará uma cópia do repositório na sua conta.

### 2. Baixar o Repositório Remoto do Seu Fork para a sua máquina:

A) Crie uma pasta no seu notebook com o nome do seu fork:
- Por exemplo: ecoapiv2-fork
B) Abra a pasta do seu projeto no VS Code ou clique com o botão direito dentro da pasta e escolha a opção abrir com o VS Code.
C) Abra o terminal integrado do VS Code (Visualizar > Terminal > New terminal ou CTRL + J) e escolha a opção Git bash.
- Observação: ALT + Z quebra a linha.
D) No terminal, execute o seguinte comando para inicializar um repositório Git dentro do repositório local do seu projeto:
- git init
E) Copie a URL do seu fork:
- No GitHub, vá para o repositório do seu fork.
- Clique no botão verde "Code" e copie a URL do repositório (HTTPS ou SSH).
- Por exemplo: https://github.com/LuisCesarPhoenix/ecoapiv2-fork.git
F) Adicione o repositório remoto:
- No terminal, execute o seguinte comando:
- git remote add origin https://github.com/LuisCesarPhoenix/ecoapiv2-fork.git
- Isso liga sua pasta local ao repositório no GitHub.
G) Agora puxe todo o conteúdo do seu fork para dentro da pasta local:
- git pull origin main
- Obs: se o branch principal do fork for master (em vez de main), troque por git pull origin master
- Se não souber qual é o nome do branch principal, você pode verificar no GitHub — vai aparecer logo no topo do repositório. Ex: branch: main.
H) Verificar se o código foi baixado:
- Depois do git pull, veja se os arquivos aparecem na pasta: ls

### 3. Próximo passo: manter o seu fork atualizado com o original

A) Sempre que o projeto original for atualizado, você pode sincronizar assim:
- git fetch upstream
- git merge upstream/main
B) Se não quiser revisar as mudanças antes de aplicar, pode usar:
- git remote add upstream https://github.com/REPO-ORIGINAL.git
- git pull upstream main
- Isso trará todas as novas alterações do repositório original para o seu fork local.

### 4. Agora você pode trabalhar no projeto

Você já pode:
- Editar arquivos
- Fazer commits com git add . && git commit -m "mensagem"
- E enviar para o seu fork com: git push origin main

```text
****************************************************************************************************************************
```

## CRIAR UM PULL REQUEST (PR) NO GITHUB:

A) utilize o comando git status para ver o caminho de cada arquivo alterado.
- git status
B) Adicionar e commitar os arquivos
- Use o comando git add caminhnho-do-arq/diretório/arquivo para adicionar os arquivos do seu projeto à área de preparação do Git.
- Exemplo: git add src/controllers/migrationController.js
C) Use o comando git commit -m "Mensagem inicial do commit" para criar um commit para cada arquivo. Substitua "Mensagem inicial do
commit" por uma mensagem descritiva.
- Exemplo: git commit -m "Corrigida conexão no migrationController.js"
D) Acesse o seu fork no GitHub:
- Abra o navegador e vá para o seu fork do repositório.
E) Clique no botão "Compare & pull request":
- O GitHub deve exibir um aviso indicando que você enviou um novo branch.
- Clique no botão "Compare & pull request".
F) Preencha os detalhes do PR:
- Adicione um título e uma descrição para o seu PR.
- Certifique-se de que o branch base seja o branch correto no repositório original.
G) Clique no botão "Create pull request":
- O seu PR será criado e enviado para o repositório original.

### Observação:

- Eu nunca vou enviar o commit para a branch main do repositório original.
- Eu vou criar uma branch temporária no meu repositório.
- git checkout -b nome-da-branch
- Depois eu vou enviar a Pull Request da minha branch temporária para a branch secundária do repositório original.
- Quando eu estiver enviando uma Pull Request para o fork jamais eu vou clicar no Merge

```text
Dicas:
1-Use mensagens de commit descritivas para explicar suas alterações.
2-Mantenha seu fork sincronizado com o repositório original.
3-Siga as diretrizes de contribuição do projeto original.
```

```text
****************************************************************************************************************************
```

## COMO APAGAR UMA BRANCH

### 1. Apagar a branch local

Como a branch já existe, apague assim:
- Deletar branch local (SE NÃO estiver nela)
- git branch -D nome-da-branch

Porém se você estiver dentro da branch, mude para outra antes:
- git checkout nome-da-branch ou ou git switch nome-da-branch
- git branch -D nome-da-branch

### 2. Apagar a branch no GitHub (branch remota)

Se a branch também existe no seu GitHub, apague assim:
- git push origin --delete nome-da-branch

```text
****************************************************************************************************************************
```

## CRIANDO UM NOVO REPOSITÓRIO NO GITHUB

Quick setup — if you’ve done this kind of thing before
or
https://github.com/LuisCesarPhoenix/n8n.git
Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

…or create a new repository on the command line

echo "# n8n" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/LuisCesarPhoenix/n8n.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/LuisCesarPhoenix/n8n.git
git branch -M main
git push -u origin main

```text
****************************************************************************************************************************
```

## The default branch has been renamed!

The default branch on the parent repository has been renamed!
fabiopasilva1/iframe-saemas renamed its default branch main

You can rename this fork's default branch to match in branch settings

master is now named main

If you have a local clone, you can update it by running the following commands.

git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a

```text
****************************************************************************************************************************
```

## SINTAXE BÁSICA DE FORMATAÇÃO MARKDOWN(.md)

https://www.markdownguide.org/basic-syntax/

```text
****************************************************************************************************************************
```

## COMO DESFAZER UM COMMIT

O que você vai fazer depende se você já enviou (push) ou não para o GitHub.

Segue abaixo os dois casos:

### CASO 1 — Você NÃO deu push ainda

(Este é o mais simples)

Você pode voltar no tempo e desfazer aquele commit gigante em vários commits separados.

A) Voltar 1 commit, mantendo o código na sua máquina:
- git reset HEAD~1
B) Voltar 2 commits, mantendo o código na sua máquina:
- git reset HEAD~2

Isso remove o commit, mas mantém todas as alterações no working directory, como se você nunca tivesse commitado.

Agora é só fazer seus commits separados:
- git add arquivo1
- git commit -m "Commit 1"
- git add arquivo2
- git commit -m "Commit 2"
- E assim por diante.

### CASO 2 — Você JÁ deu push para o GitHub

Você ainda pode desfazer, mas é mais delicado.

Se ninguém mais usa esse branch:
- git reset --soft HEAD~1
- git push --force

IMPORTANTE:
--force sobrescreve o histórico remoto.
Use apenas se for seu branch pessoal.

Qual tipo de "reset" usar?
1) --soft
- Apaga o commit, mas mantém tudo staged
2) sem opções
- Apaga o commit, deixa tudo unstaged
3) --hard
- Apaga o commit e o código ← NÃO USE aqui

Para separar commits, use sempre soft ou normal (sem opção).

```text
****************************************************************************************************************************
```
