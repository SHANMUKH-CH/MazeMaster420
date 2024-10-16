from flask import Flask, render_template, request, redirect, url_for
from src.maze_game import MazeGame

app = Flask(__name__)

game = MazeGame()

@app.route('/')
def index():
    return render_template('maze_game.html', maze=game.maze, player_pos=game.player_pos, game_over=game.is_game_over())

@app.route('/move', methods=['POST'])
def move():
    direction = request.form['direction']
    game.move(direction)
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    game.generate_maze()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)