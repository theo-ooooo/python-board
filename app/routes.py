from flask import Blueprint, request, jsonify

from app.models import Post

from app import db

bp = Blueprint('board', __name__, url_prefix='/api/posts')


@bp.route('', methods=['POST'])
def create_post():
    data = request.json
    post = Post(title=data['title'], body=data['content'])
    db.session.add(post)
    db.session.commit()

    return jsonify({id: post.id}), 201

@bp.route('', methods=['GET'])
def list_posts():
    posts = Post.query.all()
    return jsonify([{"id": p.id, "title": p.title, "content": p.contentright } for p in posts])

@bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id:int):
    post = Post.query.get_or_404(post_id)
    return jsonify({"id": post.id, "title": post.title, "content": post.content})


@bp.route('/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.json
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({"message": "updated"})

@bp.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "deleted"})