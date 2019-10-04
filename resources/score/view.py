from flask import request
from flask_restful import Resource
from flasgger import Swagger, swag_from
from .controller import total_score


class ScoreResource(Resource):
    def post(self): 
        """
        Score
        ---
        tags:
          - score
        parameters:
          - in: body
            name: body

        responses:
          201:
            description: The task has been created
          400:
            description: No input data provided
          400:
            description: Unknown error
        """
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # getting score
        try:
            score = total_score(json_data['score'])
        except Exception as e:
            print(e)
            return {'message': 'Unknown error'}, 400
           
        result = {'total score': score}
        return { "message": 'success', 'data': result }, 201