# TaskFlow — Documentação Funcional

> Documento mantido pelo time de desenvolvimento (Tech Lead).
> **Fonte de verdade dos requisitos:** Jira (projeto `SCRUM`).
> Última atualização: ver histórico do Git.

---

## 1. Visão geral do produto

**TaskFlow** é um sistema web de gestão de tarefas pessoais.

O usuário se cadastra, autentica-se e passa a gerenciar **suas próprias tarefas**
(criar, listar, alterar status e excluir) através de um dashboard.

O produto é intencionalmente pequeno: o objetivo é ter um sistema real, com
autenticação, persistência e regras de acesso, para servir de base para o
processo de desenvolvimento e QA.

---

## 2. Objetivo

Permitir que um usuário organizacione suas tarefas em um único lugar,
acompanhando o andamento de cada uma por meio de status.

---

## 3. Escopo

### Dentro do escopo (Sprint 1)

- Cadastro de usuários
- Login e logout
- Criar tarefa
- Listar tarefas no dashboard
- Alterar status da tarefa
- Excluir tarefa
- Isolamento de dados: cada usuário vê apenas as próprias tarefas

### Fora do escopo (no momento)

- Recuperação de senha
- Compartilhamento de tarefas entre usuários
- Notificações / e-mail
- Upload de anexos
- API pública
- Relatórios e métricas

> Itens fora do escopo não devem ser tratados como defeito. Se aparecer algo
> dessa lista, trate como **sugestão de melhoria**.

---

## 4. Perfis de usuário

| Perfil | Descrição | O que pode fazer |
|---|---|---|
| **Visitante** | Não autenticado | Acessar login e cadastro |
| **Usuário autenticado** | Com sessão ativa | Gerenciar **apenas** suas próprias tarefas |

Não existem perfis de administrador, gestor ou leitura nesta versão.

---

## 5. Ambientes e acesso

| Ambiente | URL | Observação |
|---|---|---|
| Dev / QA (local) | http://localhost:5000 | Flask + SQLite, servido no WSL |

- **Repositório:** https://github.com/ncnathaliaa83838gd-coder/taskflow
- **Banco:** SQLite (arquivo local, no ambiente). Não há banco compartilhado.
- **Sem dados pré-carregados:** o ambiente de QA sobe limpo.

---

## 6. Funcionalidades e requisitos funcionais

Os requisitos detalhados (com **critérios de aceite**) estão nas histórias do Jira.
Este documento não substitui o Jira — ele dá o panorama.

| Módulo | História | Descrição |
|---|---|---|
| Autenticação | [SCRUM-9] | Cadastro de usuário |
| Autenticação | [SCRUM-10] | Login |
| Tarefas | [SCRUM-11] | Criar tarefa |
| Tarefas | [SCRUM-12] | Listar tarefas |
| Tarefas | [SCRUM-13] | Atualizar status da tarefa |
| Tarefas | [SCRUM-14] | Excluir tarefa |

**Epics:**
- `SCRUM-7` — Autenticação de Usuários
- `SCRUM-8` — Gerenciamento de Tarefas

**Board:** https://ncnathaliaa.atlassian.net/jira/software/projects/SCRUM/boards/1

---

## 7. Fluxo de estados (workflow)

O fluxo de trabalho no board segue estas colunas:

```
Backlog
  -> Ready for Development
  -> In Development
  -> Code Review
  -> Ready for QA
  -> In QA
  -> Ready for Retest
  -> Regression
  -> Done
```

Estados de exceção no fluxo: uma tarefa pode voltar de **In QA** para
**In Development** (correção) e retornar em **Ready for Retest**.

---

## 8. Requisitos não funcionais

> ⚠️ **Não formalizados.** Esta seção está em aberto e é de responsabilidade do Tech Lead.

Os temas que precisam ser definidos e formalizados são:

- **Persistência e integridade dos dados**
- **Segurança de credenciais** (armazenamento e exposição)
- **Sessão** (tempo de vida, expiração, comportamento pós-logout)
- **Limites e validações de entrada** (tamanho de campos, valores aceitos)
- **Mensagens e comportamento de erro** expostos ao usuário
- **Isolamento de dados entre usuários**
- **Responsividade / compatibilidade de navegador**
- **Performance** (não há meta definida)

Enquanto não houver número acordado, **não trate como defeito** um
comportamento que seja apenas "não ideal" — **levante a dúvida** que a gente formaliza.

---

## 9. Regras de negócio

> ⚠️ **Não formalizadas em documento próprio.** As regras existentes estão
> implícitas nos critérios de aceite das histórias.

Ponto de atenção para o time: **regra de negócio que não está escrita no Jira
não existe como requisito.** Se durante a validação aparecer uma situação sem
regra definida, o caminho é:

1. Registrar a dúvida (comentar na issue ou abrir uma dúvida para o Tech Lead)
2. Tech Lead avalia
3. Se for decisão de produto -> **escalar para o Product Owner**

Não presuma comportamento e não trate suposição sua como requisito.

---

## 10. Padrões e critérios para testes

> ⚠️ **Não existe guia de padrões de teste no projeto.**

O que **não** está definido hoje:

- Template/formato de report de bug
- Definição de severidade x prioridade
- Critério de entrada e saída para QA
- Evidências obrigatórias (print, log, passos)
- Estratégia de regressão
- Definição de pronto (DoD) para QA

Enquanto isso não existir, o mínimo acordado com o time é que todo report contenha:

- **Passos para reproduzir**
- **Resultado esperado** (com base no critério de aceite)
- **Resultado obtido**
- **Evidência** (print, vídeo ou log)
- **Ambiente e versão** (commit)

---

## 11. Fontes de verdade

| Informação | Onde consultar |
|---|---|
| Requisitos e critérios de aceite | Jira — histórias do projeto `SCRUM` |
| Fluxo de trabalho / andamento | Board do Jira |
| Visão geral e como rodar | `README.md` (GitHub) |
| Documentação funcional | Este documento (`docs/`) |
| Código-fonte | GitHub (leitura) |

---

## 12. Glossário

| Termo | Significado |
|---|---|
| **Tarefa (Task)** | Item de trabalho do usuário no sistema |
| **Status** | Estado atual da tarefa: Pendente, Em Andamento, Concluído |
| **Prioridade** | Baixa, Média ou Alta |
| **Dashboard** | Tela principal do usuário autenticado, onde as tarefas são listadas |
| **Sessão** | Vínculo autenticado do usuário com o sistema após o login |
| **QA** | Ambiente de homologação onde as validações são executadas |

---

## 13. Contato / escalonamento

| Assunto | Responsável |
|---|---|
| Dúvida técnica, comportamento do sistema, ambiente | **Tech Lead** |
| Dúvida de produto, prioridade, regra de negócio | **Product Owner** |
