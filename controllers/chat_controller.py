from odoo import http
from odoo.http import request

class ChatGPTController(http.Controller):

    @http.route('/chatgpt/send_message', type='json', auth='user')
    def send_message(self, message):
        connector = request.env['chatgpt.connector'].search([], limit=1)
        if not connector:
            return {'error': 'Connector not configured.'}

        answer = connector.send_message(message)
        return {'response': answer}
