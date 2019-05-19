# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import requests

class shipping_service(models.Model):
    _name = 'hospitality_services.shipping_service'

    api_token = 'TEST_/fGYCaXvQ2Ep41DgR2RP6q+PagxOO0hrDwNxwRAFwWQ'
    api_url_rates = 'https://api.shipengine.com/v1/rates'
    headers = {'Content-Type': 'application/json', 
      'api-key': api_token}

    to_name = fields.Char()
    to_address_line1 = fields.Char()
    to_city = fields.Char()
    to_state = fields.Char()
    to_postal_code = fields.Char()
    to_country_code = fields.Char()
    
    from_name = fields.Char()
    from_phone = fields.Char()
    from_address_line1 = fields.Char()
    from_city = fields.Char()
    from_state = fields.Char()
    from_postal_code = fields.Char()
    from_country_code = fields.Char()

    weight_value = fields.Float()

    cost = fields.Float(compute="_get_rates")
    
    @api.depends('to_name', 'to_address_line1', 'to_city', 'to_state', 'to_postal_code', 'to_country_code', 'from_name', 'from_phone',
                'from_address_line1', 'from_city', 'from_state', 'from_postal_code', 'from_country_code', 'weight_value')
    def _get_rates(self):
        payload = {
            "shipment": {
                "ship_to": {
                    "name": self.to_name,
                    "address_line1": self.to_address_line1,
                    "city_locality": self.to_city,
                    "state_province": self.to_state,
                    "postal_code": self.to_postal_code,
                    "country_code": self.to_country_code
                },
                "ship_from": {
                    "name": self.from_name,
                    "phone": self.from_phone,
                    "address_line1": self.from_address_line1,
                    "city_locality": self.from_city,
                    "state_province": self.from_state,
                    "postal_code": self.from_postal_code,
                    "country_code": self.from_country_code
                },
                "packages": [
                    {
                        "weight": {
                            "value": self.weight_value,
                            "unit": "pound"
                        }
                    }
                ]
            },
            "rate_options": {
                "carrier_ids": [
                    "se-133869"
                ]
            }
        }
        r = requests.post(self.api_url_rates, headers = self.headers, data = json.dumps(payload))
        json1_data = json.loads(r.text)
        all_costs = []
        for rate in json1_data["rate_response"]["rates"]:
            all_costs.append(float(rate["shipping_amount"]["amount"]))

        self.cost = (min(all_costs))