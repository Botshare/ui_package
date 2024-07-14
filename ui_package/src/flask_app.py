#!/usr/bin/env python3

from flask import Flask, render_template
import yaml
import rospy
app = Flask(__name__)


# def load_config(file_path):
#     with open(file_path, 'r') as config_file:
#         return yaml.safe_load(config_file)

# config = load_config('/home/ubuntu/catkin_ws/src/ui_package/param/config.yaml')


@app.route('/')
@app.route('/route')
@app.route('/control')
@app.route('/info')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    local_ip = rospy.get_param("appAddress", "127.0.0.1")
    local_port = rospy.get_param("portApp", "50505")
    
    app.run(host=local_ip, port=local_port)
