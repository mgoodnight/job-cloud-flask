from job_clouds_server import create_app

if __name__ == '__main__':
    cloud_app = create_app()
    cloud_app.run(host="0.0.0.0", debug=cloud_app.config['DEBUG'], port=cloud_app.config['FLASK_PORT'])
