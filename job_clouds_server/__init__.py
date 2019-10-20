from flask import Flask, request, jsonify, abort
import base64
import os
import uuid
import random
from .config import env_configs
from job_cloud.generator import ImageGenerator


def create_app():
    app = Flask(__name__)
    environment = os.getenv('ENVIRONMENT')
    app.config.from_object(env_configs[environment])

    @app.route("/generate", methods=['POST'])
    def generate_image():
        img_args = request.json

        keywords = img_args.get('keywords', list())
        keywords = dict([(kw['text'], int(kw['weight'])) for kw in keywords])

        job_description = img_args.get('jobDescription', None)
        job_title = img_args.get('jobTitle', None)
        job_location = img_args.get('jobLocation', None)

        theme = img_args.get('theme', None)

        if not theme or theme not in ['default', 'dusk', 'autumn', 'neon']:
            abort(400, "Please provide a valid theme")

        channel = img_args.get('channel', None)

        if not channel or channel not in ['linkedin', 'twitter', 'facebook', 'pinterest', 'instagram']:
            abort(400, "Please provide a valid channel")

        dimensions = app.config[channel.upper()]['SIZE']

        g = ImageGenerator(width=dimensions[0],
                           height=dimensions[1],
                           theme=theme,
                           cloud_font='arial-black',
                           text_font='arial-bold',
                           padding=40,
                           job_title_text=job_title,
                           job_location_text=job_location)

        gen_file = "/tmp/%s.%d.png" % (str(uuid.uuid4()), random.randint(0, 1000))
        g.generate(gen_file, phrases=keywords, description=job_description)

        with open(gen_file, "rb") as g_file:
            img_data = base64.b64encode(g_file.read())

        os.remove(gen_file)

        return jsonify({'image': img_data.decode("utf-8")})

    return app

