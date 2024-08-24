from flask import jsonify, request, abort, Blueprint
import duckdb

bp = Blueprint('items', __name__, url_prefix='/items')

# 테이블 생성
conn = duckdb.connect('prototype.db')
conn.execute("""
    CREATE SEQUENCE IF NOT EXISTS id_seq START 1 INCREMENT 1
""")
conn.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY DEFAULT nextval('id_seq'),
        name TEXT NOT NULL,
        description TEXT
    )
""")
conn.close()


def get_db_connection():
    try:
        return duckdb.connect('prototype.db')
    except duckdb.Error as e:
        abort(500, description=f"Database connection error: {str(e)}")


# GET 메소드: 모든 아이템 조회
@bp.route('/', methods=['GET'])
def get_items():
    conn = get_db_connection()
    query = "SELECT * FROM items"
    items = conn.execute(query).fetchall()
    conn.close()

    result = {item[0]: {"name": item[1], "description": item[2]} for item in items}
    return jsonify(result)


# GET 메소드: 특정 아이템 조회
@bp.route('/<int:item_id>', methods=['GET'])
def get_item(item_id):
    conn = get_db_connection()
    query = "SELECT * FROM items WHERE id = ?"
    item = conn.execute(query, (item_id,)).fetchone()
    conn.close()
    if item:
        result = {"name": item[1], "description": item[2]}
        return jsonify(result)
    else:
        abort(404, description="Item not found")


# POST 메소드: 새로운 아이템 추가
@bp.route('/', methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        abort(400, description="Bad request, 'name' is required")

    conn = get_db_connection()
    query = "INSERT INTO items (name, description) VALUES (?, ?)"
    conn.execute(query, (request.json['name'], request.json.get('description', "")))

    # 방금 삽입한 아이템을 다시 조회
    select_query = "SELECT id FROM items WHERE name = ? AND description = ? ORDER BY id DESC LIMIT 1"
    new_item_id = conn.execute(select_query, (request.json['name'], request.json.get('description', ""))).fetchone()[0]
    conn.close()

    new_item = {
        "name": request.json['name'],
        "description": request.json.get('description', "")
    }
    return jsonify({new_item_id: new_item}), 201


# PUT 메소드: 특정 아이템 업데이트
@bp.route('/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if not request.json:
        abort(400, description="Bad request")

    conn = get_db_connection()
    query = "SELECT * FROM items WHERE id = ?"
    item = conn.execute(query, (item_id,)).fetchone()

    if not item:
        abort(404, description="Item not found")

    name = request.json.get('name', item[1])
    description = request.json.get('description', item[2])

    update_query = "UPDATE items SET name = ?, description = ? WHERE id = ?"
    conn.execute(update_query, (name, description, item_id))
    conn.close()

    return jsonify({"id": item_id, "name": name, "description": description})


# DELETE 메소드: 특정 아이템 삭제
@bp.route('/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = get_db_connection()
    query = "SELECT * FROM items WHERE id = ?"
    item = conn.execute(query, (item_id,)).fetchone()

    if not item:
        conn.close()
        abort(404, description="Item not found")

    delete_query = "DELETE FROM items WHERE id = ?"
    conn.execute(delete_query, (item_id,))
    conn.close()

    return jsonify({"result": "Item deleted"})
