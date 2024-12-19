from odoo import http
from odoo.http import request
import logging
import json
# import base64
_logger = logging.getLogger(__name__)


class UserAPI(http.Controller):

    @http.route(
        "/api/get_user", type="json", auth="public", methods=["GET"], csrf=False
    )
    def get_users(self):
        users = request.env["users.custom"].sudo().search([])
        return [
            {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "status": user.status,
                "role": user.role,
                "userpic": user.userpic.decode('utf-8') if user.userpic else None
            }
            for user in users
        ]

    @http.route(
        "/api/create_user", type="json", auth="public", methods=["POST"], csrf=False
    )
    def create_user(self):

        # _logger.info(f"Received data: {kwargs}")
        # files = request.httprequest.files
        # Extract raw data from request
        raw_data = request.httprequest.data

        # Decode the raw data from bytes to string
        decoded_data = raw_data.decode("utf-8")

        # Parse the decoded string as JSON
        data = json.loads(decoded_data)

        # Logging the data for debugging
        _logger.info(f"Received data: {data}")

        # Extract fields from the JSON request
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        status = data.get("status")
        role = data.get("role")
        userpic = data.get('userpic')
        # if userpic:
        #     data['userpic'] = base64.b64encode(userpic.read()).decode('utf-8')

        # Create the user in the custom model
        user = (
            request.env["users.custom"]
            .sudo()
            .create(
                {
                    "name": name,
                    "email": email,
                    "password": password,
                    "status": status,
                    "role": role,
                    "userpic":userpic,
                }
            )
        )


        user = request.env['users.custom'].sudo().create(data)
        # _logger.info(f"Created user: {user}")
        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "password": user.password,
            "status": user.status,
            "role": user.role,
            "userpic": user.userpic.decode('utf-8') if user.userpic else None
        }

    @http.route("/api/update_user/<int:user_id>", type="json",auth="public",methods=["PUT"],csrf=False,)
    def update_user(self, user_id):
        raw_data = request.httprequest.data
        decoded_data = raw_data.decode("utf-8")
        data = json.loads(decoded_data)
        _logger.info(f"Received data: {data}")

        user = request.env["users.custom"].sudo().browse(user_id)
        if user:
            user.sudo().write(
                {
                    "name": data.get("name"),
                    "email": data.get("email"),
                    "password": data.get("password"),
                    "status": data.get("status"),
                    "role": data.get("role"),
                    "userpic":data.get("userpic")
                }
            )
            return {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "status": user.status,
                "role": user.role,
                'userpic': user.userpic.decode('utf-8') if user.userpic else None,
            }
        else:
            return {"error": "User not found"}

    @http.route("/api/delete_user/<int:user_id>",type="json",auth="public",methods=["DELETE"],csrf=False,)
    def delete_user(self, user_id):
        user = request.env["users.custom"].sudo().browse(user_id)
        if user:
            user.sudo().unlink()
            return {"status": "User deleted"}
        else:
            return {"error": "User not found"}
