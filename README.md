# ChatGPT Integration for Odoo 14

Este módulo integra o Odoo com o ChatGPT, permitindo interações e conversas no canal Discuss.

## Requisitos
- Odoo 14
- API Key da OpenAI para o ChatGPT.

## Instalação
1. Coloque o módulo `chatgpt_integration` no diretório de addons.
2. Ative o modo de desenvolvedor no Odoo.
3. Instale o módulo via menu de Aplicativos.

## Configuração
1. Vá para o menu "ChatGPT Integration".
2. Insira a chave de API e salve.
3. No Discuss, abra o canal "ChatGPT" para começar a conversar com o ChatGPT.

## Uso
- No canal Discuss, envie mensagens e receba respostas do ChatGPT em tempo real.
- Todo o histórico de conversas é salvo no sistema para futuras referências.

## Estrutura
- `chatgpt.connector`: Conector principal com a API.
- `chatgpt.message`: Modelo para armazenar histórico de conversas.
- `chatgpt.controller`: Rota HTTP para enviar e receber mensagens do ChatGPT.

## Contribuição
Contribuições são bem-vindas. Envie pull requests ou abra issues para melhorias.

## Licença
MIT
