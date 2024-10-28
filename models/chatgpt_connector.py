import requests
from odoo import api, fields, models
from odoo.exceptions import UserError

class ChatGPTConnector(models.Model):
    _name = 'chatgpt.connector'
    _description = 'ChatGPT Integration Connector'

    name = fields.Char(string='Name', default="ChatGPT Connector")
    api_key = fields.Char(string="API Key", required=True)
    conversation_history = fields.One2many('chatgpt.message', 'connector_id', string="Conversation History")

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }

    def send_message(self, question):
        """Enviar mensagem ao ChatGPT e retornar resposta."""
        url = "https://api.openai.com/v1/chat/completions"
        payload = {
            "model": "gpt-4",
            "messages": [
                {"role": "user", "content": question}
            ],
            "temperature": 0.7
        }

        response = requests.post(url, headers=self._get_headers(), json=payload)
        if response.status_code == 200:
            answer = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
            # Salvar pergunta e resposta no histórico
            self.env['chatgpt.message'].create({
                'connector_id': self.id,
                'user_message': question,
                'gpt_response': answer
            })
            return answer
        else:
            raise UserError("Erro na comunicação com o ChatGPT. Verifique a chave API.")
        

class ChatGPTMessage(models.Model):
    _name = 'chatgpt.message'
    _description = 'ChatGPT Message'

    connector_id = fields.Many2one('chatgpt.connector', string="Connector")
    user_message = fields.Text(string="User Message")
    gpt_response = fields.Text(string="ChatGPT Response")
    timestamp = fields.Datetime(string="Timestamp", default=fields.Datetime.now)
