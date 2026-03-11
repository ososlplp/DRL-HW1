from flask import Flask, render_template, request, jsonify
import random
import copy

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/evaluate', methods=['POST'])
def evaluate():
    """
    接收前端資料，執行策略評估，回傳每個格子的策略（箭頭）與 V(s)。
    """
    data = request.get_json()
    n = data['n']
    start = tuple(data['start'])       # (row, col)
    end = tuple(data['end'])           # (row, col)
    obstacles = [tuple(o) for o in data['obstacles']]  # [(row, col), ...]

    # 動作定義：上、下、左、右
    actions = {
        'up':    (-1, 0),
        'down':  (1, 0),
        'left':  (0, -1),
        'right': (0, 1)
    }
    action_names = list(actions.keys())

    # 為每個非障礙、非終點的格子隨機指定一個確定性策略
    policy = {}
    for r in range(n):
        for c in range(n):
            if (r, c) == end or (r, c) in obstacles:
                policy[(r, c)] = None
            else:
                policy[(r, c)] = random.choice(action_names)

    # 策略評估（迭代法）
    gamma = 0.9
    theta = 1e-6
    V = {}
    for r in range(n):
        for c in range(n):
            V[(r, c)] = 0.0

    max_iterations = 10000
    for iteration in range(max_iterations):
        delta = 0.0
        for r in range(n):
            for c in range(n):
                if (r, c) == end or (r, c) in obstacles:
                    continue

                action = policy[(r, c)]
                dr, dc = actions[action]
                nr, nc = r + dr, c + dc

                # 如果超出邊界或撞到障礙物，則留在原地
                if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in obstacles:
                    nr, nc = r, c

                # reward: 到達終點 +1, 其他 0
                if (nr, nc) == end:
                    reward = 1.0
                else:
                    reward = 0.0

                new_v = reward + gamma * V[(nr, nc)]
                delta = max(delta, abs(new_v - V[(r, c)]))
                V[(r, c)] = new_v

        if delta < theta:
            break

    # 組裝結果
    result = []
    for r in range(n):
        row_data = []
        for c in range(n):
            cell = {
                'row': r,
                'col': c,
                'value': round(V[(r, c)], 4),
                'policy': policy[(r, c)]
            }
            row_data.append(cell)
        result.append(row_data)

    return jsonify({'grid': result, 'iterations': iteration + 1})


@app.route('/value_iteration', methods=['POST'])
def value_iteration():
    """
    使用價值迭代演算法計算最佳政策與 V*(s)。
    """
    data = request.get_json()
    n = data['n']
    start = tuple(data['start'])
    end = tuple(data['end'])
    obstacles = [tuple(o) for o in data['obstacles']]

    # 動作定義
    actions = {
        'up':    (-1, 0),
        'down':  (1, 0),
        'left':  (0, -1),
        'right': (0, 1)
    }
    action_names = list(actions.keys())

    gamma = 0.9
    theta = 1e-6

    # 初始化 V(s)
    V = {}
    for r in range(n):
        for c in range(n):
            V[(r, c)] = 0.0

    # 價值迭代
    max_iterations = 10000
    for iteration in range(max_iterations):
        delta = 0.0
        for r in range(n):
            for c in range(n):
                if (r, c) == end or (r, c) in obstacles:
                    continue

                # 對所有動作取 max
                best_value = float('-inf')
                for action_name in action_names:
                    dr, dc = actions[action_name]
                    nr, nc = r + dr, c + dc

                    # 超出邊界或障礙物 → 留在原地
                    if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in obstacles:
                        nr, nc = r, c

                    reward = 1.0 if (nr, nc) == end else 0.0
                    q_value = reward + gamma * V[(nr, nc)]

                    if q_value > best_value:
                        best_value = q_value

                delta = max(delta, abs(best_value - V[(r, c)]))
                V[(r, c)] = best_value

        if delta < theta:
            break

    # 從 V* 推導最佳政策
    optimal_policy = {}
    for r in range(n):
        for c in range(n):
            if (r, c) == end or (r, c) in obstacles:
                optimal_policy[(r, c)] = None
                continue

            best_action = None
            best_value = float('-inf')
            for action_name in action_names:
                dr, dc = actions[action_name]
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in obstacles:
                    nr, nc = r, c

                reward = 1.0 if (nr, nc) == end else 0.0
                q_value = reward + gamma * V[(nr, nc)]

                if q_value > best_value:
                    best_value = q_value
                    best_action = action_name

            optimal_policy[(r, c)] = best_action

    # 組裝結果
    result = []
    for r in range(n):
        row_data = []
        for c in range(n):
            cell = {
                'row': r,
                'col': c,
                'value': round(V[(r, c)], 4),
                'policy': optimal_policy[(r, c)]
            }
            row_data.append(cell)
        result.append(row_data)

    return jsonify({'grid': result, 'iterations': iteration + 1})


if __name__ == '__main__':
    app.run(debug=True)
