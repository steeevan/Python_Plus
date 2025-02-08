from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from app.forms import PostForm, CommentForm
from app.models import Post, Like, Comment
from app import db
import os
from werkzeug.utils import secure_filename

posts_bp = Blueprint('posts', __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@posts_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        image_filename = None
        if form.image.data:
            file = form.image.data
            if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                file.save(image_path)
                image_filename = filename
            else:
                flash('Invalid image format.')
                return redirect(url_for('posts.index'))
        post = Post(
            content=form.content.data,
            image=image_filename,
            author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created.')
        return redirect(url_for('posts.index'))
    
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    for post in posts:
        post.comments = post.comments.order_by(Comment.timestamp.asc()).all()
    return render_template('posts/index.html', form=form, posts=posts)

@posts_bp.route('/like/<int:post_id>', methods=['POST'])
@login_required
def like(post_id):
    post = Post.query.get_or_404(post_id)
    like = Like.query.filter_by(user_id=current_user.id, post_id=post.id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
        flash('You unliked the post.')
    else:
        like = Like(user_id=current_user.id, post_id=post.id)
        db.session.add(like)
        db.session.commit()
        flash('You liked the post.')
    return redirect(url_for('posts.index'))

@posts_bp.route('/comment/<int:post_id>', methods=['GET', 'POST'])
@login_required
def comment(post_id):
    post = Post.query.get_or_404(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            user_id=current_user.id,
            post_id=post.id
        )
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been added.')
        return redirect(url_for('posts.index'))
    # Ensure comments are ordered
    ordered_comments = post.comments.order_by(Comment.timestamp.asc()).all()
    return render_template('posts/comment.html', form=form, post=post, comments=ordered_comments)
