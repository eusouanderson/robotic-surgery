from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simular posição inicial do braço robótico
robotic_arm_position = {'x': 0, 'y': 0, 'z': 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move_arm', methods=['POST'])
def move_arm():
    global robotic_arm_position
    data = request.json
    direction = data.get('direction')
    if direction == 'up':
        robotic_arm_position['y'] += 1
    elif direction == 'down':
        robotic_arm_position['y'] -= 1
    elif direction == 'left':
        robotic_arm_position['x'] -= 1
    elif direction == 'right':
        robotic_arm_position['x'] += 1
    elif direction == 'forward':
        robotic_arm_position['z'] += 1
    elif direction == 'backward':
        robotic_arm_position['z'] -= 1
    return jsonify(robotic_arm_position)

@app.route('/position', methods=['GET'])
def position():
    return jsonify(robotic_arm_position)

if __name__ == '__main__':
    app.run(debug=True)
