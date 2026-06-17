# Organizador-de-Arquivos:
Esse simples script organiza arquivos com extensões diversas e espalhados em um diretório, movendo os para os devidos lugares. Foi escrito em python e executado apenas em ambiente linux, eu não recomendo o uso de multiplos diretório para organização de arquivos, caso você queira melhorar a ferramenta e adicionar essa funcionalidade.

# Requisitos:
- Python 3+
- Lib os - shutil
- Linux ou Windows

# Como usar:
Dentro do script temos uma linha com 'destino = os.path.expenduser('~/Documentos')', ou seja do diretório Documentos localizado na pasta do usuário logado(Representado por ~), vamos pegar o caminho absoluto através do caminho relativo. Em seguida o script prossegue a execução se o diretório existir. Você pode mudar o diretório que será executado o script através dessa linha e vê a automação acontecendo.

Para executar o script digite no terminal e no diretório onde o script está localizado:

```python
python3 organizador.py
```

E ele fará tudo para você, ou quase tudo porque no momento ainda não verifica todas as extensões de arquivos e eu ainda estou estudando novas forma e lógica de criar linhas para o script mover para pastas diferente arquivos com extensões não conhecidas.


<img width="633" height="307" alt="Captura_de_tela_20260617_121159" src="https://github.com/user-attachments/assets/47b569ac-87e7-4f5f-b5d5-506bf29c0472" />

