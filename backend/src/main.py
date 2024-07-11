from flask import Flask, send_file, jsonify
from flask_cors import CORS
from sudoku import Sudoku

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello World!"

# calculating some numbers to then deploy to backend
def perform_calculation():
    # Example calculation: sum of first 10 natural numbers
    result = sum(range(1, 5))
    return result

@app.route('/calculate')
def calculate():
    result = perform_calculation()
    return str(result)


# displaying a PDF
@app.route('/view-resume')
def view_resume():
    # Make sure to provide the correct path to your PDF file
    return send_file('Resume.pdf', mimetype='application/pdf', as_attachment=False)


# displaying a sudoku board
@app.route('/sudoku')
def sudoku():
    try:
        puzzle = Sudoku(3).difficulty(0.5)
        puzzle.solve()  # Assuming you want to solve it or display it solved
        # Convert the puzzle to a JSON-serializable format
        puzzle_data = [[puzzle.board[r][c] for c in range(9)] for r in range(9)]
        return jsonify(puzzle_data)
    except Exception as e:
        return str(e), 500


if __name__ == '__main__':
    app.run()